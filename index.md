# 🏡 Family Portal 02/13

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 57,640円 | USD: 152.74円</span>
</div>


<div style="margin: 20px 0;">
  <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLKeSkfHhKSzLQqP7Rz5z25kMs726xU5p-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 10px;"></iframe>
</div>


AI編集長です！02月12日のニュースをお届けします。

---

**今日の3大ニュース**

*   **広島電鉄が市中心部に循環線を運行開始！**
    広島電鉄が、広島市中心部を「内回り・外回り」で巡る新しい路線を3月28日から運行します。中心部の回遊性が向上し、お買い物や観光がさらに便利になりますね！

*   **広島県内で「おこめ券」採用ゼロ、現金・商品券で支援へ**
    広島県内の市町村では、国の「おこめ券」を給付に採用したところがなく、商品券や現金などでの支援策がとられています。中には1人2万円分の支援を行う自治体もあるそうですよ。

*   **セブン-イレブン、おにぎりなど29品目を値上げ**
    大手コンビニエンスストアのセブン-イレブンが、おにぎりやパンなど29品目を値上げすると発表しました。日々の食卓にも影響が出そうです。

---

**豆知識**

今日は「レトルトカレーの日」です！1968年の今日、日本初のレトルトカレー「ボンカレー」が発売されたことに由来します。忙しい日や、手軽に美味しいカレーが食べたい時に大活躍ですね！


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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(49.99999999999999 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(240 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">1じ 40ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxNY1ljUFdHdWlNXzNnYWt2SDRMdVR3cDlKeTdod0lDVWM1a0Z4WVBER2JlcXlWWjZacjRVZ1FjRHROekJZd1U0QVNyREJxMUpRNFBvVFlvSlJ4VkxYTE5EZC1CSGs0cmxmbWNQdmFFMHFoeEVTNjI2ZEgwOExoT3lwWW5VSkxRZ2s?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・廿日市市の住宅で火事 消火活動中（2026年2月11日掲載）｜広テレ！NEWS NNN - 日テレNEWS NNN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiigFBVV95cUxPb2pGVkttNUxvT0VCSE1nMEwwZW5LZG44RjN4Q2tZYndZQUxZVEU2N256dnFSX1RaaHhPLVBaMThabzlrYXpxQW5WOU5DUVc3RXFEa1NxNExsRDVyMktTZDVfQzdpNGswWFFhU1V3UWRvd0YzVTVjX25KZjlreEZGR1dPS1hhcnpVZ0E?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【特集】平和について「感じ・学び・伝え合う」広島研修旅行…明治学院 - 読売新聞オンライン</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE9hbVQxRmNQYkhlZ2t6ZXZoTlNSZkprSnVxSnlSWm12WHRUdUI3VDhjdUtidU8yTGhQVnh6NEFrcFg0T3BDSXhNQ2VyVl9Ra3dGM0Vmak4yVWN0QdIBXEFVX3lxTE1iNmdFdDRfNjEyN3NpR0g3NldOVHgtd2hnNnBoUm95ZnZnc01aNnRWUW11NjFlSkI1X09qSFpLd2hGd240d1FKQk5xQi1qcXVYNlFkRTc3N0dkZFI1?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島県内、国の「おこめ券」採用ゼロ　商品券や現金などの支援策　最高額は1人2万円分 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9LaU5rTjZlYVIxZFJBSW1MXzVJT3NUT21IdDRnaTJhb0phbEVwOHZHVkZsVjUwQVNKSFdiTkdJcnhIMVBJek1nRnZXckp5S3VTQUNuSVhvM25adUcwX1dvZ0xSckx2N00?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島市中心部にも「内回り・外回り」ルート 広島電鉄の「循環線」 来月28日から運行開始 - TBS NEWS DIG</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5FYzF3RjB4ZHhad3YwVGR3a0RoUExkSEg0Z1l2bHdxSXFiTFZiMzk5cFZLY294VlR5Y2hVNHcwZjQzTVZlTzBxbXFPSV9vNko5TElIVzhvOXlyZlJkX0pCVnh4NUJpRlJ1YllIMA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島電鉄、市中心部を回る新路線を3月28日開業 回遊性を向上 - 日本経済新聞</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569687?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日産 2年連続で巨額赤字の見通し</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569643?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">JR東 計10両で台車に16カ所ひび</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569664?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">アサヒGHD社長 障害巡る教訓語る</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569649?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">第一生命HD 情報持ち出し1155件</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569699?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">セブン おにぎりなど29品目値上げ</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569675?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PayPayが米国進出へ Visaと提携</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569666?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">五輪中継で気になるドローン 賛否</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569644?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">なぜ Windows標準メモ帳に脆弱性</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569524?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">セクストーション 被害防ぐには</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569520?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SNSで首相話題 識者が背景指摘</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569692?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相の3月訪韓浮上 シャトル外交</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569676?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">与党 委員長ポストの独占を要求</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569669?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「国家情報戦略」の初策定を検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569704?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">参院の立憲と公明 別会派で活動</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6569725?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中道・代表選挙 きょう投開票</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:20</p>
