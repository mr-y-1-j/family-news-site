# 🏡 Family Portal 05/11

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 62,714円 | USD: 156.87円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(60.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(0 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">2じ 0ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxOZ0ZGUzBZRE1uS1BNRUZUUDlLREU2eVU3emxmY2t5R3UybVhNdWZLSVQtRWI2b1JmcnlNZENKWlJGQkNmTGxTUlQydWtQS2ZoQndfeDBzUG5jQmo5NFFnOGtHLWhOZWVSakpva1JHWkIxTEVQbmdSSGJHa1MyTTM4Y25faUJVbGNiaGlfQnJn0gGTAUFVX3lxTE9qOW53Y2FteXdSdlVtRnp0NGNMSDBJTjZ1UWhzcTUySmNxV2hpeFhCbkl6NVFYUU1NUmFaYXVDZXM2bXRBR2t0RU9NcUl5anI4YW9ldUxicTFPdjJRS2tsaVRGdjg4YzlqVWs2ZUZaX2NiZnhDbkVfRUM4VzZqUkJ5TGtyTG1uTTI5MDZ0Q2ZpX19LUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">はまった広島のオープナー　7人全員好投の流れ作ったのは赤木晴哉　将来が楽しみだ - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMifkFVX3lxTFBwakdvbGpPZ0xhVWtuek00b01qaHBVRFB0d1V6SWwxVnFKNUFnRDVEZGFieEdWLU1KaEZncEQxOGNRUWMzWmdPMU02UzhSSEtmTGRMWXM5cUFFQ0JvR2V0ZjBGRkMxVVkzMGJxNHlpU3dwTnU2Vk1iY2ROdkpyZw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・ドラ5赤木 母・恵美さん始球式→先発の“母子リレー”から球団初7投手完封リレー「お母さんから始まって、最後までゼロで」 - au Webポータル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMie0FVX3lxTE1yQ21HN0lJY01ycFdyNFZjYldTVDMtcmtsQ3E5THRJSmJUR1R5eFV4ZUhabWpCUHVLdVJyUGV3UmdPODBfQ2hQdVFHM2t1ZE5tQXVjUHl4WDFub1ZzNnNLZnhhNnFwSEJ0UUpLeDdia3pvaHlGQXAzVFdjSQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】ルーキー赤木晴哉を1軍登録 プロ初先発へ臨む（2026年5月9日掲載）｜日テレNEWS NNN - 日テレNEWS NNN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9KOGE5Z1IwUV9adHBUZEI0T3g4RnozU3RyckxYQ2FJNC1hb1FqdEJyUlR5TDJWazBBSkpvcXd1eE5ubEJCYmNIOFVMRXZhVnlsSnpna0Zzc2VyX1F0TEE3UmxEZVhQdUk1VUpwdkhfcTJsdFhXYWlsa2ZBVGZGblE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・秋山が三回守備から途中交代 なんらかのアクシデント発生か？（デイリースポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxNZHV1b192cWpCdi1xMzJzRzdQOF80ajhFcVRYQWdISVFOUjFnbE5KUkRiX1VfZXFJdTlNcFFPMlo5LUNqU3E4VDlmNnh6ZDlPdzNfTmVYV3JGQTJxampZUlpXQjNGaVhzeXIzZzZVX1hXZkFxYUVEX0dQZGxRazlNTnRvcmloOS1QQURFR1BB0gGTAUFVX3lxTE9XczlXZ243dm8zMU1GQXVrdnRQZzBNZXhxS1hONTJ4cUdZMzVfR29scTIwUEZkUVI4cE5YUkVYQ1huWFoxRWRlSzZrUTd4aU1XZWxlSS05YTBSOEpzQVN0NVdhRXVVU3V6SE9iWEh3R3hDa2drdUZhSVFab3F0d1c0UzlDQklfVzdSOHV5QjdpRWtWUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・秋山翔吾が左ハムストリング負傷で登録抹消へ - ｄメニューニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579490?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">閑散期でも活況 ライブツーリズム</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579509?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">パンダ不在でも客足好調 白浜町</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579518?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">プラごみを油に 挑む「都市油田」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579519?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">クルーズ船・にっぽん丸 歴史に幕</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579550?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大阪駅直結の2フードコート 明暗</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579561?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米企業の新型AI 危険視される能力</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579467?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ゲーム機値上げ時代 今後の展開は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579320?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「Switch2」値上げを発表 初代も</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579312?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Switch2値上げ発表 苦渋の決断か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579383?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">デジタル教科書 IT先進国での失敗</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579580?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">本州は夏日続出予想 熱中症対策を</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579547?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">安保3文書 中国巡る表現が焦点</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579455?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">政府 成長分野での学び直し支援へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579481?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">健保法修正案 立憲公明の概要判明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579514?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">健康保険の扶養見直し案 誤解も</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:35</p>
