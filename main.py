import datetime
import os
import yfinance as yf
import feedparser
import requests
import json
import time

# --- 設定 ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

# --- 設定：ニュースソース（Googleトレンドを追加、広島修正） ---
RSS_URLS = {
    "trends": "https://trends.google.com/trends/trendingsearches/daily/rss?geo=JP", # ホットワード用
    "hiroshima": "https://www.nhk.or.jp/lnews/hiroshima/rss.xml", # 修正後のNHK広島URL
    "economy": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "tech": "https://news.yahoo.co.jp/rss/topics/it.xml",
    "domestic": "https://news.yahoo.co.jp/rss/topics/domestic.xml",
}

# --- 関数：RSS取得（頑丈版） ---
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
    
    # 1. Googleトレンド（AI入力用のみ）
    trends_feed = fetch_rss(RSS_URLS["trends"])
    if trends_feed:
        ai_input += "\n【今のホットワード（Googleトレンド）】\n"
        for i, entry in enumerate(trends_feed.entries):
            if i >= 10: break
            ai_input += f"- {entry.title}\n"

    # 2. その他ニュース
    target_cats = ["hiroshima", "economy", "tech", "domestic"]
    for category in target_cats:
        feed = fetch_rss(RSS_URLS[category])
        html_list = "<ul>\n"
        
        if feed and feed.entries:
            ai_input += f"\n【{category}ニュース】\n"
            for i, entry in enumerate(feed.entries):
                if i >= 5: break
                ai_input += f"- {entry.title}\n"
                html_list += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>\n'
        else:
            html_list += "<li>⚠️ ニュースの取得に失敗しました</li>"
        
        html_list += "</ul>\n"
        html_outputs[category] = html_list
        
    return ai_input, html_outputs

# --- 関数：AI編集長（改良版） ---
def call_gemini_smart(text):
    if not GEMINI_API_KEY:
        return "⚠️ エラー: APIキー設定なし"

    # モデル自動選択
    try:
        list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GEMINI_API_KEY}"
        models_resp = requests.get(list_url).json()
        available_models = [m['name'] for m in models_resp.get('models', []) if 'generateContent' in m.get('supportedGenerationMethods', [])]
        
        # 優先順位: Flash > Pro
        valid_model_name = ""
        for m in available_models:
            if "flash" in m and "1.5" in m: valid_model_name = m; break
        if not valid_model_name:
            if available_models: valid_model_name = available_models[0]
            
        if not valid_model_name: return "⚠️ モデルが見つかりません"

        generate_url = f"https://generativelanguage.googleapis.com/v1beta/{valid_model_name}:generateContent?key={GEMINI_API_KEY}"
        
        today = datetime.date.today().strftime('%m月%d日')
        
        # プロンプト（指示書）
        prompt = f"""
        あなたはAIニュース編集者です。以下の情報を元にMarkdown原稿を作成してください。
        
        【ソース情報】
        {text}

        【作成ルール】
        1. 挨拶: 「AIがチョイスしたニュースをお届けします」で始める。余計な挨拶はしない。
        
        2. **今日のトップニュース**:
           経済・テック・国内から「重要なニュース」を**3つ**選び、リスト形式で各3行以内で解説。
        
        3. **今話題のホットワード**:
           ソースにある「Googleトレンド」から、特に注目のキーワードを5つ選び、カンマ区切りで列挙（例: #ワード1, #ワード2...）。

        4. **今日の豆知識 ({today})**:
           大人向けの雑学を1つ。

        5. **キッズコーナー (子供用)**:
           5歳の子供向け。**漢字は絶対に使わないでください。すべて「ひらがな」か「カタカナ」のみ。**
           絵文字をたくさん使って楽しくしてください。
           
           - **🦁 あさのクイズ**: 生き物や科学のクイズ1問と答え。
           - **🈳 きょうのかんじ**: 小学校1年生レベルの簡単な漢字を1つ（例：山、川、口など）大きく書き、意味をひらがなで教える。
           - **✈️ せかい**: 国を1つ紹介し `[🌏 ちず](https://www.google.com/maps/search/?api=1&query=国名)` のリンク。
           - **🎨 アート**: 名画を1つ紹介し `[🖼️ えをみる](https://www.google.com/search?tbm=isch&q=作品名)` のリンク。
        """
        
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
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

# 市場・天気 (表を使わずシンプル表示)
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
    # 全角スペースを削除してスッキリさせる
    w = w.replace('　', ' ')
    weather_info = f"{w.split()[0]}"
except: pass

news_text, news_htmls = get_news_data()
ai_content = call_gemini_smart(news_text)

# Markdown生成（枠線なしデザイン）
dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), 'JST'))
date_str = dt.strftime('%Y/%m/%d')

md = f"""# 📰 {date_str} Family News

> **広島**: {weather_info}
> **市場**: {market_info}

{ai_content}

<br>

## 📂 ニュース詳細
<details><summary>🍁 広島のニュース (NHK)</summary>{news_htmls['hiroshima']}</details>
<details><summary>💰 経済・ビジネス</summary>{news_htmls['economy']}</details>
<details><summary>💻 テクノロジー</summary>{news_htmls['tech']}</details>
<details><summary>🚨 国内・社会</summary>{news_htmls['domestic']}</details>

---
*Updated: {dt.strftime('%H:%M')}*
"""

with open("index.md", "w", encoding="utf-8") as f:
    f.write(md)
print("✅ 完了")
