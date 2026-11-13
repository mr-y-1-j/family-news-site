# 🏡 Family Portal 11/13

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 61,868円 | USD: 159.88円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(340.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(120 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">11じ 20ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMifkFVX3lxTE5yeVJKZGtPbS02bHdoZjNhUTJCOC1ZRWc0bk55aG9odGZ2UmxtbzRQWWZ6WENSRXZVdWpRV3R4dlJZaTBpVGVZcUJhRm13NkRIUmU5c1pGOFhmcFh5b2ZKempzZE94eS1RbUtDZXJpcjhIOUVxaHZndXZtSTFudw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ハートプラザ - NHK</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5HMVdhRl8wVXgwVGUxZ2d0cDYxb05rWDBPT3FGSkxrLUg3c2M4d0psXzd0QmJES2owMUNFOXdrUVdQSFhreDVRYzRjYjcweTFLcjVpUmM5aTFEQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">配当金で家計を助ける 富国生命広島支社（広島市中区）の小塩耕造支社長 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiakFVX3lxTE1Ga0gtcW5TakhHZmgzRk1XbDJRcERXR3NJdDVKZURUd1QySGJ3WnVIWG1XaklvUkhKZGJldDd1YWZFSHFRNjVUd1ktYUQ3UFRCamFTUXRZUGdzeDZReTdRb184N0NPUjNfZnc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">開館200日前！広島城三の丸歴史館 シンボルマークおよびロゴ決定！ - PR TIMES</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBPU0F5d0JlXzdSRGpYbjlUZ3J6Z2NxVk1pUEhKRExmVzUtNVFpUGRnSlZSa2l2QTAzN3FONEt0S011QlJpaFZHdzhBd3MtWHZxZTAyQ1JGWHlDVXBlVy1aY1hIVWdzSUdsQ2dTSGJ5NklSclFoNjBJVzY2S1FtTXc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【独自】長男（30代）を放火の疑いで逮捕 3人の遺体発見の住宅火災 家族3人と連絡とれず・広島県福山市（広島テレビ ニュース） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5yeEVNMnlmZ3hhNTFiM2pBR1JTZ3lrSEdkeFhVd3I3TU92UG1ieXdBcUpNT3k4cTRKRVNlbHV5dV9tajdOOEg4blVXaFo0N1RhdlBZcFhrM2ZlVDd4Sk94a0Nmd1dtQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島の３人死亡火災、住人の長男を逮捕…何らかの方法で火放ち自宅を全焼させた疑い - 読売新聞</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602361?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">エヌビディアCEO辞任 動揺広がる</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602353?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">エヌビディアのフアンCEOが辞任</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602392?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">メルセデス 独工場の一部閉鎖検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602380?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ワタミがMBO検討 きょう付議へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602348?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">タマホーム 5年以上前から不正か</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602378?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">恋活婚活「リアル回帰」の訳 解説</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602382?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Microsoft障害 全面復旧は未定</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602362?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「Microsoft 365」で大規模障害</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602346?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">選挙ポスターAI作成? 戸惑いの声</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602292?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Appleサポートコミュ 20日閉鎖へ</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602385?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">参議院議員の山崎正昭氏が死去</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602377?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">思いやり予算 5年3兆円超を米要求</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602369?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相 防衛費巡る「大幅増税」慎重</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602290?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ポスト高市の首相再選支持 相次ぐ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602349?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">石破氏 採決で退席の小渕氏を評価</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 11:13</p>
