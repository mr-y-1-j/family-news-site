import datetime
import os
import yfinance as yf
import feedparser
import requests
import json
import time

# --- 設定 ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

RSS_URLS = {
    "hiroshima": "https://news.yahoo.co.jp/rss/l/34.xml", # 広島
    "economy": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "tech": "https://news.yahoo.co.jp/rss/topics/it.xml",
    "domestic": "https://news.yahoo.co.jp/rss/topics/domestic.xml",
}

# --- 関数：RSS取得（ブロック回避版） ---
def fetch_rss_feed(url):
    try:
        # 魔法の呪文：ブラウザのふりをしてアクセスする（Yahoo等のブロック回避）
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        # 取得したデータを解析
        feed = feedparser.parse(response.content)
        return feed
    except Exception as e:
        print(f"RSS取得エラー ({url}): {e}")
        return None

# --- 関数：ニュースデータ整理 ---
def get_news_data():
    ai_input = ""
    html_outputs = {}
    
    for category, url in RSS_URLS.items():
        feed = fetch_rss_feed(url)
        
        html_list = "<ul>\n"
        ai_input += f"\n【{category}】\n"
        
        if feed and feed.entries:
            for i, entry in enumerate(feed.entries):
                if i >= 8: break
                ai_input += f"- {entry.title}\n"
                html_list += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>\n'
        else:
            html_list += "<li>ニュースの取得に失敗しました</li>"
            
        html_list += "</ul>\n"
        html_outputs[category] = html_list
        
    return ai_input, html_outputs

# --- 関数：AI編集長（直接API通信版） ---
def call_gemini_api(text):
    if not GEMINI_API_KEY:
        return "⚠️ APIキーが設定されていません"

    # 1.5-flash を直接指名（これが一番速くて確実）
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    today = datetime.date.today().strftime('%m月%d日')

    prompt = f"""
    あなたは「家族みんなで見るニュースサイト」の編集長です。
    以下の情報を元に、Markdown形式でコンテンツを作成してください。

    【ニュースソース】
    {text}

    【作成ルール】
    1. **トップピック (大人用)**: 
       経済・テック・国内ニュースから「最も重要な1つ」を選び、3行以内で解説。
    
    2. **今日の豆知識 (大人用)**:
       Wikipediaにあるような「{today}に関する歴史的な出来事」または「面白い雑学」を1つ紹介。

    3. **キッズコーナー (子供用)**:
       5歳の子供向けに、以下の4つを書いてください。
       ※必ず**ひらがなとカタカナ**を中心に、やさしい言葉で書いてください。
       
       - **あさのクイズ**: 科学や生き物の簡単なクイズを1問（答えも書く）。
       - **せかいの国**: ランダムに1つの国を選んで、どんな国か1行で紹介。
         その後に `[🌏 地図を見る](https://www.google.com/maps/search/?api=1&query=国名)` というリンクを付ける。
       - **うちゅうのお話**: 宇宙に関する面白い話を1行で。
       - **きょうの名画**: 有名な絵画を1つ選び、ひらがなで紹介。
         その後に `[🎨 絵を見る](https://www.google.com/search?tbm=isch&q=画家名+作品名)` という画像検索リンクを自動生成して付ける。

    【出力フォーマット】
    ## 🌎 今日のトップピック
    **[ニュースタイトル]**
    > [解説]

    ## 🎓 今日の豆知識 ({today})
    > [豆知識本文]

    ## 📛 キッズコーナー（こどもよう）
    ### 🦁 あさのクイズ
    Q. [クイズ本文]
    **こたえ**: [答え]

    ### ✈️ せかい・うちゅう・アート
    * **せかい**: [国紹介] [リンク]
    * **うちゅう**: [宇宙の話]
    * **アート**: [絵画紹介] [リンク]
    """

    # リクエストデータ作成
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        result = response.json()
        
        # レスポンスからテキストを抽出
        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            print(f"Geminiエラー詳細: {result}")
            return "AI生成に失敗しました（クオータ制限またはフィルタ）"
            
    except Exception as e:
        return f"通信エラー: {str(e)}"

# --- 関数：天気・市場 ---
def get_misc_data():
    try:
        # 市場
        n = yf.Ticker("^N225").history(period="1d")['Close'].iloc[-1]
        u = yf.Ticker("USDJPY=X").history(period="1d")['Close'].iloc[-1]
        market = f"日経: {n:,.0f}円 / ドル: {u:.2f}円"
    except: market = "Market取得中"

    try:
        # 広島天気
        d = requests.get("https://www.jma.go.jp/bosai/forecast/data/forecast/340000.json").json()
        w = d[0]['timeSeries'][0]['areas'][0]['weathers'][0]
        icon = "☀️" if "晴" in w else "☁️" if "曇" in w else "☔"
        weather = f"{icon} {w.split()[0]}"
    except: weather = "天気不明"
    
    return market, weather

# ==========================================
# メイン処理
# ==========================================
print("🚀 サイト生成開始...")

market_str, weather_str = get_misc_data()
news_text, news_htmls = get_news_data()

print("🤖 AI執筆中 (Direct API)...")
ai_content = call_gemini_api(news_text)

# HTML組み立て
t_delta = datetime.timedelta(hours=9)
now = datetime.datetime.now(datetime.timezone(t_delta, 'JST'))
date_str = now.strftime('%Y年%m月%d日 (%a)')

final_md = f"""# 📰 {date_str} Family News

> **広島の天気**: {weather_str}
> **Market**: 📈 {market_str}

{ai_content}

<br>

## 📂 ニュース詳細
<details>
<summary>🍁 広島のニュース</summary>
{news_htmls['hiroshima']}
</details>

<details>
<summary>💰 経済・ビジネス</summary>
{news_htmls['economy']}
</details>

<details>
<summary>💻 テクノロジー</summary>
{news_htmls['tech']}
</details>

<details>
<summary>🚨 国内・社会</summary>
{news_htmls['domestic']}
</details>

---
*Powered by Gemini 1.5 Flash & GitHub Actions*
"""

with open("index.md", "w", encoding="utf-8") as f:
    f.write(final_md)

print("✅ 更新完了")
