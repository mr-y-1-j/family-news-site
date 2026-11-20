# 🏡 Family Portal 11/20

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 56,792円 | USD: 159.21円</span>
</div>


<div style="margin: 20px 0;">
  <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLKeSkfHhKSzLQqP7Rz5z25kMs726xU5p-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 10px;"></iframe>
</div>


通信エラー: Expecting value: line 1 column 1 (char 0)


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


<h2 style="border-bottom: 2px solid #ddd;">🎨 アート & キッズ</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
  <div>
    <div style="background-color: #e8f6f3; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #1abc9c; margin-top: 20px;">
      <h3 style="color: #16a085; margin-top: 0;">⏰ いまなんじ？</h3>
      
    <svg width="200" height="200" viewBox="0 0 100 100" style="background:white; border-radius:50%; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
      <circle cx="50" cy="50" r="45" stroke="#333" stroke-width="3" fill="#fff" />
      <line x1="50" y1="10" x2="50" y2="15" transform="rotate(0 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(30 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(60 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(90 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(120 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(150 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(180 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(210 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(240 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(270 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(300 50 50)" stroke="#333" stroke-width="2" /><line x1="50" y1="10" x2="50" y2="15" transform="rotate(330 50 50)" stroke="#333" stroke-width="2" />
      <text x="50" y="23" font-size="10" text-anchor="middle" font-weight="bold">12</text>
      <text x="80" y="54" font-size="10" text-anchor="middle" font-weight="bold">3</text>
      <text x="50" y="85" font-size="10" text-anchor="middle" font-weight="bold">6</text>
      <text x="20" y="54" font-size="10" text-anchor="middle" font-weight="bold">9</text>
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(275.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(60 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">9じ 10ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBuV2lJZG5uYTA1OFhiQmFRX3NrbUVQWnQ2eFU3TzNwRkRLdTNCMjJLVmptTmNkRWV3LV9CQjg2UlhkczQzYVZKLXVrNTJaQ1g0MWtzVDFSWlpwWXpERzRybUpwLWhydTlQVjVweTFfcXBBSHFuZU95bTVnVVcxOEk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】末包昇大が大幅ダウンで更改 会見で自ら切り出し、ファンに対してゾンビタバコ騒動謝罪（日刊スポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiR0FVX3lxTE1kWkFYMy0waklXWEttQXRPNFRFMHQtRW83VlMzak16YlRwRFJvLVktTGQ2NDdOc1M2R3ZaOGNDdWxPQ3BBY1Bj?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・末包 戦力外通告を「年齢とかも考え」覚悟の契約交渉 １２００万減更改「必死になり枠を奪っていきたい」 - スポーツブル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE5KNG5HVnhWcVJCbm0yLVNPTGY2dGg1ejd0YUtvS2k2YlZpbmpkdHdWYWY4X3A2OTF6WXA0TEhELWM2YjR4ajVqOTc5NlJTSXNTYVI0Zno3Z3JQWU9hWWFhUU1ZQnZ0QndsMzJGZnEzZG3SAXhBVV95cUxQMDRPaUVITTZZbGx5Q2ZrOF9QNURBVFlacndIaDNZaDQ1eUU0RlB5MnRHWDlUVzhCNWZQcTg0Q0owbUJfVjBUeFljbHhodHhLOU90bnppVmtyMEUxeWFiQWstNjZBZTk2OTdmdDJSR1NaQ2NPYnhvOUo?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】末包昇大1200万減で更改「申し訳ない」選手会副会長としてゾンビタバコ巡る騒動謝罪 - 日刊スポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE94Qm9XWnNPQUVXbFp1YVQxRjd5RThSQjdEdVBPdzdvQ0dGM3M0WFdCc3lncGMxcTl2NV9MZm5IcTl5Yk94dklOdXhST0t5dWE1aXZoQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">中日、国内FA行使の広島・床田寛樹と初交渉 工藤新監督迎えた球団の現状説明、大学時代を過ごした岐阜とも深い縁 - 中日新聞Web</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5rN2c4eGtfZDJDMzhZdWlyVTdzMGlhVmtOQ1RBbjh6Wk1qbWdDT09TbjNNYkdmUVpudzVrSWpHclFuWWo4ZU9jRUNBNmdYM1VEdFhwOUVRWXdBMmJfYVVFcGZvaTRGZHYycFd1U3NPQXNlckRjWnFqS280WVVOMFU?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【中日】広島からＦＡ宣言の床田寛樹と初交渉 ２５年リーグ最多６完投の先発左腕に複数年契約を提示へ 中部学院大時代は岐阜で過ごした縁も（スポーツ報知） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603248?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日経平均 一時2800円以上値下がり</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603229?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">アンソロピック 初日終値約97ドル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603253?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">楽天証券の情報流出 遺憾と金融相</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603257?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">楽天証券へ訴訟準備 1.5万人登録</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603224?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">楽天証券に対し集団訴訟の動き</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603220?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">アンソロピック 米ナスダック上場</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603168?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">六花亭 セキュリティコード流出か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603166?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">街に広がるAI画像 どこまで許容?</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603112?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サーバーソフト「nginx」に脆弱性</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603058?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">DHC 顧客氏名など1911万件漏えい</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603216?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市首相 トランプ氏と電話会談</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603228?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相の中国訪問「新ヤルタ」警戒</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603256?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米国頼みの高市外交 限界浮き彫り</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603236?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">21日にかけ寒波 北陸など暴風警戒</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603218?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">麻生氏 アジア大会トラブルに苦言</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 11:43</p>
