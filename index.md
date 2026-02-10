# 🏡 Family Portal 02/11

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 57,651円 | USD: 154.33円</span>
</div>


<div style="margin: 20px 0;">
  <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLKeSkfHhKSzLQqP7Rz5z25kMs726xU5p-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 10px;"></iframe>
</div>


AI編集長です！02月10日のニュースをお届けします！

### 今日の3大ニュース

*   広電の循環ルート、3月28日開通へ調整！紙屋町・八丁堀と比治山エリアが直結し、街の利便性がさらに向上しそうです。
*   バスケットボールB1の広島ドラゴンフライズが、女子Wリーグへの参入を発表しました。姫路のチームを買収し、広島を拠点に活動するとのこと。男女で応援できる日が楽しみですね！
*   トヨタ自動車の豊田章男会長が、アメリカの「自動車殿堂」入りを果たしました。自動車業界への長年の貢献が国際的に認められた形です。

### 豆知識

今日は「ふとんの日」だそうです。「ふ(2)とん(10)」の語呂合わせで、良質な睡眠の大切さを呼びかける日なんだとか。ぐっすり眠って、明日も元気に過ごしましょう！


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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(317.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(210 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">10じ 35ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE93TTR0Wm0zTERiQk5lakJYa3pNaWVkREloUDNZdEJSZ1EtT2wtbm0xV29QZk56SWhtNGxNNUJlZHA0V2ktRWt6UlpPa3dvNVVwNzhnR3lCdWF6Z9IBXEFVX3lxTE50cU5vMnFCcWJLMWtFVGNPTUlCNjExb3dCWVR5NlVsQ0JzZ3BXZDZ3TUxKYUhqZDBrd25wd19RVFdWRW1DM1JyTG9lU1BUS3R4V1lrSDNwd0tFZHBo?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広電の循環ルート3月28日開通で調整　紙屋町・八丁堀と比治山エリア直結 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE51dXpZZVM1LWNjY2J6OEZCQ0ZpampHeC1IY2tJNEN3MWRkSjFrRVlDTW4yaUozeDh0YkRLS05ZYmUyVE9TOVYxWnBjcmlzSF9EdVRFZW13RGFTZw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島市の川で「男性が浮いている」と110番 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFA1alpKb2lLX2FIY1J5Q2JUOS1xc1NzR0NqODNqdjRmT0Z3OHBZWEIzMElQQnA0TGc4dVlTeEs2U2dtYlNGVXhEZEFGMEY0ODB3bUVhWHEwQ1oxOTZTQVNoRXFiWm1XcXJjT0d0Y1lSTld0bzRjejdCU21xRmpCa2s?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">バスケB1広島ドラゴンフライズ、女子Wリーグに参入へ チーム買収、広島を拠点に（中国新聞デジタル） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBYY1BCVERIN0RjQUdva3ViUE1ybjdIaTR1UjdLNmVMd3dudTlKODlOSlFsaXB5Ykl0djBWalU5ZmFkaGVra3JuYzRrRXMtakhXU214NzZtQ2RCQdIBXEFVX3lxTE8zV04xZWJ5TXpqTzl6NHFuS3MybVZhcFBaM3FYNnFBT3dCdnI1VkVDRUo5TEdUX0VRMUtTaTllRjNLU2Q5NlZtYUxQVS0wX2hMN0NKRk43VWxHTkN0?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ドラフラ、白鷗大の佐古竜誠を獲得へ　広島・呉港高出身のポイントガード - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE01cUVONUNZbFdSWEZIc2YxREc0eW1lcndyV0ppU2V5WUM4Zlp3bVBkNkxXc3RDeGcwa2QyM3EtUDdjR1hpQ2ZmTnUtTVdFZlhITzBIbDV5M3hHYWFXTW94STFhMA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">Wリーグ所属「姫路イーグレッツ」の株式取得および フランチャイズ移転のお知らせ - 広島ドラゴンフライズ</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569425?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">シャープ亀山第2工場 売却不成立</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569460?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">トヨタ会長 米「自動車殿堂」入り</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569410?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">JR東社長おわび 相次ぐ輸送障害</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569437?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">資生堂が赤字406億円 米事業不発</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569419?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">円安直撃 バルミューダが赤字転落</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569446?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">JAL 2万8千人分の情報流出疑い</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569394?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AI要約でサイト「素通り」傾向は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569392?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SNSで首相人気 自民大勝の一因か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569331?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SNSで高市氏見た 遊説訪れた18歳</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569203?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">衆院選 Xで注目された発言を分析</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569459?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市内閣の支持率67% 読売調査</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569443?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">第2次高市内閣 現閣僚を再任方針</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569422?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自民圧勝 若年層の支持も原動力か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569435?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大勝の自民は交付金153億円 試算</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569430?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">意地悪やなぁにみる首相支持 解説</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:29</p>
