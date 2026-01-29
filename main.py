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
    # 広島ニュース（Googleニュース検索結果のRSS）
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
                # HTMLリスト（ターゲットブランク対応）
                html_list += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>\n'
        else:
            html_list += "<li>⚠️ ニュースの取得に失敗しました</li>"
        
        html_list += "</ul>\n"
        html_outputs[category] = html_list
        
    return ai_input, html_outputs

# --- 関数：AI編集長（デザイン強化版） ---
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

        # 生成実行
        generate_url = f"https://generativelanguage.googleapis.com/v1beta/{valid_model_name}:generateContent?key={GEMINI_API_KEY}"
        today = datetime.date.today().strftime('%m月%d日')
        
        prompt = f"""
        あなたはAIニュース編集者です。
        
        【ソース情報】
        {text}

        【作成ルール】
        1. 挨拶: 「AIがチョイスしたニュースをお届けします」のみ。
        
        2. **今日のトップニュース**:
           重要なニュースを3つ選び、リスト形式。リンク不要。
        
        3. **今話題のホットワード**:
           注目ワードを5つ、カンマ区切り。

        4. **今日の豆知識 ({today})**:
           大人向けの雑学を1つ。

        5. **キッズコーナー (重要)**:
           ここだけは**HTMLタグ**を使ってデザインしてください。
           以下の `<div style...>` から `</div>` までをそのまま使い、中身を埋めてください。
           ※漢字禁止。ひらがな・カタカナのみ。
           ※リンクは必ず `<a href="URL" target
