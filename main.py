import datetime
import os
import yfinance as yf
import feedparser
import requests
import google.generativeai as genai

# --- 設定：Gemini API ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# モデル自動選択ロジック
target_model_name = "gemini-pro" # デフォルト（万が一の場合）

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    try:
        print("🔍 利用可能なモデルをスキャン中...")
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
        
        print(f"📋 検出されたモデル一覧: {available_models}")

        # 優先順位ロジック: 1.5 Flash (安定・高速) > 1.0 Pro > その他
        # "models/" という接頭辞が付いている場合があるので部分一致で探す
        best_model = None
        for m in available_models:
            if "gemini-1.5-flash" in m and "001" in m: # 安定版の001を優先
                best_model = m
                break
        
        if not best_model:
            for m in available_models:
                if "gemini-1.5-flash" in m: # バージョン問わずFlash
                    best_model = m
                    break

        if not best_model:
             for m in available_models:
                if "gemini-1.0-pro" in m: # 1.0 Pro
                    best_model = m
                    break
        
        if best_model:
            # "models/" がついているとエラーになる場合があるので削除してセット
            target_model_name = best_model.replace("models/", "")
            print(f"✅ 最適なモデルを選択しました: {target_model_name}")
        else:
            print("⚠️ 最適なモデルが見つかりません。デフォルトの gemini-pro を試行します。")

    except Exception as e:
        print(f"⚠️ モデル一覧の取得に失敗しました: {e}\nデフォルト設定で続行します。")

# --- 設定：ニュースソース ---
RSS_URLS = {
    "economy": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "tech": "https://news.yahoo.co.jp/rss/topics/it.xml",
    "domestic": "https://news.yahoo.co.jp/rss/topics/domestic.xml",
}

# --- 関数群 ---
def get_market_data():
    try:
        nikkei = yf.Ticker("^N225").history(period="1d")['Close'].iloc[-1]
        usd_jpy = yf.Ticker("USDJPY=X").history(period="1d")['Close'].iloc[-1]
        return f"日経平均: {nikkei:,.0f}円", f"ドル円: {usd_jpy:.2f}円"
    except:
        return "Market: 取得失敗", "USD/JPY: 取得失敗"

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

def generate_ai_commentary(news_text, model_name):
    if not GEMINI_API_KEY:
        return "⚠️ APIキー設定なし"

    try:
        # 自動選択されたモデル名を使用
        model = genai.GenerativeModel(model_name)
        
        prompt = f"""
        あなたは「投資家の夫」と「家族」のために情報を整理する優秀なAI編集長です。
        以下のニュースリストを分析し、指定のフォーマットでMarkdown原稿を作成してください。

        【ニュースリスト】
        {news_text}

        【指示】
        1. **トップピック**: 経済・テックの中から「将来への影響が最も大きいニュース」を1つ選び、3行以内で投資家視点の解説をしてください。
        2. **国内フラッシュ**: 国内ニュースの中から「生活に関わる話題」を3つ選び、それぞれ1行で小学生でもわかるように要約してください。
        3. マークダウン形式のみを出力してください。

        【出力フォーマット】
        ## 🌎 今日のトップピック (AI厳選)
        **[選んだニュースのタイトル]**
        > [ここに解説文]

        ## 🇯🇵 国内フラッシュ
        * **[タイトル]**: [1行要約]
        * **[タイトル]**: [1行要約]
        * **[タイトル]**: [1行要約]
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI生成エラー: {str(e)} (Model: {model_name})"

# ==========================================
# メイン処理
# ==========================================
print("🚀 ニュースサイト生成を開始します...")

market_str, usd_str = get_market_data()
weather_str = get_weather_hiroshima()
news_text_for_ai, news_htmls = fetch_news_data()

print(f"🤖 AI執筆開始 (Model: {target_model_name})...")
ai_content = generate_ai_commentary(news_text_for_ai, target_model_name)

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
*Powered by Gemini ({target_model_name}) & GitHub Actions*
"""

with open("index.md", "w", encoding="utf-8") as f:
    f.write(final_md)

print("✅ index.md を更新しました！")
