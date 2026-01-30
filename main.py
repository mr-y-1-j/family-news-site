import datetime
import os
import yfinance as yf
import feedparser
import requests
import json
import re
import random

# --- 設定 ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
GAS_WEBHOOK_URL = os.environ.get("GAS_WEBHOOK_URL", "").strip()

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
    headers = {"User-Agent": "Mozilla/5.0"}
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
        html_list = '<ul style="list-style-type: none; padding: 0;">\n'
        if feed and feed.entries:
            ai_input += f"\n【{cat}】\n"
            for i, e in enumerate(feed.entries):
                if i >= 5: break
                ai_input += f"- {e.title}\n"
                # 少しデザインを良くする
                html_list += f'<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="{e.link}" target="_blank" style="text-decoration: none; color: #0366d6;">{e.title}</a></li>\n'
        html_list += "</ul>\n"
        html_outputs[cat] = html_list
        
    return ai_input, html_outputs

# --- 関数：動物画像取得 (Kids用) ---
def get_animal_image():
    # 犬か猫をランダムで選ぶ
    is_dog = random.choice([True, False])
    url = ""
    title = ""
    
    try:
        if is_dog:
            resp = requests.get("https://dog.ceo/api/breeds/image/random", timeout=5).json()
            if resp.get("status") == "success":
                url = resp["message"]
                title = "🐶 今日のわんこ"
        else:
            resp = requests.get("https://api.thecatapi.com/v1/images/search", timeout=5).json()
            if resp:
                url = resp[0]["url"]
                title = "🐱 今日のにゃんこ"
                
        if url:
            return f"""
            <div style="text-align: center; margin: 20px 0;">
                <h3 style="color: #555;">{title}</h3>
                <img src="{url}" style="max-height: 300px; max-width: 100%; border-radius: 15px; border: 3px solid #eee;">
            </div>
            """
    except: pass
    return ""

# --- 関数：NASA APOD取得 ---
def get_nasa_apod():
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if "media_type" in data and data["media_type"] == "image":
                return f"""
                <div style="background: linear-gradient(to right, #000428, #004e92); color: white; padding: 15px; border-radius: 10px; margin-top: 20px; text-align: center;">
                  <h4 style="margin: 0 0 10px 0; color: #ffd700;">🔭 NASA Space Photo</h4>
                  <a href="{data['url']}" target="_blank">
                    <img src="{data['url']}" alt="{data.get('title')}" style="max-height: 250px; max-width: 100%; border-radius: 5px;">
                  </a>
                  <p style="font-size: 0.8em; opacity: 0.8;">{data.get('title')}</p>
                </div>
                """
    except: pass
    return ""

# --- 関数：AI編集長 ---
def call_gemini_smart(text):
    if not GEMINI_API_KEY: return "⚠️ エラー: APIキーなし"

    try:
        list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GEMINI_API_KEY}"
        models_resp = requests.get(list_url).json()
        available_models = [m['name'] for m in models_resp.get('models', []) if 'generateContent' in m.get('supportedGenerationMethods', [])]
        
        valid_model_name = ""
        for m in available_models:
            if "flash" in m and "1.5" in m: valid_model_name = m; break
        if not valid_model_name and available_models: valid_model_name = available_models[0]
        
        url = f"https://generativelanguage.googleapis.com/v1beta/{valid_model_name}:generateContent?key={GEMINI_API_KEY}"
        today = datetime.date.today().strftime('%m月%d日')
        
        # プロンプト調整：クイズの答えを隠す、面白豆知識
        prompt = f"""
        あなたは家族新聞のAI編集長です。ソース:{text}
        
        【出力構成】
        1. 挨拶: 「AI編集長です！{today}のニュースをお届けします」
        2. 今日の3大ニュース: 3つ箇条書き。
        3. 豆知識: 「今日は何の日」または面白い雑学を1つ。
        4. クイズ (HTML出力):
           以下の形式で出力してください。答えはDetailsタグで隠すこと。
           <div style="background-color: #e8f8f5; padding: 15px; border-radius: 10px; border: 1px solid #1abc9c; margin-bottom: 10px;">
             <h3 style="color: #16a085; margin-top:0;">🦁 キッズ・クイズ</h3>
             <p style="font-size: 1.1em;">Q. [ここにクイズ問題]</p>
             <details>
               <summary style="cursor: pointer; color: #2980b9; font-weight: bold;">答えを見る！</summary>
               <p style="color: #c0392b; font-weight: bold; font-size: 1.2em; margin-top: 5px;">A. [ここに答え]</p>
             </details>
           </div>
        """
        
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        resp = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        result = resp.json()
        
        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        return "AI生成に失敗しました。"

    except Exception as e: return f"通信エラー: {str(e)}"

# --- ゲーム：おみくじスクリプト (JavaScript) ---
def get_omikuji_script():
    return """
    <div style="background-color: #fff0f5; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #ff69b4; margin: 20px 0;">
      <h2 style="color: #d63384;">🔮 今日の運試し</h2>
      <div id="omikuji-box" style="font-size: 50px; margin: 10px;">📦</div>
      <button onclick="drawOmikuji()" style="background-color: #ff69b4; color: white; border: none; padding: 10px 20px; font-size: 18px; border-radius: 20px; cursor: pointer;">おみくじを引く！</button>
      <div id="omikuji-result" style="font-size: 24px; font-weight: bold; margin-top: 15px; color: #333; min-height: 40px;"></div>
    </div>

    <script>
    function drawOmikuji() {
        const results = [
            "🌸 大吉！ 今日は最高の一日！", 
            "✨ 吉！ いいことあるかも！", 
            "👍 中吉！ 普通が一番！", 
            "🍩 小吉！ おやつを食べよう！", 
            "💪 末吉！ 筋トレしよう！"
        ];
        const emojis = ["🎉", "🌟", "🍀", "🍫", "🔥"];
        const randomIndex = Math.floor(Math.random() * results.length);
        
        const box = document.getElementById("omikuji-box");
        const resultDiv = document.getElementById("omikuji-result");
        
        // 簡易アニメーション
        let count = 0;
        const interval = setInterval(() => {
            box.innerHTML = emojis[count % emojis.length];
            count++;
            if (count > 10) {
                clearInterval(interval);
                box.innerHTML = emojis[randomIndex];
                resultDiv.innerHTML = results[randomIndex];
            }
        }, 100);
    }
    </script>
    """

# --- メイン処理 ---
print("🚀 開始...")

# 市場・天気
market_info = ""
try:
    n = yf.Ticker("^N225").history(period="1d")['Close'].iloc[-1]
    u = yf.Ticker("USDJPY=X").history(period="1d")['Close'].iloc[-1]
    market_info = f"日経: {n:,.0f}円 | USD: {u:.2f}円"
except: pass

weather_info = "天気不明"
try:
    d = requests.get("https://www.jma.go.jp/bosai/forecast/data/forecast/340000.json").json()
    w = d[0]['timeSeries'][0]['areas'][0]['weathers'][0].replace('　', ' ')
    weather_info = f"{w.split()[0]}"
except: pass

news_text, news_htmls = get_news_data()
ai_content = call_gemini_smart(news_text)
nasa_html = get_nasa_apod()
animal_html = get_animal_image()
omikuji_html = get_omikuji_script()

# 日付
dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), 'JST'))
date_str = dt.strftime('%Y/%m/%d')

# Youtube埋め込み (ANNニュースのライブ配信、または最新ニュースリスト)
# ※ライブ配信URLは変わることがあるので、チャンネルのプレイリスト埋め込みが安定
youtube_html = """
<div style="margin: 20px 0;">
  <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLKeSkfHhKSzLQqP7Rz5z25kMs726xU5p-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 10px;"></iframe>
</div>
"""

# Markdown生成
md = f"""# 🏡 Family Portal {dt.strftime('%m/%d')}

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: {weather_info}</span>
  <span>📈 {market_info}</span>
</div>

{youtube_html}

{ai_content}

{omikuji_html}

{animal_html}
{nasa_html}

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary>{news_htmls['hiroshima']}</details>
<details><summary>💰 経済・ビジネス</summary>{news_htmls['economy']}</details>
<details><summary>💻 テクノロジー</summary>{news_htmls['tech']}</details>
<details><summary>🚨 国内・社会</summary>{news_htmls['domestic']}</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: {dt.strftime('%H:%M')}</p>
"""

with open("index.md", "w", encoding="utf-8") as f:
    f.write(md)

# GAS通知 (中身はシンプルに)
if GAS_WEBHOOK_URL:
    try:
        repo = os.environ.get("GITHUB_REPOSITORY", "your-repo")
        user_name = repo.split("/")[0] if "/" in repo else "user"
        repo_name = repo.split("/")[1] if "/" in repo else "repo"
        requests.post(GAS_WEBHOOK_URL, json={
            "date": date_str,
            "summary": "ニュースとクイズが更新されました",
            "url": f"https://{user_name}.github.io/{repo_name}/"
        })
    except: pass

print("✅ 完了")
