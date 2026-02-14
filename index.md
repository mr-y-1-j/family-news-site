# 🏡 Family Portal 02/15

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 56,942円 | USD: 152.82円</span>
</div>


<div style="margin: 20px 0;">
  <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLKeSkfHhKSzLQqP7Rz5z25kMs726xU5p-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 10px;"></iframe>
</div>


AI編集長です！02月14日のニュースをお届けします！

---

**今日の3大ニュース**

*   **広島県内23市町、国の「おこめ券」採用ゼロ**：国の物価高騰対策としての「おこめ券」ですが、広島県内の全23市町で導入が見送られました。各自治体は独自の食料支援や現金給付など、別の形で住民をサポートする方針です。ご自身の住む地域の支援策を確認しておくと良いでしょう。
*   **政府、子育て施策の地域差是正へ**：政府は、子育てに関する支援策が自治体によって異なる現状を改善するため、地域差の是正に乗り出す方針です。どの地域に住んでいても安心して子育てができる環境づくりが進むことが期待されます。
*   **武蔵小杉病院で約1万人分の情報流出**：武蔵小杉病院から約1万人分の個人情報が流出したことが判明しました。病院は身代金の要求に応じない姿勢を示しています。個人情報の取り扱いには引き続き注意が必要ですね。

---

**豆知識**

今日は2月14日、バレンタインデーですね！日本では女性から男性にチョコレートを贈るのが一般的ですが、世界では恋人同士や友人、家族間でプレゼントを贈り合ったり、男性が女性に花を贈ったりする国も多いそうですよ。素敵な一日をお過ごしください！


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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(7.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(90 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">12じ 15ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE9hbVQxRmNQYkhlZ2t6ZXZoTlNSZkprSnVxSnlSWm12WHRUdUI3VDhjdUtidU8yTGhQVnh6NEFrcFg0T3BDSXhNQ2VyVl9Ra3dGM0Vmak4yVWN0QdIBXEFVX3lxTE1iNmdFdDRfNjEyN3NpR0g3NldOVHgtd2hnNnBoUm95ZnZnc01aNnRWUW11NjFlSkI1X09qSFpLd2hGd240d1FKQk5xQi1qcXVYNlFkRTc3N0dkZFI1?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島県内23市町、国の「おこめ券」採用ゼロ　代わりの支援策は【一覧表あり】 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiiwFBVV95cUxPUWsxR2VaM1YzcWpIa3h5VGlUbFRqRzNDZnJNVWRRTUdsQWxKN1lNZEFyN3YwT2V2QlhOR3pXSWRuZkpsMGdhdW5rWFBoVU1FRWJOQ01BaGdIS09JeTFSX1lZY2xBRXlGN0hDVUZaZHhBclc4VUdKdUpiMFl5S0p2cXl5ai1fMUQwQkdr?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島駅南口周辺のペデストリアンデッキ(歩道橋)及び エールエールHIROSHIMA館内通路の利用開始について - city.hiroshima.lg.jp</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ESmhhUjAzNDJIMmk1VGI4QlBoeklGWUJFWFpvY3lOelFqam9saHpCUUVISGg0dEYwTVVYZTZOMWFORC1memc0SzNOSENGQkZQWlNJREpoaGEyd9IBXEFVX3lxTE5icWRKNDNLRm9OSjRwbWI0cEdSc284a0dyeXZ2d3RJWUJJcGt3bGpLVlNWaFJVUTlNUHd6ZktXNkJ0SlpXbGRYQXlaUWlvZlhuUlRESUx5V3VHNGhJ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広陵高野球部の暴力問題、元部員2人の審判不開始　広島家裁が決定 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiV0FVX3lxTE5qSmRhVnR3Sm1ZdXNBS01Wd3VuajhKdklrcXVoRHVneTRnZkVBLVJGRE9QMHlyenU3MV9ZcXF5eWNWNmYzYjdIT29vQm1QR0Z0Y0hOWVprcw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">OK！！広島“推し食”グランプリ受賞👑 夜叉うどん販売ブース出展のお知らせ - サンフレッチェ広島 オフィシャルサイト</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiXkFVX3lxTE01SWVJdUpodnNVQTRkUFdrZmxFNnVKSFJCRE5meTM3dkgtN05UWE1KaEZjNlA3YkxQOWQ1QVY0cE9BU0lVZmk4RlAwSVdkXzMybW5RWEFBVnFBSVZIMkE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【公式】広島vs岡山の試合結果・データ（明治安田Ｊ１百年構想リーグ：2026年2月14日）：Ｊリーグ公式サイト（J.LEAGUE.jp） - jleague.jp</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569951?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">男女賃金格差の改善鈍る 共同分析</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569889?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ゴルフ場閉鎖も従業員が営業続行</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569917?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">メガソーラー計画 各地深まる対立</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569876?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">茨城の廃虚モール 震災が引き金</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569892?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">なぜ コンビニにパウダースペース</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569954?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">候補者家族にまで 選挙デマ過激化</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569950?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">身代金150億円 病院「応じない」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569824?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">武蔵小杉病院 約1万人分情報流出</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569921?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">教員が外国人差別投稿 筑波大謝罪</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569918?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「#ママ戦争止めてくるわ」反響</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569957?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">2月下旬 寒暖差激しくなる可能性</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569925?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相官邸 経産官僚の重用が際立つ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569891?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市氏に指摘「女性ウオッシュ」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569904?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中道 幹事長は立憲系の起用が軸</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569940?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">政府 子育て施策の地域差是正へ</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:12</p>
