# 🏡 Family Portal 02/08

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 54,254円 | USD: 156.78円</span>
</div>


<div style="margin: 20px 0;">
  <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLKeSkfHhKSzLQqP7Rz5z25kMs726xU5p-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 10px;"></iframe>
</div>


AI編集長です！02月07日のニュースをお届けします。

**今日の3大ニュース**
*   **広島の平和の象徴、原爆資料館の入館者数が3年連続で最多記録を更新しました。** 多くの人々が平和への思いを新たにしています。
*   **東京都心で3cmの積雪が観測され、交通機関への影響や路面凍結に警戒が呼びかけられています。** 各地で冬の厳しさが続いています。
*   **衆議院選挙の投開票を明日に控え、各党党首が最後の訴えを行いました。** 明日の結果が今後の日本の方向性を左右しそうです。

**豆知識**
今日は「**新雪の日**」。北海道旭川市で始まった「新雪まつり」に由来しています。東京都心の積雪も、明日には「新雪」に変わっているかもしれませんね。足元には気をつけてお過ごしください！


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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(45.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(180 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">1じ 30ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1hOXI2ZHhFT1phUDhzclQtdFItbXRTWGhSd3lMSF91WG9Ha2ZKME05YThBUDZ6OHJteG4xTXcyRjgyaHd2bGpqeWY1ZnRGUDdfWEJRajhoNmozQdIBXEFVX3lxTE5hMkR0T0VKV1dYVnNxUnJaeHpFdTVKMmM1WUg3YWppeFpiZUV6eTZ4VWNvYzRzZGNwM2pMR2ppVEpkYkoyOTBmUFRJRXZfWDBhZ1YxVTlGRVZqdkxp?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">産廃業者の許可取り消し　広島県 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE8zdTlHeVBpYm5OdjBYU21qbnVqWmp5d05DRkc2R2hPdXFCaUJNSS1XRzBNNWlpdzNyT1ZRTEFseDlhUGk3NDhiNlhHTDJiNExxOGl5allsdlhObTlGd1FMV0hhLU5kMlFF?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">原爆資料館入館 3年連続で最多 広島 ／広島 - 毎日新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE4yRHdoS21NdGZmWTZuRmNvWHpCeHJEYXg4Y21OWUM4OFR3a3R5YTBPTGpmeHRNSnE0UnFJb0NGVHRNamdKcHFJREtLaXVlMXR6NTR4M3YwR2NKQjZ6TFZaclNQLTBicVJPb2owNzA0S2FHWWJwNUJrYzE0bVo2VTQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">キッカケは師匠からの「破門」…「ゾンビたばこ」で逮捕の羽月隆太郎容疑者が「広島で孤立していた」（FRIDAY） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE1wcThZNlNZNFMxOEtOVi1QckFfYVFQbUFRUWR4bkI2VE9MNlBCUy1lYi1xZndjZVZ0ZlVLZ2MyZVBvNXBmb0RrR2hYbE9WaEg4Q0lUXy1qTUZsaExTQlZ3eEE0cw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">カープ羽月隆太郎容疑者、使用認める ゾンビたばこ、逮捕時は否認―広島県警 - 時事ドットコム</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1sTEEyTFBXQ2dPZlJWR0xlei1EVjlPUVZnc2ZPWUh4V1ZVV29WOWtXZ0x5YUdvRlZMTWdSblpReE5ObC1fM2o3TTBzOFIyNFlPR29jSGZnaG9qRWI0dzJFMloyY3U1TUNqbV9CRlM0UUppVEU1ejNSbG5yOGxrLXM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・鈴木清明球団本部長「報道で知った」羽月隆太郎容疑者が薬物使用を認める供述（スポニチアネックス） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569032?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">対米投融資 第1弾は3案件で調整</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569045?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">五輪ウエア 有名ブランドぞろいに</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569036?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ニデックTOB巡り 新たに男を逮捕</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569037?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">20年越し念願 東横INNが高知上陸</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569026?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">テーマパーク 価格変動チケ広がる</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569064?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">独の声優ら ネトフリ吹き替え拒否</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569025?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">外国人巡るデマ急拡散 衆院解散後</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569005?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ドワンゴ広告ゲーが人気 計3億DL</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6568942?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">海外で導入 スマホ規制の効果は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6568926?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Apple 直営店でiPhone17販売中止</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569073?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">東京都心で積雪3cm 交通障害警戒</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6568996?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">道路に雪捨ては違法? 警察に聞く</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569069?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">各党党首が最後の訴え 8日投開票</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569056?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大雪 接戦区で当落左右する可能性</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569014?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自民が単独過半数上回る勢い JNN</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:14</p>
