# 🏡 Family Portal 09/28

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 雨</span>
  <span>📈 </span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(277.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(90 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">9じ 15ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1sYUh0eTAwcjV6b1Ftc0VzaWpxQTQyckJGcHRSa0g1RE1TalN6Nk12MzZDZWp0NGpYT3l0UjBseC14UTAzRUQ1SGRGeFZHcWxMd0xXSlljYlB2UkxDUU03dGxuOXN1aEtEalJDaGU3QTlFT2xtUHRGbTBrWlUtUWs?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】菊池涼介が決勝打含む３打点で３連勝、大瀬良大地が13年連続白星となる今季初勝利（日刊スポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxON0JoeDI1dFI0OEUwT3Y4VUFTNXlaVzl5QzVQVnhmZ1ZsOVlNMHFDU3c0a0NlZ2RpdTN4NnRfemJ3akhaVWtELUV0TzM2RGIwQVpHWWlKR283WjVnR3N2MUo1cWZpbk01dDZBSWJNcGpZb3ZBalBIQUhHdVdjS2hSb3NwNE5CdFVJZTYxSWM4SEZ0Z3NoVndTYV9mNzZldTdjUXlLU09TR27SAZsBQVVfeXFMTk1LRUZKSld0VXlRZFQwSV9Ia1hWaGlyS1ZWb3AxWHJNV01sVkVlNTdrXzl1VWxFMnM2VWotYXplYjF4QUNJV0hGQkVQN0pJVUNqRFpoZkJxY3Z4ZG02elJoMXA0TXRjQVdnM0JvVjBsejFnaklITDhxQ2x4ZTY5YWFITUU3LVhUaGJQTHY4NHR5bm04MXV1MGdlYTQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】大瀬良大地が今季初勝利　13年連続白星「周りの人に支えられながら積み重ねてこられた」 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTFBsajVKRXZ6V0xKVTVrMWlfMk82WkdGbjlqRkNUWHA2TWJ4bGNvTzNRbi1jT0ctUE5QLTNURTRxM0psS1VSOW5BSEtVS0J4RW1Yd0lxSDh3cVZiN0hDS20yb1pYa0VEdWJrSEh2aXFoRmPSAXhBVV95cUxQMGw5Um1CU1VXMTRJd0o0Z1pyUmduMS0yYnM4UFdNS085dVZ6bm9lNXhoOHBYMVRjdWJGSkFveEU1OS1jLTAzLVVEX2RJeFdja3RpMEJhbEZFTjlPNWF0STktRGRQX0Q1TnVhR1ZkSUFieDNTR1c5Sk0?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【DeNA】相川監督「結果的に…」四球が全５失点に絡み広島に逆転負け「一番最悪なパターン」 - 日刊スポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiXkFVX3lxTE5JaXlXVXFOUzBwWVBERjJKYmNtaGlpd0RMZlRDNmdqeWF5aVh5dVdraUFIM0JiRlFJQ3dpUVFGTW5oU2txMXVFaFFoT1ozdFVBOF80dVNnc0k5UzJGekE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ゾンビたばこ巡り広島カープ2選手を書類送検 - 新潟日報</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE9RUld1RjRuWVN6VTV4NVFRajA4b29VcmEteno5SUR1YlJXQS1WX3JGdXBlNDBUdWxKQVV4TnQxaGtpRGRQNk0yaEZnd1hCSTlTRmRfWm1JQmdzal91Z2pVeXpnMlBVRkJ0cFl4RnNoS3DSAXhBVV95cUxOc1Jic0NUOXBSTGYySDZqUHZiZ3dNaF9EbTdVRmlydVVULVFncGVjb3cyOHlMOEVSVDZudFVwUkVxUHAzZ0VrMVdyX3ZnRnQ5U01IdVE1TW5hU0ZkcmlNRWgyOV9mQ29mcndsUkJIVmEyb0F0T25EV1A?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】「ゾンビたばこ」巡り、矢野雅哉と前川誠太が25日付で書類送検　球団本部長明かす - 日刊スポーツ</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596719?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">台風25号被害 千葉の観光地に爪痕</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596703?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">家計影響も 10月から変わる暮らし</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596754?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">長雨で作物が根腐れ 絶句する農家</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596729?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">国と攻防30年 ビール系飲料の税率</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596691?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">混雑率177%も増発できず 3つの壁</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596794?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">治安維持向けロボの開発進む 中国</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596724?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">声優業界 AI無断模倣の被害深刻</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596712?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">東京メトロ メアド5.9万件漏洩か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596707?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「俺が?」刑事一転 SNS戦略官に</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596681?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">光通信衛星を数百基整備 NEC計画</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596789?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">台風接近 沖縄奄美は高波強風続く</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596797?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">裏金議員を要職「問題」61% 毎日</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596768?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">原発事故時の拠点病院BCP策定4割</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596689?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「政治とカネ」再燃 自民に警戒感</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596706?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">岩屋前外相らが訪中 関係改善探る</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 09:05</p>
