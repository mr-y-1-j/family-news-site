# 🏡 Family Portal 08/23

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 66,016円 | USD: 158.94円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(87.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(330 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">2じ 55ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFA0WkNibHhLTlhvNTR1OEFkOFE0M2VRMFFsVzRGbVJUYlk0QnFGRExTclB2VU5CWllPUktjLXJBdWJaZ29yS3RhWnFMS1RDYjliS3VsRk5TZkVva0VsVWNiMTRzbw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「ピースマッチ」引き分け 広島、３連勝ならず―Ｊリーグ：時事ドットコム - 時事ドットコム</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiekFVX3lxTE9TcEJRX3JfUDg4Qi1rTWRkQ0ZnUTFIN0xScUY3S2swQTN2WnV4Q1BfM2toUWR3UDQ5azAzX0N0YlZGcU1zd3JxVUZrZXdqRmF5RzNXdmE1Nk9DcldXeTdMUnE1STJlcFdncjJmOXBSUTVkSnEtMVR0M3Nn0gF_QVVfeXFMUGI0LUdQZlBvbWNhOU56bUV1c3BLZzFSajI5elNtdnZYMEhnRURwT0lkRy1MMHZ2RnZCdEVNRjVKTnJSOEdFajgxU3hkcTdyZHBvcHNQTms5TTZXd3U2T0paMzF2S04zMm45T1RUWUpDdjJIX0QtUHZnbE5iS2ZHcw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島が引き分けで開幕連勝ストップも勝ち点７に伸ばす　加藤の今季初ゴールで先制も後半に追いつかれる　ガウル監督「攻め続けた姿勢は素晴らしかった」 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1RWG1lT2k5NmhPVklNNGM0LVdOSmMxRkdrNGpzdnZrb3RpZzNDM3hDZ1hZVFBPTDRTZWVvOG5wT05TUEpjTXFVNmdMVzhROWZYNG0xRk1iQ2RKUlZoSWFzeGtPNVZrWlRTUzZScmFBVWxqeWhuM3pJcVlaS2VwZjA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">開始直後にドグソ疑惑も…広島がドローで開幕連勝ストップ、川崎Fは3戦連続引き分け（ゲキサカ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1abFlxRi1rY3R4QVI3Ympqa0VCeXJLTTkzcXRuRDJoZ0ROVWhiTloyTHJGR2dfbXRYb2xEYnFjTFM5RnVIajBuQmNVN3loUDZvdzhiMFlseTFqdF9BMERGa0VXTTh2WDFQbVNNNHdBd0YwV0VYdXVCTExVZ1RZVkE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】２戦連続完封負けで最下位転落 巨人・代木大和にプロ初勝利献上…新井貴浩監督「絞りづらかった」ビジター４１イニング連続無得点 ８月敵地は６戦全敗（スポーツ報知） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxNQTF1NUhZWVNqbUhxSWJadDdsOTBuY2xaUFFwc0FXcE01RHBxQW53c0taWlA0MEpqb0dwTGVQX05UVlRoSmNhakhIZklHYUQ0TWR3aUxCNkJUbGN3UmdaUFFYbVRITktOamJ5VkYyRjZMdDgtcU4wbHFyaGNtZlp4YW1tTWxOSEJKaV9OSG5n0gGTAUFVX3lxTE9uMUF3d2tmemFaUi0xTXk0MGo1M0ZnRGtjSGZJUi1BeXAyU1BiY1d3MC11b0dnUVNjZXR1UXJsM0ZLcDdqV2dMdmVpeThfS3JoMVFwYTZSZHBzLWxrRkVJQm9ZdXd1M0Q2RC03aGxoV1JSb0liWDlhT1AydlFPM0Z5bl8xRkFDU3hXZmh1VjI5Z1dGYw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・松本竜也「自分が抑えていたら…」　2番手で今季初登板も、失点重ね唇かむ - ｄメニューニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592621?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">地震で突然失業 肩落とす被災者</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592697?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">爆発で休業のイオン 従業員は不安</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592604?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">100均業界2トップ 快進撃の理由</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592622?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">新幹線の通路に椅子 JR東の見解</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592665?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「自販機」に逆風 飲料各社が工夫</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592700?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">架空の党員をAIで作成 立憲苦言</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592695?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市氏 なぜ国会ではなくXで反論</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592628?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「味の素」広報にAI 炎上の本質</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592620?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">TikTokが636億円支払いで和解 米</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592565?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">難しい検知 bot不正どう対策?</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592717?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">茨城などで最大震度5弱 津波なし</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592706?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">衆院比例に「サンラグ式」案浮上</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592655?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ICCなど巡る高市外交「弱腰」批判</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592651?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">原爆「包帯の少女」の証言公開へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6592704?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">事件で浮き彫りに 介護のカスハラ</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:09</p>
