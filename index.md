# 🏡 Family Portal 11/02

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 雨</span>
  <span>📈 日経: 63,133円 | USD: 157.79円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(145.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(300 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">4じ 50ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5RMXhvLXBOYlJJTG56akllckJEcURKOUpXNms0TnJycGg0UHRsVUJpT0lhTTc2VVFvSFpFbDVkOVVzNlRDU3IzczMwVHRlSHlTbkpfcXRsVHZmdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【火事】広島県世羅町で民家の倉庫全焼、母屋も半焼 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiakFVX3lxTE5HaXR1Z2NaY3VUSEJtTU9FNkdOamQ3cVF4blJzakhiUVp4RGEzMkdYeGRIdjkxeE5OQlFJdGl2R1VMRUhoNWlVZVhlWmpBekhINGFqZU5vZmR0U0ZZUnZYTGRqUHNZRHlNb1E?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">一旗プロデュース「広島城 宵めぐり 2026」を12月18日から2027年1月11日まで広島市で開催。史上初・広島城天守のプロジェクションマッピングと広島城を光で彩る期間限定ナイトタイムイベント。 - PR TIMES</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9EU2VDaUxyZkJMZXNFRm8xR3ozMkdISGhkQUpLb3dIWHlSc2E2YWZFXzZOQUlvdFpTU3FJR3hfWjlPN1pTUG8tb1FkSkFIakdRM29HZ1NDVW1FNlY0TTI0d0p5bmN6MWo1dExUMHJGRVRMMzBTQWl5NExzbThWSkk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【速報】都大路の切符は西条農業 女子とのアベック優勝 世羅は23連覇逃す 各中継所通過順位など結果速報 【広島県高校駅伝大会（男子）】（RCC中国放送） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5qZjhBaG1EWEM2N2xSR2RqbTNTbVNBRUFkUWdZaEVXenNxZlJob3Ric0RKdUJpY1FQakJqNjFERlluU2VkaDBuR2RmS3dIc3U5UmVEYkMyd0Y1UQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">全国高校駅伝広島県予選、女子は西条農が大会新で22年ぶり頂点 2位は銀河学院 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE1MTnpjb2NJd0hONzc1YXBfcXkyamVfR3E4QWdJOV9GSWxmYjNoSW5VS1ZMUTk5cHBjZVVZbDBjYjRfUjhpeUtZV2daVWhvOTkzalJIY2FLX21KVlNQWmZ4MVVWcDdWeElT?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">西条農が優勝 都大路出場を決める 高校駅伝・広島男子 - 毎日新聞</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601015?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">金型の無償保管 公取委勧告が急増</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600900?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">出国時に返金 新免税制度が開始</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601025?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">内定者2年間入社しなくてOK 狙い</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600993?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">みんなで大家さん 悔やむ出資者も</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600996?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">望月衣塑子記者の対談本 回収へ</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601028?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">情報漏洩で見舞金 おわびの正解は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600991?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO攻撃 北朝鮮系のハッカーか</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600977?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO攻撃者は何者か 識者の指摘</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600980?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO子会社 9年外部閲覧可の状態</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600998?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">闇サイトで高まる 日本への関心</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601017?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">内閣の支持率64.9%に上昇 JNN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601011?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">防災庁発足 防災・災害時の司令塔</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601002?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">農相政治団体 寄付3000万円不記載</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601019?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">私立高の学校納付金2倍 NGO調査</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600965?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市政権「脱リフレ」するか注目</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:05</p>
