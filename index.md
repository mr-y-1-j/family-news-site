# 🏡 Family Portal 11/12

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 61,775円 | USD: 159.70円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(237.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(330 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">7じ 55ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1IOGZsR3ZhZGpyT1BkZWo5eXdEOHpTUVlrZnJzZDVUbU9FM0xRSDY5Y3V1aVY3Y1dJUktGVEZiZE50eFpndWVGVjVBNlhydnR3THVoRUFkWFp5QQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【火事】広島市安佐南区でログハウス全焼【動画あり】 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiTkFVX3lxTE0zTDhucXdETVhrQXRPZXFFb0FvWVFtTVRNRjZ3THljVGxFZGJBdVlPbHJvWTg4ZVozV2tNck1HSDROcDNCaG1iMS1OZ2dwQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「公務と治療は生易しいものではない」手術後の松井広島市長 １１月末ニューヨークの会議出席は明言避ける 【広島発】 - FNNプライムオンライン</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1Qb0JjQi1wenpyczB0eTlQa3dkRFZjUDcxSmd4bkdXbUVHamhuNl9XS0hUU1o5TzUyNk0zckw4bjRoWUhWOC01dXBQamM0UU5rOUNUVUIySzdtQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島県東部（備後）と岡山県内のイベント情報＆おでかけガイド【11月12日号】 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE04QWRFQnZaLW5tREs5bHllZ2x4NGZpM3VkS2dxZnFkeC1lTTFsTThvNlpoZUJ1djRjdEphamVTNHg5b3ROTmdKbjFlWkJlaU5oeWdRUnlBOHkwQXluVk9j?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 福山 2階建て住宅全焼 家族5人のうち3人と連絡取れず - NHKニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFB3dWVCVHBheS13RFU4OF9jVGhzNUo1eTh1UGs5cTVJRnkwWVJlbkFtcEIyWjhBbk9NMmQzRlMxUzRsS1BueVJRdTBaclRETDB2UDk1VldIV0FkUTloQnJBc0tKUEtMS2d5YmtvRklWT0FMSktTRE9aYUlINzYwUEU?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">福山市で住宅が全焼 ５人家族のうち３人の安否不明 「ベッドが寝たばこで燃えている」と通報 広島（テレビ新広島） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602271?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">CEOの解任可否を決定へ NVIDIA</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602266?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">CEO去就巡る報道 NVIDIA株下落</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602237?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Amazon出品者「安値強要された」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602231?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Amazon「表示枠」公取なぜ問題視</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602255?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">なぜ ブラックフライデーが長期化</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602254?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">EU「ダークパターン」禁止へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602194?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">警察庁アプリ巡る偽サイトを確認</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602193?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">パスキー設定の証券口座 侵入疑い</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602230?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ドコモ 障害から完全復旧と発表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602172?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">内閣府メルマガ登録アド6万件流出</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602246?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">核「持ち込ませず」例外検討 政府</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602244?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">違憲状態解決策見えず 合区に限界</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602224?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">防衛方針の新概念「拒否力」とは</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602218?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">石破氏 高市政権の高支持率に見解</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602258?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">減税法案 支援金対象は交渉切り札</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 11:34</p>
