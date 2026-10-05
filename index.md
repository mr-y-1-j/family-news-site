# 🏡 Family Portal 10/05

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 69,132円 | USD: 157.75円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(115.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(300 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">3じ 50ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiekFVX3lxTE1EZGdWSGRYQy1kYlpYWXJHeUpmT0JNTnFHXzNjMXVsb1I2U2tEbWpGS3lUaWk1RUVlMm8tdldHdnYtQ1duS3RGNlFQdldVRHBtc3hOMGNsUVJaRmJXVk9UZmRmRlRQTXc2bG91SG04MHF6eFZQd1A3QmRB0gF_QVVfeXFMUFB3bFVPeVhqcGJUTUdEbHM5TU9hUDlCQmVWblljUWlUNHRhUnJmd0NrQmk1bzVFOWxFUGxsQ2M1bkEyUzQ4Nkc3R3lVbktGUGRwS2RFNDJfdjFSVDJmQUV3Sk5vdm5nMlBtVHc4b2hIVDRfbkRRUXRPeXUzVm1hdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島　４位確定　４点差ひっくり返す逆転勝利　代打・林が九回に決勝打→１４打席目での今季初安打　八回は佐々木が同点の２点タイムリー - topics.smt.docomo.ne.jp</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiekFVX3lxTE5XbFZCMFRVLXJteGdhOFZpTGFzQ1Zyd3NVQkhvNEM0bW9EMFhzYVloZWFIcEpGNmF5QzFvcURXN2NMVTBuVzJNVHNVcERPeDBRbmFjdHJVdDVyVUlGWUlZZ0M0dGJkNnhrMWkxMFFFU0tfb1ZLM1pENTNB0gF_QVVfeXFMTmVZVU8wRDlOdy0teEdpV0xyUGlNUFJTUTlDalF2RllLbWV5SlRqM2Q2dE9QVlBXVGcyWXY4QWdaMTBmQU9iUmtneDJtQkViZ3JPYkZvSDRvNnBtVXByeW1Bei1zY3RDTUpqRWkyNVBranloYWdweFQ1TGtuRHBpTQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・新井監督　林「気持ちで食らいついて打った」「みんな少しずつだけど、粘り強さが出てきていると思うので」【一問一答】 - topics.smt.docomo.ne.jp</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9Rbll3Tm5xdnBuWDNLOXV1WUNRUFRFdUJ1V3hORHNpdmgwUU0wY25GSC1sVXFMdmVHeTRTNUVscGxiQXN4X2I2Yk5CaC1sN3U5SnlHejZ1Y0ozNHdyd0hKV1lHYW9ZVlJuWUtkQw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ヤクルトが広島に粋なメッセージ 試合後にスコアボードで辰見鴻之介の代走盗塁記録を称賛 広島ファンの応援にも感謝 - デイリースポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijwFBVV95cUxOeE1JOE5fdy1lS19LV2t1OGItbGllakx3YnloUHQ2T0NlbW1RUXZoOEdHb1M5eVpWNE5TbHRFalhQSmZnVkxicmhfcm1EMHJmamZrTHFYZ2FHajBEVEJ3MXp5dXZzMm50Y1dCTXJydEtWSktsTHJfTzhmeGpLaExoWkt4b0h3ekNJWDI5ZHhUSQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【阪神】岩貞祐太、６日広島戦で引退登板 甲子園のマウンドに上がり、自らの花道飾る - 日刊スポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9ZVktrWW5mQ3ZCTHNnRFFiY0UzT1Y1OGtqeTZLNTdmZ0JuSExzTXNaZm9mOHVub2djWS1adUQ2T1ZmR2VSckRGOEVRbWtZZlUtQWJCQ3laQktqVy16YWhYQnNhM1J4VlBfcHR5MlhuRks2YmhxSWZsMWRXTC1LRTg?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">阪神・岩貞祐太「10・6」広島戦で登板 当初は引退セレモニー予定も、優勝決定で引退試合に急きょ変更（スポニチアネックス） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597415?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">食品消費税1%に賛否 減税効果は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597453?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米国産ジャガイモ解禁 前倒し浮上</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597572?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">8年で20倍 民泊規制強化と争奪戦</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597461?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サザン関口氏会社5.8億円申告漏れ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597529?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サザン関口氏会社 申告漏れを謝罪</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597542?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日経新聞がサイバー攻撃被害 発表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597451?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米政府のAI 都合の悪い質問を拒否</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597441?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">MacのOSを修正へ AIリスク対策</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597431?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">アプリで家事分担を可視化 市実験</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597360?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">e-Tax 他人の税情報が一時閲覧可</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597564?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">臨時国会召集へ 消費減税など焦点</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597567?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AI自動運航船 自衛隊に導入へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597566?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">個人情報提供 事前報告を義務化へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597568?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">DV被害者らの情報漏洩 5年で68件</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6597502?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">片山さつき財務相 事前運動の疑い</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 09:17</p>
