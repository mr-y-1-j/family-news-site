# 🏡 Family Portal 06/25

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 雨</span>
  <span>📈 日経: 69,175円 | USD: 161.77円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(325.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(300 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">10じ 50ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5YeUZvVGhlc2w2WGY5QmxKS2Qtd3liTXlLTDJoVzJhTnlrOXBkWlhhYm9FZHFSOVZvY1VvTllaY00wUVFvdV95c2RDako4dEdkSXFHYjhIMWlsZw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島や山口のJR6区間、6月25日に終日運休 大雨の影響 高速道路も要注意 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTFBidTBLUHRXRks3cDJIenVibEQxM3BZbjRpT29ZT3hpZjFBNHVXOUtrbEFERmR3T1RwNnRmUXV5RUpsZ0JDei1adlVicmVxZDdmbHFzX25jOWw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 ２５日昼前にかけて大雨 ＪＲ呉線などで運転取りやめ - NHKニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5hUVdjLTV4U0taNExfNndlV2FzX1A4YV9pUGh4MFloTTZlak15amJjcmRPTnNEMXFtMkZfUGRvSXRkX2cyaHVyUmNqRUtHS1NQM1R6MER4Smc5V0dCRG0zSkRHb0daNE1wejJiVzFrcVpneHFUZnp5MkhDN05tYjA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">倒産寸前→年商132億円の大逆転…広島の農園2代目が反対を押し切り作った"当時誰も知らなかった野菜"の名前 - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTFBRTnlGbWhmVlRwbG80X2s1OUhHcnZYUjlBMzlITTZ6UTRvdnhELU96MUdzRXk5TkxjamVTUlVlV2dlVEExTTZuRTA4dUlUTHVSc2dBRGR2S0tUVVNLYXFwUHNLODY?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【レベル３大雨警報】広島県・呉市、竹原市に発表 06:25時点 - TBS NEWS DIG</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBONVNleHJ1d3ZnbkRubzJybGh6WC1pTy1pSHJpdDBaaU15ME1YQk5rdk1WZ1U5WUVzSEhnVTVlN2NOeHloSTlyU09nelRzcHpUY01Lc0ZOa0FFUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【独自】広島電鉄の運転士を書類送検、県警 路面電車と衝突のスイス人男性が死亡 - 中国新聞デジタル</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585551?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">青森県で震度6強 鉄道の運行情報</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585526?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">クールジャパン機構 統廃合検討へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585524?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日産・永井氏 再任賛成48%で否決</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585537?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">キオクシアHD会長 報酬44億円に</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585464?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">任天堂の株価低迷 業界が暗い時代</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585459?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AIが共著者の論文専門誌 創刊へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585456?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AIの予約電話鳴り止まず 店主困惑</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585448?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米「先端AIを国家管理」G7に提案</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585434?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">楽天 スマホ「衛星通信網」構築へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585422?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中国 スパコンランキングで米抜く</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585549?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">青森県で震度6強 津波の心配なし</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585550?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">青森県で震度6強 最新情報</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6577806?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">安全確保を 地震発生時のNG行動</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585546?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">九州北部 災害級の大雨の恐れ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6585536?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">皇室典範改正 正副議長が要綱了承</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:57</p>
