# 🏡 Family Portal 11/22

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 56,437円 | USD: 159.71円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(250.00000000000003 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(120 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">8じ 20ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9rbUVQV1o3TEdoMzJoc25vRnlyVXB2MWdGdnBDeGRCRXIzc2ZpLU42dVVxYU1kUUZTZTJqS0tFdFIyLXYtQU9heTlMWllRUnBOQTg0VFNUaDhJVk5jSEdTMTVXcDhkMnVPSVhwM1NGdTdvZWlyQU1ZOEdzWE82TEk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島で初雪観測 今季一番の寒さ - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1NWTNORy1MR1F0SmJqbUNscV9uNlMtb3JzMWJvZmZJWmNpVGU0S0NVcjRoYjlFRVZMdkhkUmhxQV9aS1lqUU9WbFJnV2VBaVlLbFQ1TG5GVF9fdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島で“初雪” 21日午前4時半ごろ「みぞれ」観測 平年より17日 去年より12日早い「初雪」 広島気象台 - TBS NEWS DIG</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxPaXptcmRFWVF1ZFBRMHk1S1ZPVTBKZWdYdWlCRlNsWlI4b0FwZnllWTR6a3cxNTVHc05TLXIxbzFtVURNdTVEVnBPeWQxRDRXbzNhUlh4LWk3U3ZKdGNwU3VIMU5nS1M0Z3lKazlIeWtnZkw1UFNiYVdrLXk5dS1oT3NkTWpmck0?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島で初雪観測 山陽道で車の立ち往生想定した訓練（2026年11月20日掲載）｜広テレ！NEWS NNN - 日テレNEWS NNN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBfVkwyOUtqZTJlak02X0ZkY3otX1FJY191VjJpV3RWejE4YWRUYkpZSjJZbFJhaHpNMEN5aFFvbjZGYWMtVGdBLXhvX0l3UXcxTW52TV9PWFhMQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ガスも電気もリフォームも「ガスライフ展」はじまる 県立広島産業会館 | RCC NEWS | 広島ニュース | RCC中国放送 - TBS NEWS DIG</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1sNGx1aERlVk5rSEFqdlVvczlUZ0s2Q1JBSDQ1ZjVLckotcEp3cFV2cHlHWnVqV2owblFXSVZDVnZsVGszLXFZSm5mUTByaHdVdDFhQWo3ZEQwUXlueFR4MHVVTlY3V3lJTW9GRElYRms3LV9NaG5TT1ltenZ2dVk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ガスも電気もリフォームも「ガスライフ展」はじまる 県立広島産業会館（RCC中国放送） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603509?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">地方銀行再編 各地でくすぶる火種</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603504?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">氷河期世代の正社員率改善も 格差</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603415?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">預金1億円超個人口座 00年比3.6倍</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603408?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">店の「食べ放題」巡り物議 法解説</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603512?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">メンズメイク 若者を悩ます世代差</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603483?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">推薦入試 不合格者に1秒間誤通知</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603448?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">六花亭 クレカ不正利用を1件確認</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603398?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AIでリーマン予想証明か 精査続く</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603360?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「リーマン予想」生成AIが証明か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603349?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ZOZOTOWN 1518万人の情報漏洩</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603498?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">税収格差是正 都と地方せめぎ合い</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603470?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">防衛費巡る財務省案 議論が過熱</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603489?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">関文科相の辞任論 与党内で拡大</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603461?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">参政・神谷宗幣氏 演説に変化</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603485?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">LED信号機に弱点 発熱少なく着雪</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:44</p>
