import datetime
import yfinance as yf
import feedparser
import requests

# --- 設定：取得したいニュースのRSSリスト ---
RSS_URLS = {
    "domestic": "https://news.yahoo.co.jp/rss/topics/domestic.xml", # 国内
    "economy": "https://news.yahoo.co.jp/rss/topics/business.xml", # 経済
    "tech": "https://news.yahoo.co.jp/rss/topics/it.xml",           # テクノロジー
}

# --- 関数：株価・為替を取得 ---
def get_market_data():
    try:
        # 日経平均 (^N225)
        nikkei = yf.Ticker("^N225")
        nikkei_price = nikkei.history(period="1d")['Close'].iloc[-1]
        
        # ドル円 (USDJPY=X)
        usd_jpy = yf.Ticker("USDJPY=X")
        usd_price = usd_jpy.history(period="1d")['Close'].iloc[-1]
        
        return f"日経平均: {nikkei_price:,.0f}円", f"ドル円: {usd_price:.2f}円"
    except:
        return "日経平均: 取得失敗", "ドル円: 取得失敗"

# --- 関数：広島の天気予報を取得 (気象庁API) ---
def get_weather_hiroshima():
    try:
        # 広島県(340000)の天気予報JSON
        url = "https://www.jma.go.jp/bosai/forecast/data/forecast/340000.json"
        data = requests.get(url).json()
        
        # 今日の天気
        weather = data[0]['timeSeries'][0]['areas'][0]['weathers'][0]
        # 天気コードから絵文字を簡易判定（本来はもっと細かいですが簡易版で）
        icon = "☀️" if "晴" in weather else "☁️" if "曇" in weather else "☔"
        
        return f"{icon} {weather}"
    except:
        return "天気情報: 取得失敗"

# --- 関数：RSSからニュースリストを作成 ---
def get_rss_news(url, limit=5):
    feed = feedparser.parse(url)
    text = ""
    for i, entry in enumerate(feed.entries):
        if i >= limit: break
        # タイトルとリンクをMarkdownのリストにする
        text += f"* [{entry.title}]({entry.link})\n"
    return text

# ==========================================
# メイン処理
# ==========================================

# 1. データ収集
print("データ収集中...")
nikkei_str, usd_str = get_market_data()
weather_str = get_weather_hiroshima()

# 2. Markdownの組み立て
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
date_str = now.strftime('%Y年%m月%d日 (%a)')
time_str = now.strftime('%H:%M')

content = f"""# 📰 {date_str} Daily News

> **今日の広島の天気**
> {weather_str}
>
> **Market**
> 📈 {nikkei_str} / 💵 {usd_str}

## 💰 経済・ビジネス
<details open>
<summary>Yahoo! 経済ニュース</summary>

{get_rss_news(RSS_URLS['economy'])}

</details>

## 💻 テクノロジー
<details>
<summary>IT・科学</summary>

{get_rss_news(RSS_URLS['tech'])}

</details>

## 🚨 国内・社会
<details>
<summary>主要ニュース</summary>

{get_rss_news(RSS_URLS['domestic'])}

</details>

## 🏠 家のこと・共有
<details>
<summary>家族への伝言</summary>

* **買い物リスト**: 牛乳、パン
* **週末の予定**: 特になし

</details>

---
*Last Updated: {date_str} {time_str}*
"""

# 3. ファイル書き出し
with open("index.md", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ index.md を更新しました")
