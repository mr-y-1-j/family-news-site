# 🏡 Family Portal 09/23

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 65,019円 | USD: 157.47円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(67.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(90 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">2じ 15ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1ldjVOU3lMdGotdkxjNERpMkFqVUlJdC1FUWhmWS1kSUVuZFhiVnkwSXZNV3hPUjRyY3lWQml0SUIta3BSbHNXellTT0VyaTJKa2YzQzhiVUFlb1YyXzFLT2V4WTl2RkYwQ2syZ0RzcW1jbFhQaldFREVndXR0Y1k?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">西日本では定着も関東からは少数派!? 広島への修学旅行 「平和学習のノウハウがない」 関東の中学校教員対象に「平和学習」研修会 （RCC中国放送） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9zNjc1RG9HQVZaNjM3Y0ZtQzVRQ2U2VTBQaTluaXdld2JNT1BDZmp6d2JsSlVvX3ZPTGtXUnp6S29kYmdLdXM3UTNNU3BlYktSS042d3NpRnc5ZktoVjZVRmVKbjdDSkdGeEdlWjVkdi10THp3Um1Wc0FuR2dOMmc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島×ソフトバンク 2026/9/23(水) の試合速報・結果 - sp.baseball.findfriends.jp</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1hb3JhNnpqaWV6bld2VFltUkRMamRpOUI5dDlXTng3cXIyWHA3TnJjbkUxYV9ZZG1nMDg2YzdOQWVmdTU2aXhfb3FmVlVFMGUzX2tySWVMb3lwTWFQWWdFOXhWOXlGQmR3dFhjeWVuTTJGZWVBMXc3OWlHZ19tMDg?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】新井監督「託していただいた」来季続投決定に言及「自分がやるしかない…自分しかできない」激動シーズンを経て…来季５年目（スポーツ報知） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFB5QUlleGtHTElCclc5bkxTSmUyRmlpVUlGU1VLN19WbEdNb2RlNW9YdlBCMG9wQS1nR2wtTDZpcmJTRVBRYzVHYkNnbXZwTkVoLXBZeEJ5SldPT0hZdl9B?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">プロ野球 広島 新井監督続投の方針 来季は就任5年目へ - NHKニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMirAFBVV95cUxQWks1RC1rNVFHaVYzYVhsNkNfdHo4SUZ6ckZlbDRHU2YwdGg3MVotWTJ1WXFNSFF4dXNUVzFDandjNFpLeUlTN2JCYm9JaVhqU2pTWG1EUVBLcjdSYzFlc0Y0ZVdtaW9TY0JDSFRwSXZ0RFBGRmpsRjVpMmhHMS0xSHFKdGxocGtmWjhmTlZjckhidThsUVhobzhkdUxFSWp2UkwxZUFiRnV2R3pl0gGyAUFVX3lxTE1lS3RtQlYzdTJERENiZW5YSFIxcWd6WVdIYWg1bnJRMTR6X2tPMEppdW5XLXJJajJKS2tBNk1UMzhqMGtsMmhoS3NjS2ZfTXFGT0lJWHNvdEM4R0ZHakxQU1BzUDZpazJ0bVhUdkZPdXQzSXNkbk1oSFVxWDVhRzRTQVh1S29ia2JIWkE2U3BhYW1MRXBGRWlvM0hjdTVSay1VakdBU2hNZFBYT0djYTJtZEE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">虎のソナタ　「明るくハツラツ、盛り上がる姿を」　広島・新井監督の選手時代を知る元虎番がエール - ｄメニューニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596209?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">とび職に逆風 倒産過去最多ペース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596115?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">赤潮で魚153万匹死ぬ 被害37億円</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596162?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">東南アジア食品市場 日本の勝機は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596158?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">パラマウント WBD買収へ前進</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596120?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">修繕費計5億円超 観光施設閉園へ</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596210?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">波紋 大食い動画の収益停止相次ぐ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596201?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AIは「SI」に改称 米大統領宣言</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596184?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AI搭載の人型ロボ 防衛活用研究へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596176?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AIで鉄道運行支援 日立が本格展開</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596144?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">古書店に大量注文 AI学習目的か</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596202?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">新たな台風発生へ 27日沖縄の南に</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596156?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">水害後 片付け・復旧作業の注意点</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596200?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日米 経済安保で連携の方針一致</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596091?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">副首都 6道府県6政令市「意欲」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6596077?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相 国連で「拉致問題訴えたい」</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 08:54</p>
