# 🏡 Family Portal 05/25

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 63,339円 | USD: 158.84円</span>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5JYktpeHV4dDlvTjdfWjJhc1VUMzN0ZzZ4S2J4VE8yZFdMYnBjSmFtSTVNMWZUZEgtTW1QVkdrNVJ6SjY3eGRydXF0VzV1bXZ0djdKemtFczd1aTBDaXhRalJiRmN6cHhHdkZNV003WkNXZG5oSlZwbzM3UG1qN0U?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">元広島・羽月隆太郎被告の公判でカープの複数選手に尿検査 SNSでは“実名詮索”も拡大（まるスポ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiiwFBVV95cUxPYU1hRTl1TVJTdkdsLThwUjNQZUxYWlFlNUhSUVFPa0tDUjFFdV84bmZlRHlVdk5pZTZiTTdxaDJxVVNQbmx0RTBQeXd2ZjhuYnJYZjV5TFFMWjJsWUVGX1Bwa3Q3VV9IM3d1WVNyR3Y2ME1sVFBIS2tyUGJpVWk1LWhWYlhNMkxxSWVv0gGQAUFVX3lxTE4zT09kYkc2eUlsMjFWVDlvXzNPMTN3RHhsQlZ1SFA1dkRkbFZ3ZWJLRFhqcmV5djE2c3J6OHVieFlWNzBCOWppaHBOM2tuSHFlYm9ubW5OVTdWSUVhNDlucmpPbFVMN2tCVUV1MjM2bmN5VXNwUGFxYjljSTB2UG5zSVA1VTRwaUdTQmMzb25neQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">市制移行目指す「人口全国最多」の町、焦点は新たな市名　広島県府中町、既に東京と広島に二つの「府中市」 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFA1X2ZCcURuNGVmazhVM2VVZWlpN1hPRUU1RGdEQVVGUUNmWkE0QlV5UVhJanBGN3ZmQXFwWGF2b1Q4UFZaVW1OUkI3SFFwVHFBSFd0THR2RXprbWFuVkxSNnMwMjdSOTMtWmhXeVoyT3lOTUdNNkpVb21PX2ZSN00?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【中日】広島に2戦連続逆転負け 最悪借金”15”＆12球団最速30敗...初回3点リードも髙橋宏が6回一挙5失点でセ最多6敗目 9安打で3得点＆10残塁（TBS NEWS DIG Powered by JNN） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMic0FVX3lxTE02bUpMT3U2dzliZkdzWW1CUVc3Rk5iSDEzOU9CckRhdy00RV84QXpIOGh4ODJFMVR2ODNKMUFVZEhRVmF3R3JxTkstWGxSRU55bmN4VjF4QWRvMF9kb3FILXF6ZHZQMi1VQTc3ODBkUGJUajg?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・名原から六回一挙５点！持丸が走者一掃の逆転打 育成出身コンビで天敵・高橋宏を攻略 ２年ぶり３カード連続勝ち越し - デイリースポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE5tNzRSeW5KZzZvSUdXaDNQSkthZ2JrRjdYWXdYOVlyU2Z0WXhQSERGR3FPR1VWY2M1TGgzRllidGVKbnNmUDA5cnQ1OFRHdVlLOWVDdTBqQWRTOUR3d1hfM3Q5cFFwWkhVZWxjMzB0dlnSAXhBVV95cUxPOVBoLVdjR1BvOURxM2QtREZncy13LW0zX2wwNUhEVTdFakIxSGhOOUdKSTFIVDMyTVkxVVlqQ0ZMYzBUNFZISW9oYVNjMmNSRUlrVW1VMF9mS05ZT2JrdGNHd19NdkQ2M0YyNVNYd01NT2pzY0V3RmU?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】小園海斗が２回裏守備から交代、新井監督が苦言「士気が落ちる、今日だけに限らず」 - 日刊スポーツ</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581500?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日産 英でのEV部品生産を撤回</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581495?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">美容室に訪日客 常連離れ懸念の声</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581533?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">chocoZAP「女性専用」展開 背景</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581467?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">リカちゃん米に再進出 40年超ぶり</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581452?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">バインミー専門店が増加 なぜ人気</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581543?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">携帯キャリア次々乗り換え 問題は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581470?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">連日Xの首相 問われる取材の意味</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581539?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SNSで増 カラーハンティングとは</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581395?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Anthropic評価額 OpenAI超えか</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581370?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ナフサ巡るデマ論争 首相きっかけ</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581536?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">内閣支持率50%で発足後最低 毎日</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581501?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">赤沢氏が訪中 日中関係は不透明感</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581522?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相宿願「国旗損壊罪」急ぐ自民</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581511?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">小沢氏 中道が軸の政権奪取不可能</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6581490?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日赤名誉社長・近衛忠煇さん死去</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:44</p>
