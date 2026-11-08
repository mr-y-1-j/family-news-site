# 🏡 Family Portal 11/08

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 57,435円 | USD: 158.43円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(162.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(150 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">5じ 25ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5Hby1JbThzMVBtWWNhb1o2VkctRXRlSTBGUktaNnREWXFvNlJsRlRXS3ByZkFQMi1BRHRjclNrU0toZG8zY25fQzZnc01oUVVmOVg3OC1Dek83UQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【火事】広島市中区のマンションから出火 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE05RjQ3bXVYdjZrREhJQU92bU5xVHN5RDVzdUY2bjlaSHVHcFhKbDl6TTh4NXhIRGdxVFFmUXdBMnNSQW5MTW1tR0FvUmZJQmtobTV1WjVPWGdrWUZhd0JuN21EdWNrV1ZQamZ1cldZUHY5UnZpUm9xa2lXZDBBRU0?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">SNSで「警察車両が幅寄せ」動画が拡散…警察官に“反則切符”「進路変更の禁止」で 広島県警（RCC中国放送） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMihgFBVV95cUxQR2JhbTFSV2laUzVDSjhBSnZWcXBjU2pYZ2s5SmducXNXam5MQXR5ZUV5Rzl5ai1xZ0JENHBnR0hHRlpiM0NJOFVkd0k1STlyZ09JOElyOEVWTkQ0TGxYSFlaT0FkTHotNmJHb2JJTDFTbVFtUFNYYzV0X0lSNlUtcnRWYk1aZw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">きょう広島決勝が11時45分キックオフ 広島皆実vs如水館（高校サッカードットコム） - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiS0FVX3lxTE5rU3FEcTdEdDFwZGpnVzNzZ1dwbk5RTjRLN096ZTA4dlc2aXpoUmhCeDNlbU9oSkd0MGhBcEFEaUFrMVVHbTFuRGtxYw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">鳥取市で震度2、福山市や広島県府中町で震度１ - 47NEWS</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE9GWVpMZ3FuVGI1QVZsT3RFY0dkQlJiNFEzT2ltQ0g2TEIyNkNTSHRRaFNsVDRYZHdLVGRqUTZnenVfdk1ubUZGaUpPRXd4T18xNk93MVRIVDI2UQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">女性監禁疑い、広島の男逮捕 - 中国新聞デジタル</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601744?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">東北新幹線運転再開 ダイヤは乱れ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601728?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">東海道新幹線 地震で最大60分遅れ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601614?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">テスラ サイバートラック生産縮小</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601643?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">スーパーの衣料品売れない? 今後</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601656?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">購買力高い大学生 なぜ存在する</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601743?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「なりすまし電話」巧妙化 対策は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601694?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO謝罪会見なぜ炎上 プロ解説</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601670?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ブッダボット 仏教界でAI活用模索</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601651?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">東大野球部 独自のAIで打球予測</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601649?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SNS中傷 スポーツ・芸能界の対策</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601719?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">愛知県で震度5強 津波の心配なし</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601737?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">あす都心11℃予想 12月下旬並み</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601734?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">互いに譲らず 冷え切った日中関係</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601705?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「継戦能力」強化を明記 政府検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601664?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自民 採決前退席の4氏に説明要求</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 09:57</p>
