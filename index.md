# 🏡 Family Portal 11/03

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 63,082円 | USD: 157.90円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(130.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(120 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">4じ 20ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFB1b0RkbFNOOWpXemlwamZKX2tPQXY3ZFZEekhvQ2hyZC15eGkydURRaXgycWYzb0xoOWpXQnJVWFN1VGFVaGRsS2ctR1IzanZPLTJqak5PajlkZw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">東広島のマイクロン工事、大量バス送迎スタート ラッシュ避けて建設従業員を運ぶ - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1fb3d2NHM4NXQxdGZlS1p5VlNDUmJ4anJ2c1ZYaUE4bzhYWTgwdUhBcGVla1p6REh5ZHliaUo3eWVHMDNuNGlZSXZZdGlweTl0ZWhRTGtkdUZxSXh0Skp4eWlMeHB4N2luaDFBWXJsSVdVV0RQVWZneUNFV0VKbWc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】超異例のコーチ転身！新井監督付広報の松本高明氏が内野守備走塁を担当 緒方＆佐々岡政権時も監督付を務める １４年に現役引退（スポーツ報知） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiakFVX3lxTE5iWHVHTW9xN1JiWEpZd3ZTQkROcm9ZcllNWGtLeGpXNll5djhhek1xYzhHRXQ1Mnl1ZXI0TG1MWkw3NG9zZG1YSHRmb3dXUmZRb05vTnpDNXZZTTdHdkt0SEozM2lJUzVYVXc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島空港の到着口に「福山の熱」を。松原組×福山シティFC×びんご福山デニックス、国内線到着バゲージクレームにコラボ広告を掲出 - PR TIMES</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE44UndiQjFzcVBITkw1QlFJUHlGMWlLcnc1VmNYU1h6dGNsaFBaRUp5UDFtTWFCMkd0SC01bGJrWDVybGJwVFcxcjhaNmpfSnN3OTU0QlFyNVluZnN3Q05yb056WlBmSm9vZ1BkcFZfT2hKTUpRb0xrUTZzOXNSRDA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島が異例人事！松本高明氏が監督付広報からコーチ転身 新井監督に「僕の方から自分でいいのか」と質問「驚きもあり責任を感じている」（デイリースポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9la2dSNWwtWndab1VOSXlpYm1RLWZxbEMzdENyZnMwSVdHa3JNQnRlSXNqTkpITWdwbzU4QzV1MmRxZEZoWlptZHFPUVBrQ0ZSZmhQM3k1azNYbmhDQm1Vd3ZmUTctS1E3M0dVMGE3SmVDMTExWEFPdDlFaHp1Wms?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島県産カキの水揚げ始まる 例年より1か月遅く - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601082?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO熊谷社長ら 報酬を3カ月減額</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601048?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">フラット35 金利3.81%で過去2番目</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601077?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SBIとフジHDが資本業務提携 発表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601141?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">安いもやし限界 5年で13社消える</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601135?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">子どものセルフレジ操作 SNS賛否</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601134?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米アップルiPhone好調で増収増益</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601127?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">欧州店舗にサイバー攻撃 食品廃棄</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601132?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO 侵入から2カ月なぜ気付かず</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601115?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO会見で「命の砂時計」 意味</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601107?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMOが謝罪 利用者「響かない」</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601124?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">公布80年 初改正へ改憲派前のめり</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601117?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">転換期の憲法論議 発議見通せず</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601133?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">トランプ政権に「共感」日本で23%</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601113?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">医療インバウンド 厚労省が検証へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601090?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO攻撃 警視庁が捜査本部設置</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 12:07</p>
