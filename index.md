# 🏡 Family Portal 11/15

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 雨</span>
  <span>📈 日経: 61,142円 | USD: 159.88円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(295.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(300 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">9じ 50ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5yYXJjY2Fja0pRUkcyVWtwNW5SQ1l4RDZJZE1pVkp0V3J1S3RITnduVTFaRlUzSTdKYzQ4clBqTTU0ZUo3MTdwb0ZJZE03cERCcWdvNDZXenJRQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">春高バレー広島代表 女子は進徳、男子は崇徳に決定 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE16VU1XQS1TWC1sRHhFMHh6QUtyMHNObFdNa0UybGhlUnJhLUZhVmZzWVd1QWRRREpHbWtTSTQxdnIwVXA0QWhhMDBtQ0IydzVVVXZIT1RKODg5b2RMVEh1UllHaEg0R2I4T3ZMQXVpX25acTJ0QWN2ak9hUGc0MFE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">田村俊介がトライアウトへ決意「いい姿をアピールしたい」今季限りで広島を戦力外もファームでは打率３割超え「シーズン通りにプレーできれば」（デイリースポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBTWE13a1RSV1JWbTc4YkwwZDQ3MFBKZkozd2kxa2JCQ25UUHZfSmNXQV9fVXh5enc2NnBIMjFERW9ILXR2bVVhSGJNRXJKam5UWlRPS3ppU3hZbnZsNUF1MmR0cFIzV1ll?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">復興の象徴、広島の路面電車 被爆100年、つなぐ平和 - 毎日新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBxSlhBSmZYUnJpQWRJemtXMTJTcExyZlFxam9STERGX0liSXNWcTZ2Y1RsY1VkbEQ3NjNLazVfTGlnVmlOU24zNnZla0lKOGpxYmVMOWJjc01GZzhDbXh2enpfY2lWS09OQVJvRWVGd0NydEk1N1FTNjhKN0R1TEk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・新井監督 来春キャンプ１、２軍振り分け材料に筋力測定数値「オフに継続し、意識を高く持ってやることがすごく大事」 - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1ndFZ2cjVia1hPdjEyT09NbzFfNHpLWGpxV2NyWFpQRVNBb05pd0tmdUV6RjJwbExjVG9ibzJiZVFxQVNhaE9xVmNwMm1MTmJrR3puRkFtNnNCeWF1LTJjd2dXeXBvak1lZDNrMDVIMDZYdEhfZWtnOE5ONkZHVlk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 国内ＦＡ権行使の坂倉将吾「悩んで、長引かせても迷うだけ」去就決定時期に言及 ロッテとは面会済み（デイリースポーツ） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602554?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">エヌビディアCEO 後任選定難航か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602572?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">売れ残りを寄付 広がる一方問題も</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602636?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">月収2万円と年金5万円 70代の現実</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602575?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">スバルWRXのMT車復活 要望受け</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602597?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">縦型ショートドラマ トラブル急増</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602619?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Netflixが値上げ 最安は990円に</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602602?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AI悪用攻撃拠点か 世界で千台発見</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602556?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">マイクロソフトの障害 全面復旧</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602606?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">MS 障害原因は過去の増強作業</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602508?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">マイクロソフト 大規模障害を謝罪</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602621?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">きょう近畿や東海で激しい雨 注意</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602615?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相 「アジア版IEA」創設提唱へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602584?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米中露の接近 日本政府は危機感</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602620?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">横田さん拉致49年 母が思い吐露</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602551?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">関東15日は気温急降下 師走並みか</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:25</p>
