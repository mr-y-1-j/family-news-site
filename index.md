# 🏡 Family Portal 11/24

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 58,711円 | USD: 159.17円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(227.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(210 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">7じ 35ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiUEFVX3lxTE9LaU9YSjhKNWVCZmpjSW4yNTN2eGxvYmE3SVpULXpiZVdkWWVUdVZwT0p2WnNseGk5LXQ4MXJTNmtsTXA2RFFBTEkzTVpzbWpN?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">2027シーズン キャッチフレーズ『DAHA』に決定！ - 広島東洋カープ公式サイト</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9BanhVN3ZNZWFGUnowMlhLSTQ0VWdPWVBaODZ6WEFJMk02cDJMWDBJcklVS0QxMEltd1VpWUlOWnozbnVCRWl6MGpaMUJfZ3NMd3BBa21vRWZZOXEtbk9pTVgzLS1aT0diMmVwWHV4OXhLLXNKcmpadlEyUWM0U2c?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【大学受験2027】2段階選抜73大学が予告、鳥取・広島大の医など厳格化…旺文社（リセマム） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiUEFVX3lxTE95VUFlWlFPdkZ5YXJjN29HU1FFWDNuNkpHekw5eWx6dEE1YUJZb052ZWxmV25ickx1RUxXNnc1VFpwRGhQVzlzd0FoNEdQczV3?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">河野 佳選手、支配下選手契約締結！ - 広島東洋カープ公式サイト</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMie0FVX3lxTFBZZ20yR3k5LWZvWC12S2puZl9vLWV5TG16RlAwSzJSX3dOU2dXZ05BMndOeFFJN0ZCNmFVQ0lQcHo4TkxIVXJqUGhWM0lvRm5XQTVibk5MUzRjZTdVbXhrZ00yd3Zzdm5XR3hiazdFaVVSX0ltSTRaOXltQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】河野佳と支配下選手契約「来年一軍で活躍できるよう頑張ります」 25年には戦力外も経験 - 日テレNEWS NNN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE83UFVuX1lRbEIzT0JTc2N5OWZzbE1fYU02bDc3UzB4OWtBVk95YldUSXlFSzdlMFpqVmcyOVhLS0FVbmJ4TGFuQ2FRSzlxOV9zX2lnM0NNaERWc1ZSRzJZWnhWR093eFhhc0FueUx4ZmlKa2xCMzlaMzhrVHRHSUE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島が二軍で投手三冠に輝いた広陵出身右腕の支配下復帰を発表！支配下は66人に（高校野球ドットコム） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603771?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日経平均 一時2800円超値上がり</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603732?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">フアン氏 エヌビディアCEOに復帰</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603780?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">松屋の一人負け? 牛丼業界で明暗</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603792?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">くら寿司22品値上げ 34品値下げ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603777?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">セカストが急成長 人気の要因は</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603779?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">バザールでござーる サイト終了へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603699?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">タッチ決済改札 利用者が戸惑いも</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603626?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">攻撃急増 背景にセキュリティ軽視</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603588?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">タワーレコード 1100万件情報流出</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603568?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">リーマン予想 AI証明巡り共同声明</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603783?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">野党 文科相への問責案提出で一致</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603766?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">文科相 自宅家賃を政治資金で支出</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603742?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">3文書改定 経済安保の概要案判明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603770?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">立憲 最大5万円給付案を参院提出</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603791?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">辺野古事故受け7割が校外活動点検</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 14:40</p>
