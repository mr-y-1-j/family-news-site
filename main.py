import datetime
import os

# 日本時間の現在時刻を取得
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
date_str = now.strftime('%Y年%m月%d日')
time_str = now.strftime('%H:%M')

# サイトの中身（Markdown）を作成
# ここを書き換えることで、サイトのデザインが変わります
content = f"""# 📰 {date_str} のニュース

> **今日のひとこと**
> 現在の時刻は {time_str} です。
> Pythonスクリプトによって、このサイトは自動生成されました！

## 💰 経済・マーケット
<details open>
<summary>市場概況</summary>

* **日経平均**: 取得中...
* **ドル円**: 取得中...

</details>

## 💻 テクノロジー
<details>
<summary>最新テックニュース</summary>

* **AIニュース**: Geminiがすごいらしい。
* **宇宙開発**: 新しいロケットの打ち上げ成功。

</details>

## 🏠 家のこと・メモ
<details>
<summary>共有事項</summary>

* 今週末は買い物に行く予定です。
* **夕食**: 今日は焼肉の予定？🍖

</details>

---
*Last Updated: {date_str} {time_str} (JST)*
"""

# index.md というファイル名で書き出す
with open("index.md", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Webサイトの原稿(index.md)を作成しました！")
