# 🏡 Family Portal 10/27

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 63,354円 | USD: 157.62円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(347.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(210 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">11じ 35ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5ISXpGVHUybUR2NGZmU1VXdG5QXzJOX2ZIV0gwWkt0QWtUR29PQzFzSDh2VEN1aV9tMnp6YmlXU1ItWjhDaGJfMVBiYkUzblRLLU1kc1BkNmdsaHNOampHNVlONDJXTzVCMjZ1RkgwSjhaSkNsSWJaYkdFVmI5NmM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】元ヤクルトGMの小川淳司氏を球団副本部長編成担当に 球団が発表（日刊スポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMie0FVX3lxTFBpUUtFanpmc1dYZWdQb2pndXFJemVIZWRqRVE2dDBHWHZ0SFRBRlItbjBWc0hEZGxYRXRXOHkxOWlzbjNZZFhGajM3Ti1adHh5WEZJdXctek1wbS1zTndlbDM4QzJFa1pRNU1DQjJKWXoyS3JRMnNNR1VXaw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】小川淳司氏を球団の編成部門に招聘 ヤクルト監督やGMを務める 新井貴浩監督5年目へ向けて動き - 日テレNEWS NNN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE05ZTlTbXhyNldmWlNRNGJoeFowMk1qVWRsSHNHQXdveWJFbi16RjNXa0N6QjYybzVxNG9pZHBqZkxURDIwVC1Td21VRUJRLWdCRUNCcGxmWGk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島、元ヤクルトGMの小川淳司氏を招聘 Bクラス低迷＆ゾンビたばこで揺れるチーム…外部招集は異例 - Full-Count</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE9zdlNMdGEtSThwcUNhcEEwZ21xX2NTcm9OU01sMlZwbG1HRDhZOUxuZXVtbldlM1BNNTF5a2NVNE4tai13MHhCZ1gwTUxtYTV1Tk13TW5ReHJ5UQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島市の松井市長、出馬「変更のつもりない」「上手に手術してもらった」脳腫瘍治療で1カ月ぶり登庁【記者会見の一問一答】 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBFVjhxdVlLeGk0akY1bGhNclpHVTBDT1VJRVJ5dmNhLUdZcDYzeThrT1hPWTRIWjVKdHVRdnlvaEVPQ2lrdnFDZGhDY29fNEtiV2JlNl85TF9aM0xyakdHQXF4SGtIemgtaS1Bakc5T3YydFNiQ3dIUVdYdjl4X2M?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島市・松井一実市長 来年春の市長選挙への立候補「変更するつもりはない」 「悪性の脳腫瘍」の治療で約1か月ぶりに登庁 - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600248?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米MS 6万人に退職パッケージ提示</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600240?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米Anthropic IPO申請書類を公開</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600265?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大手生保 国債の入れ替え加速</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600166?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">退職倒産が最多 中小企業どう対応</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600187?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">温泉「無断持ち帰り」 若旦那困惑</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600241?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMOに予告 正午に顧客情報公開</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600222?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMOに攻撃 当初は約80億円要求</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600246?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">iPhone Duo画面不具合 交換対応</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600262?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">新iPad mini発表 防水を初搭載</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600238?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">楽天トラベル 約260万件が流出か</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600231?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">福田康夫さん死去 親子2代で首相</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600189?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">福田元首相が死去 高市首相が談話</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600239?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">露拘束の記者 大使館員が領事面会</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600226?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">スパイ防止へ登録制度案 政府提示</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600219?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サイバー攻撃に緊急対策 首相方針</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 09:58</p>
