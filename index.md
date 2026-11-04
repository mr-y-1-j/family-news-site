# 🏡 Family Portal 11/04

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 61,556円 | USD: 157.77円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(155.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(60 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">5じ 10ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE5zNUJrR1hGdFdtM3ZBRWdQdjliMG9Tal9aeUk4bzlfRFJYbUpYb1FWZnZVdkJfUHN2aE92RUI4U3JOQU1KWlBoUVE0a01kX0ZoMUY5ZVcwNjNZUXM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島、来季コーチングスタッフ発表 広報から異例転身も…田中＆一岡ら黄金期主力が入閣 - full-count.jp</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMimAFBVV95cUxQQTcweEtxV29uZFM3RE9IbU5PckVSZUtMVFZjWUs1MjJLbGlqQ1Z0N1F6eVZzUGxCLUxWLUR2TUVnOWtDbEFyRTBWZ0ozRmlYUEZnMXhWcjM5MmRJUVY2QVllMU83Vmc0Uld2ZHhPLXhNN2k1OXBScnYwZUwtSlA2WjhKQTJ4RFNVV2VGTS1hT1dmM3VCNm52ddIBngFBVV95cUxQOGwySTNSMjZRYVg4aFhCR3J4Q1JBRkVKc3FzNGhFRkF4cmxrUDFNM2NqNFk2U3l5SGUwSjAtUHJ3RERRM0lYRkM0TTFSR3R2Sk5IM1FFVnhzZzNTY2c2Z1VRMU9qVHpSbFRqUVg5TlUyc04xcTR1TzJoVkIycHpoTEVQYm9fbHJHcVJ1VXpmenJXSG95S3RPX1ZGbVlmUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ちばてつやさんの直筆「ジョー」など展示　広島の筆の里工房で追悼展 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE4wX1BCMTM4WWxOMXZSVEtUbjdsOVBJNndHVjl4S3IzTGFwRWx0dzJ2Q0hBbzY3aGU4dDFkYnZGdWJCalNLZWF5U0JVSHRXUXdJeXZ0NFVmOUpaOWEyQXFhVlVyWEFKcE5JMGFzNUpjRUR4LTJhQzh5czJVV25RUUE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">4日の天気は下り坂・広島（4日午前10時20分放送）（2026年11月3日掲載） - 日テレNEWS NNN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBDR05CVnBMUW1NTkM2TEVjdjFYN2xhLUNwd2NOV1pZekU1a1F1TUk1dE4wY2hnenlVai0wTS1tNlJ5VGJVaUlKbEFiREc4LWduLUtVU1NYb0U2d3I2UGpJRTFieGszQ3hPaFFFbFBIb05wVGFLUFpvM0xlWk9QOHM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・森下暢仁がFA権行使決断 今オフ市場最大の目玉にソフト、巨人など大争奪戦か（スポニチアネックス） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBVSGoxWERfV2Itc0FzZS1sbU9jMG11SWNpQWhEYnAtNGtJMzhET2h4dFNyb3pxTEUtcDFVR0lTNll3akFYbWRQSUg4anhFRElIc0F2cV9DMV93M3M0VDlyNkNZODhoUjN2VG54LVF3V3lNMThSN2pyYmxKQ3RtYW8?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】森下暢仁、国内ＦＡ権行使を決断 宣言残留か移籍か…複数球団が水面下で獲得調査 争奪戦の可能性 床田＆坂倉も今季新たに権利取得（スポーツ報知） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601258?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自治体システム移行費巡り調査へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601082?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO熊谷社長ら 報酬を3カ月減額</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601212?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">豪が追加利上げ 18年ぶり高水準</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601266?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">フードデリバリー業界に淘汰の波</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601141?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">安いもやし限界 5年で13社消える</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601264?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">1兆円盗難 バイナンスが手口公表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601234?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">アソビュー 1500万件超の情報流出</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601209?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMOのサーバー「設計上の不備」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601198?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SNS巡る問題 揺らぐ表現の自由</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601181?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ダークウェブ 日本人の情報流出増</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601253?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">関東一部 5日朝に警報級大雨恐れ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601133?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">トランプ政権に「共感」日本で23%</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601222?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">武部農相 献金巡り新たな疑惑</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601224?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">イタイイタイ病 最後の原告死去</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601223?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">緊急要請 備蓄1週間分並べてみた</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:44</p>
