# 🏡 Family Portal 09/04

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 雨</span>
  <span>📈 日経: 64,214円 | USD: 155.79円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(155.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(60 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">5じ 10ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9PSW83S1VaRW4xY2ZSQ2tpMTNRTzExNjhFaTdRUFdFbHRLbWg3eVdUbWx6NldtOVowSTgxOUpaa2UzTU9ZZC1PaUp2c0VwcU9fTjQ3MFBfNHRfME8zeU1ZRWdFaVpOSm5KbXNINGx0YUVCUjlPSlNDbXg3aTg0NzA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・栗林 １カ月半ぶり勝利７回２失点 先発で初の２桁三振「１試合でも多く勝利を」 辰見の偉業も祝福（デイリースポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMilwFBVV95cUxQX2Faa0Q4aHJqNHUyN194RU9DTHdHcnZ1RDVVSUJIVXpCaUpHOGp2UTI1cHRMMUlyelFHVFpQaEpTR05sbUttYXRoUEJCSmluX1hVRFZWVUR4dDZ0enNqMWktZHB4dXRmT3RWWWtyWlJVR2xSNkFrUTZjdmxoaW1QMnAtSGNyU3VhVWl2R1lmdW1tR1p4VTNr?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】栗林良吏が7回2失点10Kで6勝目！大盛穂が逆転タイムリー｜プロ野球結果 - DAZN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiekFVX3lxTFBzNUhkbzNlOVIwQ0xLRVpicTBDNGFnejRPZG94SFRhcGZtQnpfMzRTMXlOaVNJaUtua2pDZFlsTGlIWENfamdzN1JoeUxUdnRaeVlXLXRwdDN5VVVmekFaZVhNU0s1S3BhR20wODBCYVVXRFQ4OUwyTkl30gF_QVVfeXFMUEYwRGI5RDJlS0lCYVVuQW5jeEtSUjNSbHQ5VC12WmJ0VHVvTURiQTJERlRVLUJ2RjRaRFZZclZQbmxscTZLdlRXT0VRTnZldnVzR2FyVnhCMjc0bXd5MExKaElfRHhycHY4WUJGR3BBWGVCQUxLbEROSTkxX3ZERQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【解説】広島　栗林、大盛、辰見…個々の持ち味がかみ合った価値のある逆転勝ち - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMilAFBVV95cUxPMGVlNTljZVJoSG5MTGE5NUlFVEtKbmF2MnFOVUwzVnVlai1Gak9wVTd3SEVZUWJSSU1zcGw4b0RndHBjcmVwN2tITDI4MlV0RS02c1ZVTkJFcjZxbjNIemZwU2w4ZFNiQkZGQXFMeElKWHdTUG1GTGN0ZV9sTFphenhoS2xnOTRvZHhhVVdNMVBnZHZ30gGaAUFVX3lxTFBWMFBHSnpZYTN5TE1TQVJrQXJTM1NiSkFfVVlucXcwa1BjWVhpYkxQMmpmeGd0LTd6QU9fNkUxV2JRLVA0bUhaTGJjaWl4dHoxZml2QUJ3MWFnV0J6M1FOUW1FX2cxeFBCX2QxNmNHZlA0WnRQbE9SMGw4YjF0TFpSQWR3bGI4R0xEMF90Vm9RdWpmU1FxdGVzc2c?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・小園海斗、渡辺リサと「なぜ今」離婚？　「経緯話せない」事情とは - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBJVEtLay1NZ2g3UmRDbG9OeDJGeWdtSGpLR1Z4TVkxVzlRaVlQb3dMcU1hRXRzT2ltbWw1NHhEQ1M4UDY0QU1zUldjUDlGRUJXTkYwWXZiVlJfYzdDQ3M2T3ZMa0M0Z051VE1zMjk1QV9fcy13N3IxOHBKRDNMNlE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・小園海斗が離婚 昨季2冠＆WBC出場から一転、公私ともに大きな変化（まるスポ） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594159?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">NVIDIA 米AI新興企業を買収へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594116?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">最低賃金改定額 33府県で目安超え</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594146?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大和ハウス 一戸建ての部門再編へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594120?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ヤマトとJAL 国内線貨物機終了へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594130?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「純金」実は銅と鉄 偽サイト被害</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594158?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">OpenAI「GPT-6 Astra」発表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594110?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">混雑状況を床投影 東京メトロ実証</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594089?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">NY市 小中学校でAIを原則禁止へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593978?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">LINEとPayPay 今夏の連携を延期</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6593969?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">論文査読にAI活用 誤情報リスクも</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594154?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">四国や九州 災害危険度高まる恐れ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594153?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">臨時国会 10月上旬に召集で調整</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594150?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">内閣改造 片山さつき財務相留任へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594129?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">維新が閣内協力へ 馬場氏推す方針</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6594088?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">麻生副総裁続投へ 役員人事の狙い</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 08:37</p>
