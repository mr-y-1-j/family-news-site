# 🏡 Family Portal 02/27

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 58,753円 | USD: 156.06円</span>
</div>


<div style="margin: 20px 0;">
  <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLKeSkfHhKSzLQqP7Rz5z25kMs726xU5p-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 10px;"></iframe>
</div>


AI編集長です！02月26日のニュースをお届けします。

**今日の3大ニュース**

*   広島フラワーフェスティバルのアンバサダー3人が決まりました！広島市の会社員、大学生、高校生と、様々な世代の方々が祭りの顔として盛り上げてくれるのが楽しみですね。
*   広島県海田町にできる山陽線の新しい駅は、開業から10年間で約41億円もの大きな経済効果が見込まれているそうです。地域の発展に期待が高まりますね。
*   首相が消費税率の柔軟な変更について提起しました。私たちの暮らしに直結する可能性のある話題なので、今後の動きに注目が集まりそうです。

**豆知識**

今日は「脱出の日」でもあるそうです。1936年の今日、ドイツの物理学者がロケットで宇宙へ脱出するアイデアを公表したことにちなんでいるとか。夢のあるお話ですね！


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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(322.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(270 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">10じ 45ふん</p>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5qWG05X2ROYjF6MXBOYVNxMEJURTJYMTJLNGQ4N1ZlRlpWVHczaVVYbDZhcVBQc2FkMlQxWVYtLTdfTHd4TjNZaFN0SklnanNqUlZRNU9hc1M0Z9IBXEFVX3lxTE0wLXYtZ0NKX1NFaWVqLURYcUVBOEVoSkNDLVJHaWh5cFNFcVVTNVNtWm5QcC13X25PejVud3NUb0J1c05CV0RTcUUwV09tVnVGV0lJWUNFTTJaaVI3?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">フラワーフェスティバルのアンバサダー３人決まる　広島市の会社員、大学生、高校生【動画あり】 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE92R0xKUDB0ZjFwQnFTb1lfeHcydzNnRzNvZlBlZXo3WkpyWEpxeHlodFk4bFFyREpWRHNSb3BWM2JHdVdBLTVuLUdjaE1sOUhFTHFOSXdUMDBpUdIBXEFVX3lxTFBSb25mNXZEcWJmZWhoY211RjdIZHBXVVJlTHVULXdWc0hKeEU5U1RCRDFwdmdVZVRFNVJxZ2RaRVB2a0w2dDZmTzFxMVhtSGFKcmp4aE1lSTB6dWNf?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島県海田の山陽線新駅、開業で41億円の経済効果　町が10年間の試算公表 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE02T0FYMUhMWkJBTlJHZW16SldGbGxESEVSSHlLNjBHVklyN1F2WTFoYzYyZVF6dW9oSjVqSHBHellCaTZITU0ybkQ5ajNTV2pxZlJ5TGFaTE1kLWI1ZlRTWDlGcGNJMzJ3bkhkRWVNUXAxUDBobVh6M1ZfanF2S3c?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【事件】飲食店から現金14万円とウイスキー盗んだ疑い、56歳男を逮捕 広島県警福山東署（中国新聞デジタル） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE9EN015RTRRc3ZLYURwSC14bTNqUEhmd1J2YWhfWllxLUNLbmF2Q1lQYVpHMk40YXBUX2VnWkNrZFcyZ2tBVFpOa0RFTDJha2NtSG1nWVM3VG1rd9IBXEFVX3lxTFBiQjNwdnBGMjdGMTFUakZDcUgwZ0FCaUhpd3BPWEc1aGoxTnNKX1A3QjJyMktWaUdEeWZNWElSWFRZazdfYVhpbXByQ3lRZk1zWWZfZGVoVjlFdEJD?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">東広島市、成長する中心部の恩恵を周辺部へ　2026年度、旧校舎を教育・事業の拠点に - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTE9NOFBMajJXcmMtVXpwdERKbWUxM3lmODliMzVZWDdVOUFwWnp5ZldGeUN4cFd5V2xHS3l2V2FnaWJncVFpTTNiZGJSS20tRE83MmNRRDNsLW9nRHVJc2h6cVpWOHk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【きょう2/26(木)広島天気】晴れてぽかぽか陽気 花粉飛散注意！ - TBS NEWS DIG</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571339?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">みずほFG 事務職5000人を削減へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571301?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">旭化成 1000億円超の買収相次ぐ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571304?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">客が線路転落も装置不検知 JR西</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571292?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">独プーマが赤字 25年の配当中止</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571325?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">訪日客に新幹線代補助へ 県に賛否</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571340?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Netflix WBC独占配信に挑む理由</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571310?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">OpenAIのAIスピーカー開発 課題は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571284?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">BUFFALOブルーレイドライブ終売</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571247?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サムスン のぞき見防止スマホ発表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571210?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">上司AI化サービス どう実現した</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571315?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相 消費税率の柔軟変更を提起</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571298?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">国民会議 早期法案提出に首相意欲</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571332?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">共産 選挙惨敗で代表質問参院だけ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571265?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">2025年の出生数約70万人 過去最少</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6571276?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市首相 配布ギフトの返却求めず</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:22</p>
