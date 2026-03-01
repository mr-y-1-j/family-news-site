# 🏡 Family Portal 03/02

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 58,850円 | USD: 156.24円</span>
</div>


<div style="margin: 20px 0;">
  <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLKeSkfHhKSzLQqP7Rz5z25kMs726xU5p-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 10px;"></iframe>
</div>


AI編集長です！03月01日のニュースをお届けします！

### 今日の3大ニュース

*   広島のマツダスタジアムで4月、「ポケモンベースボールフェスタ」が開催されることが決定しました！
*   OPECプラスが4月からの原油増産を再開することに合意し、今後の市場動向が注目されます。
*   AI開発をリードするOpenAIが、米国防総省とAI導入で合意したと発表。AI技術の活用がさらに広がりそうです。

### 豆知識

今日は3月1日「行進曲の日」です！アメリカの作曲家、ジョン・フィリップ・スーザの代表作の一つ『ワシントン・ポスト』が初めて演奏された日だそうですよ。明るい行進曲で、気分を上げて一日をスタートするのも良いかもしれませんね！


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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(195.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(180 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">6じ 30ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBPcm02RWJUOENmS0lZTGNnVGs5V2d5SE9LX0d4MmwyMjNfU3N6VUI2QXJOMGpnR2lGMlJrTHdRN0NvNHZDWmtCdzRndk9JVlMybGszYlBTMUc0dw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">東広島市中心部の交通渋滞解消へ 市が本腰 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE1Ebmt5NUNkV0JSdG9pT2oyYVhtdjVOQ05xNkg3Ymoyb0lORi1SR0R4RW5ua2d5dHNxVTlWQjJ0NThmamtjXzBvczFKS2lKOExuYmM4enJ2NXY?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島で「ポケモンベースボールフェスタ」 マツダスタジアムで4月、開催へ - 広島経済新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5uR3pPWVZkbWpoN1FUUmR6cEE2MWI1UGpBUUtUdjlMbnRRbk5YaW0xM1RYME5NSmFLRnBpNVhkWFlwem9Eb3NGbVk4NUFyZUUwVTVDT2ctbmF6SU5nZm4yZXRuZDZEOFp5RkhMem5hWVVxNVBlWWZ1N0ZVSHF4MVk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】新外国人フレディ・ターノック「全体的に良かった」４回４K１失点、開幕ローテへ前進（日刊スポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxOX1ItQ3kzRHE3VEJPd3Fwc0JUT04wam53ekpURmJ2a1RETG5Bb1lpNGs3NjJzV2NfU2pnYXFjTExyNGxVWjFma0NDZ3ZDZU1Ja0dnUklyTHE5TktHV2ZKeVNUVmRJbkZtY3NnVG84U29hTTdWVFREQTQyRk9aaWxrTmwxaWViYXlEM1pidVhn0gGTAUFVX3lxTFBfSFdyeG5wcVdLdGNaV0pQX3RCR2NEaXBLVnRvTEY0N1oyYzBZckJiS2ctTWpDMGxaQ0xfRWJzcDFxVHFQRE51c3R0ZGJhR21WSzVzWmVIanZnRGZiWHVXSVRNLXVvcnZ3VnlFQ0I4TENkeENoQmZNaFFnX0xWN2UwOFlTNlJSSzVWUDJoZnhhb1EyMA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島　新外国人ターノック　2度目先発で4回1失点　新井監督は高評価「ナックルカーブも切れていた」 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMifkFVX3lxTFBMTjBoSjB2bW9LdEt3Y3R4OXBUX2lfMmFEN2Y3aVNhREJIY3h2b25RejJkV2tPSkYtTE5aLUk5SUF1SnNlWU1NRmxaUHNWczA5cHlRSlcxWDM2NXNaVlB2T0FfMVpkeUhhU2hVdUtRdXhaSmJGbHhnSnBtOFNYUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】ドラ２斉藤汰直「どんどん成長を」フォーク武器に１イニング無失点 先発とリリーフ“両にらみ”の戦力で期待 - au Webポータル</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571707?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">OPECプラス 原油増産4月に再開</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571691?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日本の海運各社 ホルムズ通航停止</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571714?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">トラック運転手 隠れ残業が常態化</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571704?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">小学館 漫画賞の贈賞式を延期</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571666?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">一部スシローで決行 順法闘争とは</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571571?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">優先席巡るSNSの議論 識者が警鐘</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571558?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">終了迫るドコモ3G 放置で影響も</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571534?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">OpenAIと米国防総省 AI導入で合意</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571495?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">OpenAIが17兆円新規調達 SBGなど</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571442?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">インスタ自殺検索を親通知 米など</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571709?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">イラン攻撃 日本は賛否明確にせず</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571721?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">政府 イスラエルで邦人の退避検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571706?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自維 衆院の定数削減法案提出へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571695?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中道が立ち位置模索 追及は控えめ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571684?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">1.6億回再生の首相動画 法的解説</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:13</p>
