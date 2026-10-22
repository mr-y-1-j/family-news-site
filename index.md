# 🏡 Family Portal 10/22

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 64,681円 | USD: 158.17円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(135.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(180 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">4じ 30ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE53MHE5RjJhVmNZQjdoalN5MUFkenB2SjAyOGwtUkxXa0xrNG1ZQVR0YjQwbnM3WWZSMFVEb2h0d09Gdkk5VG00X0tKWEQzR2VWb0hHc24xUG8wUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【火事】広島市安佐南区で「家の中に火が」 消防車11台出動 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBoRFZwODk5WGVkc0N3YmVFcEgzSWxSVVJnUmYyU254cE11N29DeXJob2cwOVpWNjVSWThDajNuYlZGSmlIcVZqYUtORmdvRTNqUDVVdWg1Wnd3R1pvMlNUeWlQR1RIV1RyQ3p0bVNGZldlTzFMZzl3OV92RC1vdWc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【速報】広島市安佐南区で火事 「住宅から火が見える」 ２階建て住宅半焼 けが人はなし（テレビ新広島） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiV0FVX3lxTE5VR1pncVlESnVpaFRWY2pnRGViQTNOeEJjZjhCQm84N3RwM2c5ZVRiWkJRRkh4bnQ3RC0zajBpS05VQWE1eVFMRFhaaXhrcU9fWmNQMm5VQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「建物内から火が見える」広島・安佐南区で火事 約1時間後に鎮火 けが人なし - TBS NEWS DIG</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9tY2oyTXVUQ0JKVnluRF9LR1d6VTBkZ0tBeVoyZ3hDYVFPTnotSENlb2pXVVN6M0hWWjlXQVdwZG4xbTRBNm9aY0Z2OWVnRHBXNEtxcmN5NV8zS2U4aklIUG8xWjBFQjhTRUJGVldQXzZlOTlzd2VtNHRPSjlFeGs?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">頭突きで一発レッド！ 広島のアレーが退場処分、ビハインドで数的不利に（SOCCER DIGEST Web） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMi3gFBVV95cUxNMzM1aFdyT0s4SllkYWRBNENoQndnT2p1elFfbnMtM1ctQktiSng1ZGhBY0xySUdETk5RckRpR1RoSjJLdHJreTVXMFVjRV96WjU0dVMxR0MzX0tyYTBIQXhnOVJWd0RpdXdlRnc2Vm5mcnA4THBfUkUtMVFxZGNsM2xuOVVUbHR4N0tKYWlDaTNxeVFrempVY0pxdGl1WldraHdFOGlHTnVuMHZCNGQxV1lXLUZtV0VsTTc2bi0ydVJFb184SU85bGx5VXBsWHNVc29XWVZDY3dkenBRc3c?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【10月21日】V・ファーレン長崎vsサンフレッチェ広島のテレビ放送・ネット配信予定・視聴方法｜明治安田J1リーグ - DAZN</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599642?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">EVの補助金引き下げ 27年1月から</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599543?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SpaceXとテスラ 経営統合を検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599584?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米ネトフリ純利益44%増 7～9月期</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599514?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">フラット35 全国で不適正利用64件</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599546?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">北海道職員が「就活セクハラ」か</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599661?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">情報抜き取りに15秒 悪用指摘のAI</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599651?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PHPの脆弱性 米OpenAIのAIで発見</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599637?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PHPに重大欠陥 Webの7割で使用</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599646?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">コミックシーモア最大420万件流出</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599612?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大食い動画規制の動き 投稿者動揺</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599608?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">武部農相に選挙運動員買収疑惑</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599660?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">G7TV会議を首相欠席 与野党波紋</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599586?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">政権発足1年受け首相が意気込み</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599609?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">復興相の事務所数 公選法違反疑い</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599633?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自民 衆院定数の削減幅を31で調整</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 09:17</p>
