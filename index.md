# 🏡 Family Portal 11/18

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 58,697円 | USD: 159.40円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(330.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(0 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">11じ 0ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1mSVlxRERJVmZkNDQ5cllVSWtMQ2lfU0tvdHlUYV9RUnZycThOY2UtNElVU1RUUTRUZ0VhRGxGRjBRckV3SDd4T1RxanExRGJELXVhb0FKVDU2Zw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島県の新病院建設計画、概算工事費が929億円に ゼネコンのフジタなど提示 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBpYTYyaHJIZnl6Q0xKd1FUM3A3VU5YcDV4U3RtUFpKLWxUN0F4Z1N4TXJody1uYnpGQWdENDZkVDNXeW5KUDFGZHVRdktSRlFCYS1CWHRYVUNfTVo4bE5vXzFEN0k1OGhJZFZKQ0dKMDZ6Q0lORDA1UmlVRXM3NTA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島、江夏豊さんを追悼 「江夏の21球」で日本一に貢献 練習は喪章着用、半旗で実施（スポニチアネックス） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBnMHRIZkNWQktlZ2RXOFZUQ1I1cDFNazc1cWprTDM2RTA5SFRicXVxOVBGc3drbFlTWDRLSDhScjBqdENVN3lRNnl0ek4zS1F4QnZLYmhvWkZMX2hFNE5wNlJHRTFoWVU?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">生きたシカを…東広島産ジビエが人気、狩猟に同行して見えた手法は [広島県] - 朝日新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFB3aFVyajdlQzVKSFQ2NXEzOTJjM01WVFZMWkRzUENTRFlnc1ZDdGQ0ZUZaNlFBSXktZnVvSXlRMEN5QzE2TFZfZ0dnVTB5d1JOb1BIXzRVZ3ZhbGdyTHh5NWNIOTRyUXRWaXktZEdCOXZHNVRYWGV5X19TNXA3dFk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">足跡のにおいをたどり２０分で小学生を発見 広島を１０年守った警察犬カリフ、出動１０００回で退任（テレビ新広島） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5MMDZULW5sU19TZFNqTUxmRV90M3dEcE1lWGhWNzVkM3BxQW1EZ0hGOXBDSGloYjlTbjNEZ2JGYk1heXJ6cmRzb1g3MWxpSGpQeHNzVEkzU3d0dGlJTmx0VVhSNHRqUmMwYUw3alctczF1LW5aSUZwdFdqNklfLVk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">旧広島陸軍被服支廠の被爆瓦約1000枚、無償配布へ 希望者募る（毎日新聞） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603011?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">リニア開業時期 年内公表を断念</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602988?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">NVIDIA会長 フアン氏CEO復帰ない</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602983?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">NVIDIA前CEO 復帰なら「光栄」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602987?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">個人向け国債 税優遇見送りで調整</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602976?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">NHK 職員に「飲み会22時頃まで」</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602951?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「JINS」最大1829万件の情報流出</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602935?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">楽天証券 最大1125万口座分流出か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602918?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">物議の選挙ポスター AIと認める</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602871?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">MS大規模障害 幹部が原因を説明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602840?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">卵サンドつかむ客動画炎上 店説明</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603009?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">装備移転三原則「非核」の削除案</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603003?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">看護師の死 突きつける命の格差</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602984?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">転職組の教員免許を容易に 改革案</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602982?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日本版DBSに脆弱性 稼働延期へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602978?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">小渕優子氏更迭 自民総務会で反発</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 12:11</p>
