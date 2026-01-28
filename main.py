import datetime
import os
import yfinance as yf
import feedparser
import requests
import json
import time

# --- 設定 ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

# --- 設定：ニュースソース（NHKをメインに昇格） ---
RSS_URLS = {
    "hiroshima": "https://www.nhk.or.jp/rss/news/pref/hiroshima.xml", # NHK広島（取得しやすい）
    "economy": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "tech": "https://news.yahoo.co.jp/rss/topics/it.xml",
    "domestic": "https://news.yahoo.co.jp/rss/topics/domestic.xml",
}

# --- 関数：RSS取得（シンプルかつ強力に） ---
def fetch_rss(url):
    try:
        # NHKなどは素直なリクエストのほうが通ることがある
        response = requests.get(url, timeout=10)
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
    
    for category, url in RSS_URLS.items():
        feed = fetch_rss(url)
        html_list = "<ul>\n"
        
        if feed and feed.entries:
            ai_input += f"\n【{category}】\n"
            for i, entry in enumerate(feed.entries):
                if i >= 5: break
                ai_input += f"- {entry.title}\n"
                html_list += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>\n'
        else:
            html_list += "<li>⚠️ ニュースの取得に失敗しました</li>"
        
        html_list += "</ul>\n"
        html_outputs[category] = html_list
        
    return ai_input, html_outputs

# --- 関数：AI編集長（自己修復モード） ---
def call_gemini_smart(text):
    if not GEMINI_API_KEY:
        return "⚠️ エラー: APIキーが設定されていません"

    # 1. まず「使えるモデル一覧」をGoogleに聞く
    try:
        list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GEMINI_API_KEY}"
        models_resp = requests.get(list_url).json()
        
        valid_model_name = ""
        
        # エラーチェック（リスト取得さえ失敗した場合）
        if "error" in models_resp:
            return f"⚠️ モデル一覧取得エラー: {models_resp['error']['message']}"
            
        # 2. リストの中から「generateContent」が使えて、FlashかProを含むモデルを探す
        available_models = [m['name'] for m in models_resp.get('models', []) if 'generateContent' in m.get('supportedGenerationMethods', [])]
        
        # 優先順位: Flash > Pro > 1.0
        for m in available_models:
            if "flash" in m and "1.5" in m: valid_model_name = m; break
        if not valid_model_name:
            for m in available_models:
                if "pro" in m and "1.5" in m: valid_model_name = m; break
        if not valid_model_name:
            for m in available_models:
                if "pro" in m and "1.0" in m: valid_model_name = m; break
        # どうしてもなければリストの最初を使う
        if not valid_model_name and available_models:
            valid_model_name = available_models[0]
            
        if not valid_model_name:
            return f"⚠️ 利用可能なモデルが見つかりませんでした。\n検出されたモデル: {available_models}"

        # 3. 見つけたモデル名（例: models/gemini-1.5-flash-001）を使って生成実行
        # モデル名には既に "models/" が含まれていることが多いのでそのまま使う
        generate_url = f"https://generativelanguage.googleapis.com/v1beta/{valid_model_name}:generateContent?key={GEMINI_API_KEY}"
        
        print(f"🤖 選択されたモデル: {valid_model_name}") # ログ用

        today = datetime.date.today().strftime('%m月%d日')
        prompt = f"""
        あなたは親しみやすいニュース編集長です。Markdownで書いてください。
        ソース: {text}
        
        【出力】
        ## 🌎 今日のトップニュース
        大人向けに1つ選び、3行で解説。
        ## 🎓 今日の豆知識 ({today})
        今日の日付に関する雑学を1つ。
        ## 📛 キッズコーナー
        - **🦁 あさのクイズ**: 5歳向けクイズ1問と答え。
        - **✈️ せかい**: 国を1つ紹介し `[🌏 地図](https://www.google.com/maps/search/?api=1&query=国名)` のリンク。
        - **🎨 アート**: 名画を1つ紹介し `[🖼️ 絵を見る](https://www.google.com/search?tbm=isch&q=作品名)` のリンク。
        """
        
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(generate_url, json=payload, headers={'Content-Type': 'application/json'})
        result = response.json()
        
        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"⚠️ AI生成失敗: {json.dumps(result, ensure_ascii=False)}"

    except Exception as e:
        return f"⚠️ 致命的なエラー: {str(e)}"

# --- メイン処理 ---
print("🚀 開始...")

# 市場・天気
market_info = "Market Loading..."
try:
    n = yf.Ticker("^N225").history(period="1d")['Close'].iloc[-1]
    u = yf.Ticker("USDJPY=X").history(period="1d")['Close'].iloc[-1]
    market_info = f"日経: {n:,.0f}円 / 💵 {u:.2f}円"
except: pass

weather_info = "天気不明"
try:
    d = requests.get("https://www.jma.go.jp/bosai/forecast/data/forecast/340000.json").json()
    w = d[0]['timeSeries'][0]['areas'][0]['weathers'][0]
    weather_info = f"{w.split()[0]}"
except: pass

# ニュースとAI
news_text, news_htmls = get_news_data()
ai_content = call_gemini_smart(news_text)

# Markdown生成
dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), 'JST'))
date_str = dt.strftime('%Y/%m/%d')

md = f"""# 📰 {date_str} Family News

> **広島**: {weather_info} | **市場**: {market_info}

{ai_content}

<br>

## 📂 ニュース詳細
<details><summary>🍁 広島のニュース (NHK)</summary>{news_htmls['hiroshima']}</details>
<details><summary>💰 経済・ビジネス</summary>{news_htmls['economy']}</details>
<details><summary>💻 テクノロジー</summary>{news_htmls['tech']}</details>
<details><summary>🚨 国内・社会</summary>{news_htmls['domestic']}</details>

---
*Generated by GitHub Actions & Gemini*
"""

with open("index.md", "w", encoding="utf-8") as f:
    f.write(md)
print("✅ 完了")
