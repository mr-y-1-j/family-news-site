import datetime
import os
import yfinance as yf
import feedparser
import requests
import json
import time

# --- 設定：APIキー（前後の空白を自動削除） ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

# --- 設定：ニュースソース（広島はNHKも予備で追加） ---
RSS_URLS = {
    "hiroshima_yahoo": "https://news.yahoo.co.jp/rss/l/34.xml",
    "hiroshima_nhk": "https://www.nhk.or.jp/rss/news/pref/hiroshima.xml", # 予備
    "economy": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "tech": "https://news.yahoo.co.jp/rss/topics/it.xml",
    "domestic": "https://news.yahoo.co.jp/rss/topics/domestic.xml",
}

# --- 関数：強力なRSS取得 ---
def fetch_rss_feed_robust(url):
    # 複数のUser-Agentを試す（ブロック回避）
    user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "RSSReader/1.0"
    ]
    
    for ua in user_agents:
        try:
            response = requests.get(url, headers={"User-Agent": ua}, timeout=10)
            if response.status_code == 200:
                feed = feedparser.parse(response.content)
                if feed.entries:
                    return feed
        except:
            continue
    return None

# --- 関数：ニュースデータ整理 ---
def get_news_data():
    ai_input = ""
    html_outputs = {}
    
    # 広島ニュース（YahooがだめならNHKを試す）
    feed = fetch_rss_feed_robust(RSS_URLS["hiroshima_yahoo"])
    if not feed or not feed.entries:
        feed = fetch_rss_feed_robust(RSS_URLS["hiroshima_nhk"])
    
    # 広島のHTML生成
    html_list = "<ul>\n"
    if feed and feed.entries:
        ai_input += "\n【広島のニュース】\n"
        for i, entry in enumerate(feed.entries):
            if i >= 5: break
            ai_input += f"- {entry.title}\n"
            html_list += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>\n'
    else:
        html_list += "<li>⚠️ ニュースが取得できませんでした（アクセス制限の可能性）</li>"
    html_list += "</ul>\n"
    html_outputs["hiroshima"] = html_list

    # その他のカテゴリ
    for cat in ["economy", "tech", "domestic"]:
        feed = fetch_rss_feed_robust(RSS_URLS[cat])
        html_list = "<ul>\n"
        ai_input += f"\n【{cat}】\n"
        if feed and feed.entries:
            for i, entry in enumerate(feed.entries):
                if i >= 5: break
                ai_input += f"- {entry.title}\n"
                html_list += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>\n'
        html_list += "</ul>\n"
        html_outputs[cat] = html_list
        
    return ai_input, html_outputs

# --- 関数：AI編集長（デバッグ機能付き） ---
def call_gemini_api_debug(text):
    if not GEMINI_API_KEY:
        return "⚠️ **エラー**: GitHub Secretsに `GEMINI_API_KEY` が設定されていません。"

    # エンドポイント：v1beta の gemini-1.5-flash を使用
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    today = datetime.date.today().strftime('%m月%d日')
    
    prompt = f"""
    あなたは子供を持つ親向けのニュースサイト編集長です。Markdown形式で出力してください。
    
    【ソース】
    {text}

    【出力項目】
    1. ## 🌎 今日のトップニュース
       大人向けに1つ選び、3行で解説。
    2. ## 🎓 今日の豆知識 ({today})
       今日の日付に関する雑学を1つ。
    3. ## 📛 キッズコーナー
       - **🦁 あさのクイズ**: 5歳向けクイズ1問と答え。
       - **✈️ せかい**: 国を1つ紹介し `[🌏 地図](https://www.google.com/maps?q=国名)` のリンクをつける。
       - **🎨 アート**: 名画を1つ紹介し `[🖼️ 絵を見る](https://www.google.com/search?tbm=isch&q=作品名)` のリンクをつける。
    """

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        result = response.json()
        
        # 成功判定
        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        
        # 失敗した場合：エラー内容をそのまま画面に出す（これがデバッグに重要）
        error_msg = json.dumps(result, indent=2, ensure_ascii=False)
        return f"""
        ## 🙇‍♂️ AI生成エラー
        Googleから以下のエラーが返ってきました。この内容を確認してください。
        
        ```json
        {error_msg}
        ```
        
        **よくある原因と対策:**
        * `429 RESOURCE_EXHAUSTED`: 無料枠の使いすぎです。数分待てば直ります。
        * `400 INVALID_ARGUMENT`: APIキーが無効です。コピーミスがないか確認してください。
        * `404 NOT_FOUND`: モデル名が間違っています（現在は gemini-1.5-flash を使用）。
        """

    except Exception as e:
        return f"## ⚠️ 通信エラー\n\n`{str(e)}`"

# --- メイン処理 ---
print("🚀 開始...")
market_info = "Market Data Loading..."
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

news_text, news_htmls = get_news_data()
ai_content = call_gemini_api_debug(news_text)

# Markdown組み立て
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
print("✅ 完了")
