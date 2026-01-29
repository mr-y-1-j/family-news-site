import datetime
import os
import yfinance as yf
import feedparser
import requests
import json
import urllib.parse

# --- 設定 ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

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
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        feed = feedparser.parse(response.content)
        if feed.entries:
            return feed
    except:
        pass
    return None

# --- 関数：ニュースデータ収集 ---
def get_news_data():
    ai_input = ""
    html_outputs = {}
    
    # 1. Googleトレンド
    trends_feed = fetch_rss(RSS_URLS["trends"])
    if trends_feed:
        ai_input += "\n【今のホットワード】\n"
        for i, entry in enumerate(trends_feed.entries):
            if i >= 10: break
            ai_input += f"- {entry.title}\n"

    # 2. ニュース
    target_cats = ["hiroshima", "economy", "tech", "domestic"]
    for category in target_cats:
        feed = fetch_rss(RSS_URLS[category])
        html_list = "<ul>\n"
        
        if feed and feed.entries:
            cat_name = "広島ニュース" if category == "hiroshima" else category
            ai_input += f"\n【{cat_name}】\n"
            for i, entry in enumerate(feed.entries):
                if i >= 5: break
                ai_input += f"- {entry.title}\n"
                html_list += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>\n'
        else:
            html_list += "<li>⚠️ ニュースの取得に失敗しました</li>"
        
        html_list += "</ul>\n"
        html_outputs[category] = html_list
        
    return ai_input, html_outputs

# --- 関数：AI編集長（エラー対策版） ---
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

        generate_url = f"https://generativelanguage.googleapis.com/v1beta/{valid_model_name}:generateContent?key={GEMINI_API_KEY}"
        today = datetime.date.today().strftime('%m月%d日')
        
        # プロンプトを分割して記述（エラー防止）
        prompt_intro = f"""
        あなたはAIニュース編集者です。
        【ソース情報】 {text}
        【作成ルール】
        1. 挨拶: 「AIがチョイスしたニュースをお届けします」のみ。
        2. 今日のトップニュース: 重要なニュースを3つ選び、リスト形式。
        3. 今話題のホットワード: 注目ワードを5つ、カンマ区切り。
        4. 今日の豆知識 ({today}): 大人向けの雑学を1つ。
        """

        prompt_kids = """
        5. キッズコーナー (重要):
           ここだけはHTMLタグを使ってデザインしてください。
           以下のdivタグを使い、中身を埋めてください。
           ※漢字禁止。ひらがな・カタカナのみ。
           ※リンクは <a href="URL" target="_blank">もじ</a> を使うこと。

           出力テンプレート:
           <div style="background-color: #fef9e7; padding: 15px; border-radius: 10px; border: 2px solid #f1c40f;">
             <h2 style="color: #e67e22;">📛 キッズコーナー（こどもよう）</h2>
             <h3 style="color: #2e86c1;">🦁 あさのクイズ</h3>
             <p>Q. [ここにクイズ]</p>
             <p><strong>こたえ: [ここに答え]</strong></p>
             <h3 style="color: #27ae60;">🈳 きょうのかんじ</h3>
             <p><span style="font-size: 24px;"><strong>[漢字1文字]</strong></span> ([読み仮名])</p>
             <p>[その漢字の意味を簡単なお話で]</p>
             <h3 style="color: #8e44ad;">✈️ せかい・アート</h3>
             <ul>
               <li><b>せかい</b>: [国名] <a href="https://www.google.com/maps/search/?api=1&query=国名" target="_blank">🌏 ちずをみる</a></li>
               <li><b>アート</b>: [作品名] <a href="https://www.google.com/search?tbm=isch&q=[作品名+画家の検索ワード]" target="_blank">🖼️ えをみる</a></li>
             </ul>
           </div>
        """
        
        # 連結する
        full_prompt = prompt_intro + prompt_kids
        
        payload = {"contents": [{"parts": [{"text": full_prompt}]}]}
        response = requests.post(generate_url, json=payload, headers={'Content-Type': 'application/json'})
        result = response.json()
        
        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"AIエラー: {json.dumps(result, ensure_ascii=False)}"

    except Exception as e:
        return f"通信エラー: {str(e)}"

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
    w = d[0]['timeSeries'][0]['areas'][0]['weathers'][0]
    w = w.replace('　', ' ')
    weather_info = f"{w.split()[0]}"
except: pass

news_text, news_htmls = get_news_data()
ai_content = call_gemini_smart(news_text)

# Markdown生成
dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), 'JST'))
date_str = dt.strftime('%Y/%m/%d')

md = f"""# 📰 {date_str} Family News

> **広島**: {weather_info}
> **市場**: {market_info}

{ai_content}

<br>

## 📂 ニュース詳細
<details><summary>🍁 広島のニュース (Google)</summary>{news_htmls['hiroshima']}</details>
<details><summary>💰 経済・ビジネス</summary>{news_htmls['economy']}</details>
<details><summary>💻 テクノロジー</summary>{news_htmls['tech']}</details>
<details><summary>🚨 国内・社会</summary>{news_htmls['domestic']}</details>

---
*Updated: {dt.strftime('%H:%M')}*
"""

with open("index.md", "w", encoding="utf-8") as f:
    f.write(md)
print("✅ 完了")
