# 🏡 Family Portal 04/17

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 59,518円 | USD: 159.06円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(30.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(0 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">1じ 0ふん</p>
      </details>
    </div>
    </div>
  <div>
            <div style="background-color: #fdfefe; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-top: 20px;">
                <h3 style="margin-top:0; color: #555;">🖼️ 今日の名画ギャラリー</h3>
                
                <div class="mySlides" style="display:block; text-align: center;">
                    <img src="https://www.artic.edu/iiif/2/ef96e79b-f481-8114-0804-4bd39c101983/full/600,/0/default.jpg" style="width:100%; max-height:400px; object-fit: contain; border-radius: 5px;">
                    <p style="font-size: 0.9em; margin: 5px 0;"><b>Early Morning, Tarpon Springs</b><br><span style="color:#666; font-size:0.8em;">George Inness (American, 1825–1894)</span></p>
                </div>
                
                <div class="mySlides" style="display:none; text-align: center;">
                    <img src="https://www.artic.edu/iiif/2/815fb024-96bb-6f38-e6fc-d398d2103c65/full/600,/0/default.jpg" style="width:100%; max-height:400px; object-fit: contain; border-radius: 5px;">
                    <p style="font-size: 0.9em; margin: 5px 0;"><b>Sunlight</b><br><span style="color:#666; font-size:0.8em;">Richard E. Miller (American, 1875–1943)</span></p>
                </div>
                
                <div class="mySlides" style="display:none; text-align: center;">
                    <img src="https://www.artic.edu/iiif/2/e72305c9-1a1c-8a36-7450-582619366338/full/600,/0/default.jpg" style="width:100%; max-height:400px; object-fit: contain; border-radius: 5px;">
                    <p style="font-size: 0.9em; margin: 5px 0;"><b>Flower Girl in Holland</b><br><span style="color:#666; font-size:0.8em;">George Hitchcock
American, 1850–1913</span></p>
                </div>
                
                <div class="mySlides" style="display:none; text-align: center;">
                    <img src="https://www.artic.edu/iiif/2/2e796bd8-4e0b-f55a-7c69-75a70a3e97d7/full/600,/0/default.jpg" style="width:100%; max-height:400px; object-fit: contain; border-radius: 5px;">
                    <p style="font-size: 0.9em; margin: 5px 0;"><b>Afterglow</b><br><span style="color:#666; font-size:0.8em;">Jonas Lie (American, 1880–1940)</span></p>
                </div>
                
                <div class="mySlides" style="display:none; text-align: center;">
                    <img src="https://www.artic.edu/iiif/2/9604cbbd-722b-8de3-e7cc-4a80be648d79/full/600,/0/default.jpg" style="width:100%; max-height:400px; object-fit: contain; border-radius: 5px;">
                    <p style="font-size: 0.9em; margin: 5px 0;"><b>Lady in Green and Gray</b><br><span style="color:#666; font-size:0.8em;">Thomas Wilmer Dewing (American, 1851–1938)</span></p>
                </div>
                
                <script>
                var slideIndex = 0;
                carousel();
                function carousel() {
                    var i;
                    var x = document.getElementsByClassName("mySlides");
                    for (i = 0; i < x.length; i++) {
                        x[i].style.display = "none";  
                    }
                    slideIndex++;
                    if (slideIndex > x.length) {slideIndex = 1}    
                    x[slideIndex-1].style.display = "block";  
                    setTimeout(carousel, 5000); // 5秒ごとに切り替え
                }
                </script>
                <p style="text-align: right; font-size: 0.7em; color: #aaa;">Powered by Art Institute of Chicago</p>
            </div>
            </div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBfWENLWV9IOTNWd09TNWRPR3NxTzgzSTVrX2tFVFRuTVlxR25mZTlyazBBN1FNZjcwaXBJa0YwM1A5c3BlTEswZldoZHM0dVZFcXBoSFFxUGo5dw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島の味「むさし」若鶏むすび1250円に 広島駅弁当も値上げ、コスト上昇で「ギリギリ」 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBpVGR4YWU3dHd5QXRqQWRMLXk1bl9ZNWlQRk5ST3JFR2M3cUltajVhUHBadkt1cXBHdW9NVzZQamM4eU00SnRXVGRkdGlVWUc5cTliaXBoUTRrUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島市内、18日も混雑か カープ、サンフレ、B’z…イベント再び集中 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9FUHljVDRsWXRrTmQzVk80UG1vZmRHS2tKVHgwdWFFazJUYjkwdTVhZ0t1MjVDSHVCY1FWMXgybGF6Q0YwUGlLSUVWSXVzd2dNNUFfOENqVXR0V3VtbkFLR2wzdy1kUmRiWDJaM1hsdWFramlteUF2U2swSVU1cDg?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">『旅サラダ』畑芽育、初めての広島旅 人生初のレアお守りづくり【コメントあり】（オリコン） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBHckNxT1pRanVWQjJERnVlYk16M2tqWldUTTI4dEMtR3hPRE5fLS1rZnF4b1Z0U204VnQyaDN0WFFIN2trUEdVUDBNeEtrNlVTcjhjdHpaZEFOZFBQc2RnbWoxdWpEbHA2d2lKaTJDWExQNUctd0p1ZnBjSU9hSmM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【東広島市・西条】香りと美食・美酒、よくばり女子2人のサステナビリティぶらり旅（トラベル Watch） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1kZXdrYnpPZkdVTHNocDFJRkh1WXJ4Y2p5TGZfaG1tSElhaUtNODN2MUZHRFFFQ0w2RGJDZmtkdU9pSkZseGFFb2tXcFFrTUhkVnBZMXBYSGpiQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【事件】広島市安佐南区で「オレンジ色の液体を顔にかけられた」と通報 3人が病院に搬送 - 中国新聞デジタル</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576511?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">時間外労働巡る自民提言 妥当性は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576521?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">滋賀銀行と池田泉州HDが提携へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576500?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">がん判明 職場対応に不安募り退職</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576505?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サンリオ役員1人が報酬不正受給か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576548?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日本の管理職は罰ゲーム? 背景</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576501?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">人型ロボット展 中国の出品相次ぐ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576452?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AIキャラ「ポケとも」ヒットの訳</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576391?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">災害時の「デマ拡散」どう備える</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576319?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">顔隠すポーズ 女子高校生が好む訳</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576285?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">JASRAC投稿 動画で楽曲利用巡り</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576525?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相 医療用手袋の備蓄放出を表明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576527?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">内閣支持59.1%に微減 時事調査</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576493?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">柏崎刈羽6号機 営業運転に移行</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576486?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">今国会で皇室典範改正を 麻生氏</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6576439?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日EU 防衛産業協力で共同声明へ</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:29</p>
