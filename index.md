# 🏡 Family Portal 10/29

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 64,683円 | USD: 157.87円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(210.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(0 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">7じ 0ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMic0FVX3lxTFB1czFoaFV0TkFfYVpkY2ExZThTc2MzcDkxZFhYTlhwRWlCak9MTENVdWgyZ1FDN2dNSXd4R1RJNG9IXzU4aGYzTTdCNzEzQzJ6ZVNpekZxN25lS0VYRktfcU1MaUVBVTJTYS0yRWVSMDRpRVE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 契約更改がスタート ４年目右腕・益田が１００万増１１００万円で更改「そろそろ（期待に）応えられるように」 - デイリースポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxOaDNLYVVmZlh3VlMwZU5USmhHOTJwc1cwNzhOeFRxZ0RkczBzOFhPM0ZkaEhFdzgyTjZOVHdwclhKTGZCMWFOdkJyd0l1WEQ0c2lVWXlJdlp2N2RKUEs5bTI5MjNaY3FsT3pLRFdoNk80Zm9adnBVMjQxY1NHLUZFQm5hck9mRnM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">里親の虐待問題 再発防止策を検証部会が提言 広島（2026年10月28日掲載）｜広テレ！NEWS NNN - 日テレNEWS NNN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1PSVBYX3VJeS0xX3htQm05clZsVk9RQjI4RlNqNllFZTRCcXZyU2JNV2lLVS1iMXdfSW9GS2NNM0xnWVJ3dG1idi03YnUzZWN4b1hIN0pxUkk3cExRVkFyNHNWcy1oRjd0SndLQVp1dVJuXzBZZkRWVzF1SXMtQmM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・森下、ロッテ・小島、オリックス・中川らが今季国内FA権を取得 10月29日にFA申請がスタート（ベースボールキング） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1HYnI0T19rcXAwdHF4aVlEV0VqV0c0SW5NNGZ4WFFYMmdQbjRzNTBJcU9LcjN6d1VjV3J4ZUZoWnBZSUo5d19zZjNwMmFDNjd4S011Rm5Bb2NXZVZlZ21z?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">プロ野球 きょうからFA宣言期間 広島3主力選手の去就に注目 - NHKニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5ORXFqNTR6NEpLMTN0RExTYm5WbVdVYVA2MDBURDE0bG1kREtFenIyYnc1TUh4LUVGbmd5eW13SVhMT3hDQ2VvVlgxUHpTdC05ZnZBbS1ON3JWX2doMVNvd2tnRWh3eXNNazA3M0ktZnFEU1U0T3REQWx3ZWNIRzQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">今オフのFA戦線が本格化！広島の主力トリオや筒香嘉智、髙橋光成らの動向に注目【主なFA有資格選手】（高校野球ドットコム） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600510?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米FRBが政策金利を据え置き</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600452?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">プルデンシャル 新たな不正事案</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600474?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「千鳥饅頭」千鳥屋本家が破産へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600504?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">本や雑誌発売日 大阪も1日遅れに</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600444?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">キッチンタイマーを回収 TDR運営</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600494?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO脅迫サイト 国が遮断を要請</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600483?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO懸賞金 6hで113件の情報提供</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600424?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMOへの「劇場型」攻撃 狙いは</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600364?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO攻撃 被害者は「恐怖しか」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600375?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サイバー攻撃 サイト経由型が急増</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600518?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">燃料油補助 予算累計10兆円超に</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600506?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">教員「特別免許」の基準明確化へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600505?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">多くで今季一冷え込み 東京10℃台</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600480?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中道代表 政党交付金の使途を回答</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600466?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">武部農相 衆院選の人件費巡り疑惑</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:21</p>
