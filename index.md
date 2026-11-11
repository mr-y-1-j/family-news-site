# 🏡 Family Portal 11/11

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 60,877円 | USD: 158.91円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(192.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(150 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">6じ 25ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiS0FVX3lxTFBreTBUTXQwSVlPSmZVc3BlNmlUSXVmMW1FN0tIOVdvUGt3bFo2YlJpeEdRSjZUNWtCb2VXYktJYmpLQTNGR3UtSDFyOA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島で事業承継やM&A考えるフォーラム ドラゴンフライズの社長、事例発表 - 47NEWS</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiakFVX3lxTE1iLTZ4UGNZOFItYXJoRFpGel8tMnRreEkxdU1YLWZQemFING1oS2htNHVjRFRoZEF1SHJTM29Qc1h5M1hpdHVBdm84QUJWaWFXWk8ySjdkNjRuejhfSEx5bEVRQS1sVG1Ld1E?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島工業大学】大学・自治体・商業施設による産学官連携 「食」から考えるSDGsイベントを開催しました - PR TIMES</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9GejNmeUFwUm1PcUQ2VGtsWXpPRnRWVjBWV2w5ZWh6QzNsNUgzbVZYVzFaM1lGLXJ6VS1TQmhtcEpOR3gtX19iNXIwQ3BrR3VXbFY1VFlzUFMwcG9wNHRnbDRPQ01NTTM1VDNmLXpHM0ptWWh6SE1oMldXUENnY1E?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・中村奨成は３００万円減の２７００万円更改「金額に対して、言えることはないです」（デイリースポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMickFVX3lxTFBDNFphX0ozQkJwc1haUG12clI0MDM3NHRCXzdfSFRUaklXZEF1LTdQQWhURXBZVzVjQ3pqSER5QncxOTA1aVo4UFhRU2VMVzlFLW1TcTV1UGo3QTdQd0xWTnNVZ1hYcVQteFdfOEJiYmRTQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島の中村奨成は３００万円減の２７００万円で契約更改…佐藤啓介は倍増の１４００万円 - 読売新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijwFBVV95cUxPM2JIRl90dHhtekxyRzgxZnF1dmd3M3lxTFdOZXAtUjk3aHZDcUFjRzZPOVJSNTRCNW1rT3piOGN4QWptbnVVdUVBcXFpckpHeE1MVkd0YlhFaWsyamVha2I1ejkyc3Y3R01XanppTjNxVXQ4QjdmdmJteHZ6NmYtem5xZzRfMWhZSEM2UGlLOA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 佐藤啓介が1400万円でサイン 「想像を超える自分へ」 バックスクリーン弾量産宣言 - スポニチ Sponichi Annex</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602117?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">障害者雇用ビジネス 登録制を検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602099?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">タマホーム社員 保険金を不正請求</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602072?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SBGが7680億円の赤字 中間決算</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602124?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">トヨタ 軽トラックを米国で販売へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602095?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">もう終わりやで 明石ダコ深刻不漁</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602126?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">前澤友作氏なぜ敗訴 詐欺広告裁判</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602082?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">スマホ遠隔操作し詐欺疑い 逮捕</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602077?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日商簿記など 合否や得点が流出か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602104?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">証明書コンビニ交付で障害か 復旧</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602054?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ケンタ 一部メニュー画像にAI使用</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602125?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">国際情勢は歴史的変革期 政府方針</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602093?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日中首脳会談 実現への調整不調</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602083?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自民・小渕氏ら 税調副会長を辞任</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602107?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">小泉氏 首相総裁選出馬なら支える</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602067?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">原子力潜水艦 導入視野に検討へ</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:33</p>
