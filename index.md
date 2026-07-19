# 🏡 Family Portal 07/20

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 64,141円 | USD: 162.50円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(32.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(30 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">1じ 5ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5pZm4zRkVBejY2U01leDczY3ZVN0tzN1VlWHJVVF9uTHpPbFgySEp0UElBYy1XUHp0MlQ5ZTB0LXNyaGsxdDlKWlJ0c2pQNER6TDZEMWhtWjhsZV9EUVBhdXlYemE3ZF9IajhtZE96dE8xSWpDTnpBaHNRV2FZQ0k?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島－阪神で一触即発、警告試合に 大山に死球、本塁付近で両軍ナインが集合 １７日に阪神の前川が死球で右肩甲骨を骨折 １８日は胸元付近のボールに佐藤輝が怒り 直後には小園に死球（デイリースポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE9SRE84N3J2ek5kMHRlZFVYY3hvRmZ2RkNKNjhiMGhZX05iYTRmNUt6UU1CajJwZWtUa3M5amU5VzRqSHpmLVppRV90anBvQVFLTEJDYlJ0X2ZhYmluN1hkczhzQzJlX0xXbDZ4RFdKNEvSAXhBVV95cUxObERWZllpZWVjTzRtUGlvZEVnMHJhYkZXc2FzcnJGbHZoMVpGa0dsVWZUVW14aHJmaVNDZE13amM1aXVOc0VYMFpZRnplbVZ0Q0FhZkJBX2RGRWJyOEJjeUluR3BaN3dMY2tpTzIzQ3dJWkFaZjMyMDI?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【阪神】また死球…今カード4個目　広島ハーンの投球が大山悠輔に直撃　マツダスタジアムに怒号響く - 日刊スポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMic0FVX3lxTFAzQmJxbVFpM09kVEtaOWg5aEkyQzNxWVZEOGEtR242dl80MnUxSmV3cXFTZEtWWjY0ZGNYcXItb09SZzY1Q1FuVlk4ajZYdUNQQmZQbHNDS0dDTy0zUUM5b2UxVEt4MTJqWDYzV3VFb25BYlU?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・新井監督が謝罪「まずはハーンのね。本当に申し訳ないという言葉しか出てこない」 八回に阪神・大山に死球 両軍が集まり一触即発に「その後、大山君がプレーしてくれたので。ホッとしました」 - デイリースポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxOakFXSGVNNlZxNGFCS2V3TmZmcjBoelEtLVpMTy1hU29FeVFRLW0wa05uYl9tSEZhRTRWR3E1cm10ZWFKNUE4d2pJek03UzNlRGRCSmJNTzk0NXZtTVdscnktM3hBc3c4a2p1bU9ndkVoRWdCVDNkR29nTXBGNWZUengyVUZZRnBjNXphTURB0gGTAUFVX3lxTFB3SmlBZTFGVUpNWllYdGM0dWtHdDZUMWlfSFo4TFA4NWdRZUthc09UVXNuSEVmTEJJZl80VmtvM05oeGhuN3FIMGctWWlmVWVURGU0dTFzWnNhXzNCUnVpd0JjY012Y1Z5b3Yza0dXZ0FpRlFBMF9UOExJNlpEZDRpUTRiYVVNLUY2OXg5WV85c3ZxUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・ファビアンとモンテロが来日初の2者連続本塁打　3度目のアベック弾で逆転負けも次戦へ光 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1LblNkMmY2ZUpnQ1R2RF9wejhZN3Q1MTR4M1ZUTENWUzZFUlZ2cVB2Y2lWcllnNzlFRmpYZnhNZTFOZzhMWFl4cE5EQ2pnVnJwVmpBYklsOHN4WnhnaWRIR01ubHY4VFExbk1mREZiRm1Sc2R5b3h0V2pYOEdfUWs?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・ファビアン＆モンテロ「初めてファビとバックトゥバック」 初の２者連発も痛恨の逆転負けで２０日にも自力Ｖ消滅 - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588426?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">食品消費税1% 効果に不透明感も</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588516?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ニチレイの障害 物流復旧へ正念場</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588483?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">1円玉1億3200万枚量産 背景</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588540?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">飲食店倒産増 個人店どう生き残る</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588438?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">トレカ人気 ブックオフG株が高値</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588560?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">闇バイト投稿に警告7万件超 25年</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588487?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">故人のサブスク 解約苦労する遺族</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588446?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ポケモンGOが10周年 遊び方変化</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588448?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">iPhone値上げ 中古の需要急増か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588420?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">iPhone値上げ 廉価版も10万円台</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588559?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">連休最終日は猛暑日エリア拡大か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588550?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">内閣支持率が41%に大幅下落 毎日</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588522?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">参院自民と官邸 13日間の攻防</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588472?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">延長国会も綱渡り 審議実質3日間</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6588539?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">政府 カンボジア軍に装備品供与へ</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:39</p>
