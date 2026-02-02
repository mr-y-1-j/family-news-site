import datetime
import os
import yfinance as yf
import feedparser
import requests
import json
import re
import random
import math

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
                html_list += f'<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="{e.link}" target="_blank" style="text-decoration: none; color: #0366d6;">{e.title}</a></li>\n'
        html_list += "</ul>\n"
        html_outputs[cat] = html_list
        
    return ai_input, html_outputs

# --- 関数：時計クイズSVG生成 (Kids用) ---
def get_clock_quiz():
    # ランダムな時刻を生成 (5分刻みにして読みやすくする)
    h = random.randint(1, 12)
    m = random.randint(0, 11) * 5
    
    # 針の角度計算
    # 短針: (時間 + 分/60) * 30度
    h_angle = (h % 12 + m / 60.0) * 30
    # 長針: 分 * 6度
    m_angle = m * 6

    # SVG描画
    svg = f"""
    <svg width="200" height="200" viewBox="0 0 100 100" style="background:white; border-radius:50%; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
      <circle cx="50" cy="50" r="45" stroke="#333" stroke-width="3" fill="#fff" />
      {''.join([f'<line x1="50" y1="10" x2="50" y2="15" transform="rotate({i*30} 50 50)" stroke="#333" stroke-width="2" />' for i in range(12)])}
      <text x="50" y="23" font-size="10" text-anchor="middle" font-weight="bold">12</text>
      <text x="80" y="54" font-size="10" text-anchor="middle" font-weight="bold">3</text>
      <text x="50" y="85" font-size="10" text-anchor="middle" font-weight="bold">6</text>
      <text x="20" y="54" font-size="10" text-anchor="middle" font-weight="bold">9</text>
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate({h_angle} 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate({m_angle} 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    """
    
    html = f"""
    <div style="background-color: #e8f6f3; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #1abc9c; margin-top: 20px;">
      <h3 style="color: #16a085; margin-top: 0;">⏰ いまなんじ？</h3>
      {svg}
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">{h}じ {m}ふん</p>
      </details>
    </div>
    """
    return html

# --- 関数：名画スライドショー (Art Institute of Chicago API) ---
def get_art_slideshow():
    # 印象派などの美しい絵画を検索
    api_url = "https://api.artic.edu/api/v1/artworks/search?q=impressionism&fields=id,title,image_id,artist_display&limit=5"
    html_parts = ""
    
    try:
        resp = requests.get(api_url, timeout=10)
        data = resp.json()
        config_url = data.get('config', {}).get('iiif_url', 'https://www.artic.edu/iiif/2')
        
        slides = []
        for item in data.get('data', []):
            img_id = item.get('image_id')
            if img_id:
                # IIIF形式の画像URLを作成
                full_url = f"{config_url}/{img_id}/full/600,/0/default.jpg"
                title = item.get('title', 'Unknown')
                artist = item.get('artist_display', 'Unknown')
                slides.append(f"""
                <div class="mySlides" style="display:none; text-align: center;">
                    <img src="{full_url}" style="width:100%; max-height:400px; object-fit: contain; border-radius: 5px;">
                    <p style="font-size: 0.9em; margin: 5px 0;"><b>{title}</b><br><span style="color:#666; font-size:0.8em;">{artist}</span></p>
                </div>
                """)
        
        if slides:
            # 1枚目だけ display:block に書き換える (JS読み込み前のチラつき防止)
            slides[0] = slides[0].replace('display:none', 'display:block')
            
            html_parts = f"""
            <div style="background-color: #fdfefe; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-top: 20px;">
                <h3 style="margin-top:0; color: #555;">🖼️ 今日の名画ギャラリー</h3>
                {''.join(slides)}
                <script>
                var slideIndex = 0;
                carousel();
                function carousel() {{
                    var i;
                    var x = document.getElementsByClassName("mySlides");
                    for (i = 0; i < x.length; i++) {{
                        x[i].style.display = "none";  
                    }}
                    slideIndex++;
                    if (slideIndex > x.length) {{slideIndex = 1}}    
                    x[slideIndex-1].style.display = "block";  
                    setTimeout(carousel, 5000); // 5秒ごとに切り替え
                }}
                </script>
                <p style="text-align: right; font-size: 0.7em; color: #aaa;">Powered by Art Institute of Chicago</p>
            </div>
            """
            return html_parts

    except Exception as e:
        print(f"Art API Error: {e}")
        
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
        
        # プロンプト：クイズは別関数にしたので、ここではニュース解説と豆知識に集中
        prompt = f"""
        あなたは家族新聞のAI編集長です。ソース:{text}
        
        【出力構成】
        1. 挨拶: 「AI編集長です！{today}のニュースをお届けします」
        2. 今日の3大ニュース: 3つ箇条書き。
        3. 豆知識: 「今日は何の日」または面白い雑学を1つ。
        """
        
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        resp = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        result = resp.json()
        
        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        return "AI生成に失敗しました。"

    except Exception as e: return f"通信エラー: {str(e)}"

# --- ゲーム：おみくじスクリプト（修正版） ---
def get_omikuji_script():
    # 注意: ここはインデントを付けず、左端に詰めて書くこと！
    return """
<div style="background-color: #fff0f5; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #ff69b4; margin: 20px 0;">
  <h2 style="color: #d63384;">🔮 今日の運試し</h2>
  <div id="omikuji-box" style="font-size: 50px; margin: 10px;">📦</div>
  <button onclick="drawOmikuji()" style="background-color: #ff69b4; color: white; border: none; padding: 10px 20px; font-size: 18px; border-radius: 20px; cursor: pointer;">おみくじを引く！</button>
  <div id="omikuji-result" style="font-size: 24px; font-weight: bold; margin-top: 15px; color: #333; min-height: 40px;"></div>
</div>
<script>
function drawOmikuji() {
    const results = ["🌸 大吉！", "✨ 吉！", "👍 中吉！", "🍩 小吉！", "💪 末吉！"];
    const emojis = ["🎉", "🌟", "🍀", "🍫", "🔥"];
    const randomIndex = Math.floor(Math.random() * results.length);
    const box = document.getElementById("omikuji-box");
    const resultDiv = document.getElementById("omikuji-result");
    let count = 0;
    const interval = setInterval(() => {
        box.innerHTML = emojis[count % emojis.length]; count++;
        if (count > 10) { clearInterval(interval); box.innerHTML = emojis[randomIndex]; resultDiv.innerHTML = results[randomIndex]; }
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

# 各パーツ生成
omikuji_html = get_omikuji_script()
clock_html = get_clock_quiz()  # 時計クイズ
art_html = get_art_slideshow() # 名画スライドショー

# 日付
dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), 'JST'))
date_str = dt.strftime('%Y/%m/%d')

# Youtube
youtube_html = """
<div style="margin: 20px 0;">
  <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLKeSkfHhKSzLQqP7Rz5z25kMs726xU5p-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 10px;"></iframe>
</div>
"""

# Markdown生成 (配置調整：上部はニュース、下部はキッズ＆アート)
md = f"""# 🏡 Family Portal {dt.strftime('%m/%d')}

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: {weather_info}</span>
  <span>📈 {market_info}</span>
</div>

{youtube_html}

{ai_content}

{omikuji_html}

<h2 style="border-bottom: 2px solid #ddd;">🎨 アート & キッズ</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
  <div>{clock_html}</div>
  <div>{art_html}</div>
</div>

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

# GAS通知
if GAS_WEBHOOK_URL:
    try:
        repo = os.environ.get("GITHUB_REPOSITORY", "your-repo")
        user_name = repo.split("/")[0] if "/" in repo else "user"
        repo_name = repo.split("/")[1] if "/" in repo else "repo"
        requests.post(GAS_WEBHOOK_URL, json={
            "date": date_str,
            "summary": "ニュース・時計クイズ・名画を更新しました",
            "url": f"https://{user_name}.github.io/{repo_name}/"
        })
    except: pass

print("✅ 完了")
