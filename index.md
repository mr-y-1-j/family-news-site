# 🏡 Family Portal 11/25

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 57,108円 | USD: 159.30円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(122.49999999999999 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(30 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">4じ 5ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9OV0pOMGN5UTRmN1AtLVpPZTJUbFU3SV90N1YzdHQyTUx4enpwUXU4blNPdmtVODQwX2NYRzhXSTBvN2M0RUFqTDNpSEdQbXBSYWVaeW9XWUNxMTlMcnMw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 庄原 高齢女性強盗殺人事件 逮捕の男 配送業務で土地勘か - NHKニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE8zNmxzVEQ1RHV0ak05NlJPZmNNdGFUcmNaME1mdnJJWFdER1ZYYzlQNFRQNXo5WERSdkM2WEVwOFo1N3FEQjQxX3o4aUVKN29DSUZkbnFhYm9fUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">庄原市東城殺人事件、東広島の配送業社員を強盗殺人容疑で逮捕【県警の記者会見詳報あり】 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5WOTdBZlBlTk9pelNYOE5nSnMyWkJUN012ZUQyc3VmTEhpeHRVYnhkUjhLWWg3WFVlSUdiTHhqaGE4RjlPdjRiSER2cjR3dVVYT05CTlBiNE5DdHhvQnNWazFYcVVYdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・庄原の高齢女性殺害事件、配送会社員の男を強盗殺人などの容疑で逮捕…「殺意はなかった」と一部否認 - 読売新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1mc1J3M0dLZkloeFZaY2EzWDNxS19oY041UVpQNVQ3VUo0bnB5SVVQNDFtQWFNWDNmS0RaSmVMeV96aHhISHNSTEtYemRBNlZrSFVCMVZ0M185TjFibUFZYUVlVTBraGNLY2ZFUmlJUUZGR2pEWGtXV0ZKOXBnZnM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島、杉原と育成再契約「より一層頑張らなければ」（ベースボールキング） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMie0FVX3lxTE9rWTFmdDVGdEZoTGctNTBOQVNvdkZ1NjRaUzJpQmtINUJnWnpQci1hVWdqb0JPZk0wRlRHVnk5NVdEUHhEOGJDVUc5WTR1OEZhRGpEWXBxNm9CcWVkYnViVkI0Ty1NZ2RQdUtXc1ExWnBieG1rVE9Zb1pWYw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】杉原望来と育成再契約「もう1年チャンスをいただけて、より一層頑張らなければいけない」 - 日テレNEWS NNN</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603901?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日経平均 一時2000円超値下がり</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603828?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">個人消費判断 約3年ぶり下方修正</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603877?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">フアン氏 エヌビディア社員に謝罪</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603897?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">くら寿司 値上げ・値下げ同時なぜ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603878?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">新型ウォークマン 歴代最高65万円</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603903?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Microsoft 障害受けコードレッド</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603882?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AI登場「創造性」問い直す機会に</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603825?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">京王グループ 約1063万件漏えいか</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603807?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ヴェレダ クレカ4万件超漏えいか</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603814?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Z世代トレンド 大賞「ドパガキ」</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603895?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">週後半は気温上昇予想 寒暖差注意</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603860?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">副首都 来年秋に複数同時に指定</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603841?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">支援金「最大年27万円」の給付案</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603876?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相が文科相擁護 辞任ドミノ懸念</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603868?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米中に次ぐAI国家確立へ 政府案</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 13:39</p>
