# 🏡 Family Portal 08/30

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 66,406円 | USD: 160.04円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(315.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(180 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">10じ 30ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxPbXFVZS1UREQyT293OHlQMUlGTW5rX05SZUJkWmRHc05NUjlzRktaeEU0dHlPa1plZXo2RVNRLUlsakRtc29WWGdFZERzQlBKYmI4WnpCU2YzZ3ZaR1RqMUdla0YwY1kwUU5jR3Ffek9kUmhublFSU0ZQcmpwem5odHJ1ZS0wTFpqQ0lGRmJ30gGTAUFVX3lxTE53T0w0a0NrcnBrQkRMR2phNkl0N1ZMR3FJQjRHcGtoMGdNOWhUMGh1UlcwNU9Val92a014dW8yamdyUmhHeUtGcFFmLWotRTVaektoMmRmQldDNU9IT25yTl9PR1lCZEFjT2RscElLazlWODE2WEcyMFlPSmg4Q2hyWUlUWDBsV2tvMnJfM0tCcnZXRQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島　スカウト会議で横浜・織田翔希を高評価　田村スカウト部長「大学・社会人を含めてもトップクラス」 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTFB1RnVnMjh1WjFkYmtZejVoNXNsRFlDaFFhTE5ReEVsQ0lQSzllSklST2lhMUNWeTFUMzZRRkNDU0p2R0V5RkFXRGFlTUVIQWtTdzFsaTNQTjBZSEhlcUM5VTBR?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】田村スカウト部長「本当にすごい」甲子園“最速右腕”に最大級の評価 スカウト会議で高校生１９人チェック 最速１５２キロ＆高校通算２０発の二刀流も - スポーツ報知</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMic0FVX3lxTFBST3BhT0NmMjFpSzlrR0VzUFNrUGJfSWdubURyU3o0amlZbEhWX0NPbWlEMk5feERZd1p2a2ZiRzhqMUJOM2d6VVN4NmtxSlJ2YnJqemxiQW1OSHdKeXpVbUd0STVhZ0lxS25GaUc1bmFjRXM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・田村スカウト部長 横浜・織田に「すごい人がいらっしゃるので。球団としての評価も何も、もうトップです」スカウト会議で高校生１９人の映像確認 - デイリースポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMilgFBVV95cUxPMEZZdWxhaWxNWGlCdkpwQnpuM01MX1JCR1FhMFY2eU9pVUJkdmhHM2FpbjcwSngycXh4LVZsZmxBMXVTd1BKc3Fpc2dHZml1aDVCMVJNU0c3Nmd6OHZBTHNCOGxQelBnc3huTjJXUm1DTUNvNmpuMXVnX0lIT1J5SnFpUmlNemRGNVhTLS16Vm1kRlExVlHSAZsBQVVfeXFMUFdEZFZNY3J0WG9LMWlvRnAyNUcxUDVGYVFrVHQzTHNkcldxYUpYaWxTY2JwTDFld0pac09CV1dtck5xSkxLWmZhS2pxNENnWjJsTU1GT0NLR0FmOHZXXzlOMWxmbnNaeTNjZGQ4Mk5LOXUwTnhhNmt3ZUo4b3dLcW1rX1JZWC1PcUw5ekdPaVlEbWNJbWxfYWt1azA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">元広島アンダーソンがドジャース戦に先発「カープ時代もいい投球をしてくれて」小早川毅彦氏解説 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5KekpvbHpIdnpkSm92U1ZfQ3E3ZlZCS3ZqTUtsQU5Vd21HMWdJaktHOWRFZ0RFMEdILTNYQV9weXo2aHoxbUV4RFlvam1teGNRMW5hUHdqQmZpclpnNTc2cjJiNm51dFJOM3lTU1cwWXNXZURVemhnVWVpX2lkMW8?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">大谷翔平 初回第1打席は元広島右腕から空振り三振 連敗脱出へ、8試合ぶり豪快一撃に期待（スポニチアネックス） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593500?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">円が下落 介入効果4週間で陰り</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593460?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">FRBによる9月利​上げ観測高まる</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593433?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">9月の電気ガス 全地域で値上がり</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593423?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">社員逮捕 竹中工務店の副社長謝罪</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593483?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">17年で社長が7人 百貨店消滅の街</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593448?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中国のヒト型ロボ 本当の脅威は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593422?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">イエローハット180万人分漏えいか</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593415?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Anthropic 機器とAI接続規格開発</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593385?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ゲイツ氏のAI巡る提言 実効性は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593388?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">購入済みゲームの維持 各社対応は</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593588?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">福井県に大雨特別警報 最大級警戒</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593581?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">福井県に大雨特別警報 最新情報</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593206?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">安全確保を 大雨のときのNG行動</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593582?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大雨で浸水リスク 車移動は危険</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593545?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">千葉豪雨 半壊判定が大幅増見通し</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 08:40</p>
