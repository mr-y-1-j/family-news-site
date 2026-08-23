# 🏡 Family Portal 08/24

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 66,016円 | USD: 158.88円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(295.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(300 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">9じ 50ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMioAFBVV95cUxPME9KbDd0VWR3S181bC1OejNTcV9ndFF1cVk1bzc4TklrTzVoY01CYkNpb2daMWo5YnpfanJPdXZoYkZxUDdJMmE5d28tR0RGVG9rWFZacG9SX2xucTcyTTRyTE5MVXRQNEstNGF0WHpvY1ItUVZwOTFXbjZkdnpSaDBaN1BhWmx3Y0pTWEtva2dGTHFyelhCUE1SMEc5M3FH0gGTAUFVX3lxTFBoelVqa2s0bVFXb1BQVnlhZXg1TkdOVXJBb193QUViR3VlWkJxMjNIbDdOOE13SUJxSXRkdG45aU14MFozZmhsLVk4anRPVm8wRTY4aVFjbnVfOTBxeTlUWHFQQ3B2TEE5QkZnNVlseHR2Wk5zZk5QQUoweHpxaGJ3NHRFR25KVjV2RGwwN2JJb3Btdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・遠藤淳志　安定感！安心感！9試合連続で無失点　夢の球宴初出場が復調の転機に - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5lNzFfRl9JVm45dmNPRXd2RFJCNW5JeU1KbEtOdWYzZXFTWWNONzRucEE0Zk42TlRJbjFyOWFFWThtLUxLMUs4RUNORzJPU0NQZUg4ZHZPMG40LWhYZlkxV3Z0Z0Rwb1NiU1d0NXdRR2tMd29BbHVrZXZZQ21LTFk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】遠藤淳志が４勝目マーク ８月は無失点で月間３勝 球宴で出会った阪神高橋遥人のおかげ（日刊スポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijwFBVV95cUxOWjBzOFJranVuRFRYS0xxYWJYSGgyQnNZY3ppbmRvTHQ0ZUd4d0lkZTF4Y0pMRmhoOUREUVozSElJejlfa05YQlZ6QUppWmVLaG9XNzJKQ3FBT2dZb3JwNU1rQnZjazcwamdyMTBURTVZTEllVFZZbG55RF9FX1dua2Z2SWZHYkRjazRBR1VhZw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">＜巨・広（17）＞力投する広島3番手・遠藤 （撮影・田中 和也） - スポニチ Sponichi Annex</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1fOGp0aC1JNENOV2pHcTlETFh3bmN1S2l6eEIzSm5sZ0xiUDluSEtnOXRtUk1JUUF1bFYxSi1xZTlWSzZOXy1kams2RnVGZ0NKSW5wWHloS1VWZw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">最低賃金 広島・山口・岡山県で1100円超え 中国地方５県の引き上げ額、過去2番目の水準 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1sVjVjRzEtNWpaZW1ka0lEcFZ4OW1JTWxScWZPVzNLSXA2eHA2Zkd2OFJ1YnJabEZCMHl6UjFqd2Z1WU1zNDZhdjJ3ZmhJSlVGbUt5NXVwbUp2Zw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">コイン通りから左折の新レーン設置へ 広島市佐伯区の中央陸橋南詰交差点、渋滞緩和へ - 中国新聞デジタル</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592734?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">2000円台の新米 昨年産と価格逆転</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592731?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">発火相次ぐ「モバ充」規制強化へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592777?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">就活で障害伝えず76% 不利益懸念</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592793?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ソニー 中国「TCL」と手を組む訳</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592772?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">年金だけ苦しい 炎天下働くシニア</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592770?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">スマホ乗っ取られ詐欺SMSのbot化</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592760?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中国でロボ運動会 続々と人類超え</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592727?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">人型ロボ100mボルト超え 直後炎上</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592700?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">架空の党員をAIで作成 立憲苦言</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592695?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市氏 なぜ国会ではなくXで反論</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592823?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">消費減税巡り財政に不安71% 共同</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592818?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">原油輸送確保 首脳外交求める声も</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592773?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">関東で震度5弱 けが人40人超に</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592802?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市内閣の支持率横ばい41% 毎日</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592736?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">沖縄知事選 県政奪還へ自民総力戦</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:09</p>
