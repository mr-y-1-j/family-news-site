import datetime
import os
import yfinance as yf
import feedparser
import requests
import google.generativeai as genai
import time

# --- 設定：Gemini API ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# --- 設定：ニュースソース ---
RSS_URLS = {
    "economy": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "tech": "https://news.yahoo.co.jp/rss/topics/it.xml",
    "domestic": "https://news.yahoo.co.jp/rss/topics/domestic.xml",
    "hiroshima": "https://news.yahoo.co.jp/rss/l/34.xml",
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

# --- AI編集長（総当たりモード） ---
def generate_ai_content(news_text):
    if not GEMINI_API_KEY: return "⚠️ APIキーが設定されていません"

    # 試行するモデル名のリスト（上から順に試す）
    candidate_models = [
        "gemini-1.5-flash",
        "gemini-1.5-flash-latest",
        "gemini-pro",
        "gemini-1.0-pro"
    ]
    
    today_date = datetime.date.today().strftime('%m月%d日')

    prompt = f"""
    あなたは「家族みんなで見るニュースサイト」の編集長です。
    以下の情報を元に、Markdown形式でコンテンツを作成してください。

    【ニュースソース】
    {news_text}

    【作成ルール】
    1. **トップピック (大人用)**: 
       経済・テック・国内ニュースから「最も重要な1つ」を選び、3行以内で解説。
    
    2. **今日の豆知識 (大人用)**:
       Wikipediaにあるような「{today_date}に関する歴史的な出来事」または「面白い雑学」を1つ紹介。

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

    ## 🎓 今日の豆知識 ({today_date})
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

    # 総当たり実行ループ
    for model_name in candidate_models:
        try:
            print(f"🤖 試行中: {model_name} ...")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            print(f"✅ 成功: {model_name} で生成しました")
            return response.text
        except Exception as e:
            print(f"❌ 失敗: {model_name} - {str(e)}")
            time.sleep(1) # 少し待って次へ
    
    # 全滅した場合のフォールバック（サイト更新を止めないため）
    return """
    ## 🙇‍♂️ AI編集長はお休み中です
    現在、AIサーバーへの接続が混み合っているか、調整中です。
    下のニュースリストから直接記事をご覧ください。
    """

# ==========================================
# メイン処理
# ==========================================
print("🚀 サイト生成開始...")

market, usd = get_market_data()
weather = get_weather_hiroshima()
news_text, news_htmls = fetch_news_data()

# AI執筆（総当たり）
ai_content = generate_ai_content(news_text)

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
