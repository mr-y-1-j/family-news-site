import datetime
import os
import yfinance as yf
import feedparser
import requests
import google.generativeai as genai

# --- 設定：Gemini API ---
# GitHub Secretsからキーを読み込む
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# --- 設定：ニュースソース ---
RSS_URLS = {
    "economy": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "tech": "https://news.yahoo.co.jp/rss/topics/it.xml",
    "domestic": "https://news.yahoo.co.jp/rss/topics/domestic.xml",
}

# --- 関数 1：市場データ取得 ---
def get_market_data():
    try:
        nikkei = yf.Ticker("^N225").history(period="1d")['Close'].iloc[-1]
        usd_jpy = yf.Ticker("USDJPY=X").history(period="1d")['Close'].iloc[-1]
        return f"日経平均: {nikkei:,.0f}円", f"ドル円: {usd_jpy:.2f}円"
    except:
        return "Market: 取得失敗", "USD/JPY: 取得失敗"

# --- 関数 2：天気取得 ---
def get_weather_hiroshima():
    try:
        url = "https://www.jma.go.jp/bosai/forecast/data/forecast/340000.json"
        data = requests.get(url).json()
        weather = data[0]['timeSeries'][0]['areas'][0]['weathers'][0]
        # 絵文字変換
        icon = "☀️" if "晴" in weather else "☁️" if "曇" in weather else "☔"
        return f"{icon} {weather.split()[0]}" # 最初の天気だけ取る
    except:
        return "天気不明"

# --- 関数 3：ニュース取得（AI用テキスト & 表示用HTML） ---
def fetch_news_data():
    ai_input_text = ""  # AIに読ませる用
    html_outputs = {}   # サイト表示用
    
    for category, url in RSS_URLS.items():
        feed = feedparser.parse(url)
        
        # AI用のテキストを作成（カテゴリごとにタイトルを羅列）
        ai_input_text += f"\n【{category}ニュース】\n"
        
        # HTMLリストを作成
        html_list = "<ul>\n"
        for i, entry in enumerate(feed.entries):
            if i >= 8: break # 各カテゴリ8件まで
            # AI用
            ai_input_text += f"- {entry.title}\n"
            # HTML用
            html_list += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>\n'
        html_list += "</ul>\n"
        
        html_outputs[category] = html_list
        
    return ai_input_text, html_outputs

# --- 関数 4：Geminiに原稿を書かせる（ここが心臓部） ---
def generate_ai_commentary(news_text):
    if not GEMINI_API_KEY:
        return "⚠️ APIキーが設定されていません。Secretsを確認してください。"

    model = genai.GenerativeModel("gemini-1.5-flash") # 最新モデル指定
    
    prompt = f"""
    あなたは「投資家の夫」と「家族」のために情報を整理する優秀なAI編集長です。
    以下のニュースリストを分析し、指定のフォーマットでMarkdown原稿を作成してください。

    【ニュースリスト】
    {news_text}

    【指示】
    1. **トップピック**: 経済・テックの中から「将来への影響が最も大きいニュース」を1つ選び、3行以内で投資家視点の解説をしてください。
    2. **国内フラッシュ**: 国内ニュースの中から「生活に関わる話題」を3つ選び、それぞれ1行で小学生でもわかるように要約してください。
    3. 冒頭の挨拶や「はい、作りました」などの返事は不要です。中身だけ出力してください。

    【出力フォーマット】
    ## 🌎 今日のトップピック (AI厳選)
    **[選んだニュースのタイトル]**
    > [ここに解説文。なぜ重要か？どうなるか？]

    ## 🇯🇵 国内フラッシュ
    * **[タイトル]**: [1行要約]
    * **[タイトル]**: [1行要約]
    * **[タイトル]**: [1行要約]
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI生成エラー: {str(e)}"

# ==========================================
# メイン処理
# ==========================================
print("🚀 ニュースサイト生成を開始します...")

# 1. 各種データ収集
market_str, usd_str = get_market_data()
weather_str = get_weather_hiroshima()
news_text_for_ai, news_htmls = fetch_news_data()

# 2. AIによる原稿生成
print("🤖 Geminiが記事を執筆中...")
ai_content = generate_ai_commentary(news_text_for_ai)

# 3. 最終的なMarkdownの組み立て
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
date_str = now.strftime('%Y年%m月%d日 (%a)')

final_md = f"""# 📰 {date_str} AI Morning News

> **広島の天気**: {weather_str}
> **Market**: 📈 {market_str} / 💵 {usd_str}

{ai_content}

<br>

## 📂 ニュースソース (詳細)
<details>
<summary>経済・ビジネス</summary>
{news_htmls['economy']}
</details>

<details>
<summary>テクノロジー</summary>
{news_htmls['tech']}
</details>

<details>
<summary>国内・社会</summary>
{news_htmls['domestic']}
</details>

---
*Powered by Gemini 2.0 Flash & GitHub Actions*
"""

# 4. ファイル書き出し
with open("index.md", "w", encoding="utf-8") as f:
    f.write(final_md)

print("✅ index.md を更新しました！")
