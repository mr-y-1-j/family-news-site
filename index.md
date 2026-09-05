# 🏡 Family Portal 09/06

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 65,021円 | USD: 156.22円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(47.50000000000001 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(210 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">1じ 35ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5lcFNUTUROUXEzQzREanEzNXphZzRaOE1qQjZRY3RQdElKLUlQTE9PdE9OSnV1eVphajBZSFdOLV9pS2FfbVlCbXA3M1hfVGJCU1JTYktjQlZybHQxQXJIc3NzR204Mi1keDA2dGktRzlUSTYwTHFWX3dIT3N1T28?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「世界のコバヤシ」がブルペン投球 巨人・小林誠司が広島戦延長11回に非常時登板に備えて準備（スポニチアネックス） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMilgFBVV95cUxQN1RWX3dBNkVhZkpFMEVGR2NMZW1Oc1NpdHh2SThJTDU3VndnVHlkc0ZlemhlZVlYN1g0OV9nemh2MXBBS2NIMGJfQV9aZVVUUXV4UnpSdklpd1RMYUpqUy1WNWdWR2JsY3hrWF85azhfVlh6dnVIbUlqTFRQMjh1ejhJdWUzRzU1d1BkZ0RPSldPelZhY2fSAZsBQVVfeXFMTTg1TDB6S1ZJS2VFWHpySmp5cXY0cHVfYXgtVTJRMmkyU1AwYmhoaEdOVmExTlpQY2ljZWJsWFNWS0g5emtCZUVHU1pOQVZYbWN0WWM4TEpJVk1aWUM1YjdhYzVZUm44VmFsekNYa1UzS0szX21iNXF3eXlNTExBcEpNVmt4VUJKWVBxUXdtUEh3Wk80VHlVX29qejQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】新井監督、先発玉村昇悟の４回降板に「どんどんブルペンがきつくなってくる」／一問一答 - topics.smt.docomo.ne.jp</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiTEFVX3lxTE9mQVVWYzRfbXhJVUxFV2dKMEJOdjlTQTBvUGNNLTI1SW9GcURWSGhtTFFsVUVYTzktNS14bEtxN0NTT3RNMGx4RXVSOUI?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">天谷氏「守備の方での貢献度は素晴らしい」開幕から一軍でプレーし続ける広島・勝田 - ニッポン放送 NEWS ONLINE</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMilgFBVV95cUxNcDVOSzRhekpRTmpxbm0xQzNrWG0zZkFvRGd1UWFvRjhwS2VQMEw4cU0waHFyYUdPNmNfWjJVaGhNcTAzZVRRVF9jOVZLMnRHNWlmTEdXSUd3RlZCeWVnTHRENHl0Y2ZtMlo1Z0dOSzFoWXIxZVNXWHVaN0JLVGJtdnBWTHdNMDNfMzdqQ044aXk5cnpkbGfSAZsBQVVfeXFMTjRkMGlleFBVd2h6VnM4eUJ6eU1QRlNncUxYTHdib1kyb1g1eXRLM25NRGJBODMzaUF0b21tc3ZPX2xpRF96VTFuZ3ZRbFBnSVhJTlo5MTViR3h4LVl1X1NqTUFNU3g0NE9LMnBhZ1RGcUZOX1YtdHVKX2FLaUk5cHlWYVVtWk5SMVBOY3ZPSXBuUTQzVHNLa1pFWjg?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】ファビアンがホームラン性の打球を好捕、２戦ぶりスタメンですでに２安打と攻守で存在感 - topics.smt.docomo.ne.jp</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE05ek9vNVV5VUpjWlItOElabFdnZUhWMjVheWh0ZGpGWVJiYlF4OVVGcHVWMmtaQ1hJV3VXdU1VcV9kV3hyVFhpY1NucHdpa3N2cTZyZ0tZRks5bDRKTDJLcE11Q3BETTZSN0Y3b0pUR1hfbUNYQ3ZSOUJDX0c5TDA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】ファビアンが大仕事！ 「ホームランキャッチ」で勝ち越し許さず 石塚裕惺のホームラン性の大飛球を好捕（スポーツ報知） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594376?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">出版業の倒産急増 利益が悪化傾向</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594343?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">獺祭が1億円寄付 豪雨被災地など</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594334?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">マンション一室で旅館業 民泊問題</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594316?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">家買う若者と3畳住む若者 共通点</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594274?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">住宅購入急ぐ若年層 リスクに警鐘</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594300?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SNS「setlog」若者になぜ刺さる</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594243?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">異例 任天堂2日連続新情報発表へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594230?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大阪高裁 Teamsに約6000人誤登録</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594217?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「新R25」9月末で運営終了と発表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594209?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">キャラの自作グッズ投稿NG? 見解</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594342?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">西-東日本 警報級大雨が続く恐れ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594335?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">29年に中低所得者へ現金給付検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594375?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">内閣改造 林芳正氏の去就焦点</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594345?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">内閣改造 小泉防衛相の留任で調整</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594361?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">露に対日戦勝碑 首相が撤去を要請</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 08:26</p>
