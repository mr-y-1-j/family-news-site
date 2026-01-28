import datetime
import os
import yfinance as yf
import feedparser
import requests
import google.generativeai as genai
import random

# --- 設定：Gemini API ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# モデル自動選択ロジック
target_model_name = "gemini-pro" 
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    try:
        print("🔍 利用可能なモデルをスキャン中...")
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
        
        # 優先順位: 1.5 Flash > 1.0 Pro
        best_model = None
        for m in available_models:
            if "gemini-1.5-flash" in m: best_model = m; break
        if not best_model:
             for m in available_models:
                if "gemini-1.0-pro" in m: best_model = m; break
        
        if best_model:
            target_model_name = best_model.replace("models/", "")
            print(f"✅ モデル選択: {target_model_name}")
    except Exception as e:
        print(f"⚠️ モデル選択エラー: {e}")

# --- 設定：ニュースソース（広島を追加） ---
RSS_URLS = {
    "economy": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "tech": "https://news.yahoo.co.jp/rss/topics/it.xml",
    "domestic": "https://news.yahoo.co.jp/rss/topics/domestic.xml",
    "hiroshima": "https://news.yahoo.co.jp/rss/l/34.xml", # Yahoo!ニュース（広島）
}

# --- 関数群 ---
def get_market_data():
    try:
        nikkei = yf.Ticker("^N225").history(period="1d")['Close'].iloc[-1]
        usd = yf.Ticker("USDJPY=X").history(period="1d")['Close'].iloc[-1]
        return f"日経: {nikkei:,.0f}円", f"ドル: {usd:.2f}円"
    except:
        return "Market取得中", "USD取得中"

def get_weather_hiroshima():
    try:
        url = "https://www.jma.go.jp/bosai/forecast/data/forecast/340000.json"
        data = requests.get(url).json()
        weather = data[0]['timeSeries'][0]['areas'][0]['weathers'][0]
        icon = "☀️" if "晴" in weather else "☁️" if "曇" in weather else "☔"
        return f"{icon} {weather.split()[0]}"
    except:
        return "天気不明"

def fetch_news_data():
    ai_input_text = ""
    html_outputs = {}
    
    for category, url in RSS_URLS.items():
        feed = feedparser.parse(url)
        ai_input_text += f"\n【{category}ニュース】\n"
        html_list = "<ul>\n"
        for i, entry in enumerate(feed.entries):
            if i >= 8: break
            ai_input_text += f"- {entry.title}\n"
            html_list += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>\n'
        html_list += "</ul>\n"
        html_outputs[category] = html_list
        
    return ai_input_text, html_outputs

# --- AI編集長への指示（ここを強化） ---
def generate_ai_content(news_text, model_name):
    if not GEMINI_API_KEY: return "⚠️ APIキーなし"

    try:
        model = genai.GenerativeModel(model_name)
        
        # 今日の日付から豆知識を出すために日付取得
        today = datetime.date.today().strftime('%m月%d日')

        prompt = f"""
        あなたは「家族みんなで見るニュースサイト」の編集長です。
        以下の情報を元に、Markdown形式でコンテンツを作成してください。

        【ニュースソース】
        {news_text}

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
             その後に `[🌏 地図を見る](https://www.google.com/maps/search/国名)` というリンクを付ける。
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
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI生成エラー: {str(e)}"

# ==========================================
# メイン処理
# ==========================================
print("🚀 サイト生成開始...")

market, usd = get_market_data()
weather = get_weather_hiroshima()
news_text, news_htmls = fetch_news_data()

print(f"🤖 AI執筆中 ({target_model_name})...")
ai_content = generate_ai_content(news_text, target_model_name)

# HTML組み立て
t_delta = datetime.timedelta(hours=9)
now = datetime.datetime.now(datetime.timezone(t_delta, 'JST'))
date_str = now.strftime('%Y年%m月%d日 (%a)')

final_md = f"""# 📰 {date_str} Family News

> **広島の天気**: {weather}
> **Market**: 📈 {market} / 💵 {usd}

{ai_content}

<br>

## 📂 ニュース詳細
<details>
<summary>🍁 広島のニュース</summary>
{news_htmls.get('hiroshima', '取得失敗')}
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
*Powered by Gemini & GitHub Actions*
"""

with open("index.md", "w", encoding="utf-8") as f:
    f.write(final_md)

print("✅ 更新完了")
