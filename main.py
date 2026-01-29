import datetime
import os
import yfinance as yf
import feedparser
import requests
import json
import re

# --- 設定 ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
GAS_WEBHOOK_URL = os.environ.get("GAS_WEBHOOK_URL", "").strip() # 追加

# --- 設定：ニュースソース ---
RSS_URLS = {
    "trends": "https://trends.google.com/trends/trendingsearches/daily/rss?geo=JP",
    "hiroshima": "https://news.google.com/rss/search?q=%E5%BA%83%E5%B3%B6&hl=ja&gl=JP&ceid=JP:ja",
    "economy": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "tech": "https://news.yahoo.co.jp/rss/topics/it.xml",
    "domestic": "https://news.yahoo.co.jp/rss/topics/domestic.xml",
}

# --- 関数：RSS取得 ---
def fetch_rss(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        feed = feedparser.parse(response.content)
        if feed.entries: return feed
    except: pass
    return None

# --- 関数：ニュースデータ収集 ---
def get_news_data():
    ai_input = ""
    html_outputs = {}
    
    # トレンド
    trends = fetch_rss(RSS_URLS["trends"])
    if trends:
        ai_input += "\n【ホットワード】\n"
        for i, e in enumerate(trends.entries):
            if i >= 10: break
            ai_input += f"- {e.title}\n"

    # 各ニュース
    for cat in ["hiroshima", "economy", "tech", "domestic"]:
        feed = fetch_rss(RSS_URLS[cat])
        html_list = "<ul>\n"
        if feed and feed.entries:
            ai_input += f"\n【{cat}】\n"
            for i, e in enumerate(feed.entries):
                if i >= 5: break
                ai_input += f"- {e.title}\n"
                html_list += f'<li><a href="{e.link}" target="_blank">{e.title}</a></li>\n'
        html_list += "</ul>\n"
        html_outputs[cat] = html_list
        
    return ai_input, html_outputs

# --- 関数：AI編集長 ---
def call_gemini_smart(text):
    if not GEMINI_API_KEY: return "⚠️ エラー: APIキーなし"

    try:
        # モデル自動検出
        list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GEMINI_API_KEY}"
        models_resp = requests.get(list_url).json()
        available_models = [m['name'] for m in models_resp.get('models', []) if 'generateContent' in m.get('supportedGenerationMethods', [])]
        
        valid_model_name = ""
        for m in available_models:
            if "flash" in m and "1.5" in m: valid_model_name = m; break
        if not valid_model_name and available_models: valid_model_name = available_models[0]
        if not valid_model_name: return "⚠️ モデル不明"

        # 生成
        url = f"https://generativelanguage.googleapis.com/v1beta/{valid_model_name}:generateContent?key={GEMINI_API_KEY}"
        today = datetime.date.today().strftime('%m月%d日')
        
        prompt = f"""
        あなたはAI編集者です。ソース:{text}
        
        【ルール】
        1. 挨拶: 「AIがチョイスしたニュースをお届けします」のみ。
        2. 今日のトップニュース: 3つ選びリスト形式。
        3. ホットワード: 5つカンマ区切り。
        4. 豆知識 ({today}): 1つ。
        5. キッズコーナー: 以下のHTMLテンプレートを使用。漢字禁止。リンクはtarget="_blank"。
           <div style="background-color: #fef9e7; padding: 15px; border-radius: 10px; border: 2px solid #f1c40f;">
             <h2 style="color: #e67e22;">📛 キッズコーナー</h2>
             <h3 style="color: #2e86c1;">🦁 あさのクイズ</h3>
             <p>Q. [クイズ]</p><p><strong>こたえ: [答え]</strong></p>
             <h3 style="color: #27ae60;">🈳 きょうのかんじ</h3>
             <p><span style="font-size: 24px;"><strong>[漢字]</strong></span> ([よみ])</p><p>[いみ]</p>
             <h3 style="color: #8e44ad;">✈️ せかい・アート</h3>
             <ul>
               <li><b>せかい</b>: [国] <a href="https://www.google.com/maps/search/?api=1&query=国名" target="_blank">🌏 ちず</a></li>
               <li><b>アート</b>: [絵] <a href="https://www.google.com/search?tbm=isch&q=[ワード]" target="_blank">🖼️ え</a></li>
             </ul>
           </div>
        """
        
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        resp = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        result = resp.json()
        
        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        return f"AIエラー: {json.dumps(result)}"

    except Exception as e: return f"通信エラー: {str(e)}"

# --- 関数：GASへ通知 ---
def notify_gas(ai_text, date_str):
    if not GAS_WEBHOOK_URL:
        print("⚠️ GAS_WEBHOOK_URLが未設定のため、通知をスキップします")
        return

    # AIのテキストから「今日のトップニュース」の部分だけ簡易的に抜き出す
    # (正規表現で "トップニュース" の次行から空行までを取得するイメージ)
    summary = "サイトをご確認ください"
    try:
        # "トップニュース" という言葉が含まれる行を探し、そこから数行を抜き出す
        match = re.search(r'(トップニュース.*?)(?=\n\n|\n#)', ai_text, re.DOTALL)
        if match:
            # マークダウンの記号(*とか)を少し綺麗にする
            summary = match.group(1).replace('**', '').strip()
    except:
        pass

    # GitHub PagesのURL (リポジトリ名から自動推測または手動設定)
    # ここでは固定値としてあなたのURL形式をセットします
    repo = os.environ.get("GITHUB_REPOSITORY", "your-repo") # "User/Repo"
    user_name = repo.split("/")[0]
    repo_name = repo.split("/")[1]
    site_url = f"https://{user_name}.github.io/{repo_name}/"

    payload = {
        "date": date_str,
        "summary": summary,
        "url": site_url
    }
    
    try:
        requests.post(GAS_WEBHOOK_URL, json=payload)
        print("✅ GASへ通知を送りました")
    except Exception as e:
        print(f"⚠️ GAS通知エラー: {e}")

# --- メイン処理 ---
print("🚀 開始...")

# 市場・天気
market_info = "Loading..."
try:
    n = yf.Ticker("^N225").history(period="1d")['Close'].iloc[-1]
    u = yf.Ticker("USDJPY=X").history(period="1d")['Close'].iloc[-1]
    market_info = f"日経: {n:,.0f}円  |  ドル円: {u:.2f}円"
except: pass

weather_info = "天気不明"
try:
    d = requests.get("https://www.jma.go.jp/bosai/forecast/data/forecast/340000.json").json()
    w = d[0]['timeSeries'][0]['areas'][0]['weathers'][0].replace('　', ' ')
    weather_info = f"{w.split()[0]}"
except: pass

news_text, news_htmls = get_news_data()
ai_content = call_gemini_smart(news_text)

# Markdown
dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), 'JST'))
date_str = dt.strftime('%Y/%m/%d')
md = f"""# 📰 {date_str} Family News

> **広島**: {weather_info} | **市場**: {market_info}

{ai_content}

<br>

## 📂 ニュース詳細
<details><summary>🍁 広島のニュース</summary>{news_htmls['hiroshima']}</details>
<details><summary>💰 経済・ビジネス</summary>{news_htmls['economy']}</details>
<details><summary>💻 テクノロジー</summary>{news_htmls['tech']}</details>
<details><summary>🚨 国内・社会</summary>{news_htmls['domestic']}</details>

---
*Updated: {dt.strftime('%H:%M')}*
"""

with open("index.md", "w", encoding="utf-8") as f:
    f.write(md)

# 最後にGAS通知を実行
notify_gas(ai_content, date_str)

print("✅ 完了")
