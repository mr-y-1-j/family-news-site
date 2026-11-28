# 🏡 Family Portal 11/28

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 58,711円 | USD: 159.28円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(232.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(270 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">7じ 45ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMihgFBVV95cUxQWHlISmhYWU1uT2hGTVhDRzA4MVg3d2w3eEQ2bHZyLV94SEEyN19hbVpKdVA4YU5PUjdlV3Q3R0hnNTQwSTNHcmxCSnJRbDNvNGozbXdtc0wzZXl5QzhOU0dLdnhKOG51OEFidU9oQXpDWGYyU2haZzVXVjZHUUN5OGZhLW10dw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">元広島の田村俊介選手、オイシックス新潟へ 「謙虚に全力でプレー」 [新潟県] [広島（広島東洋カープ）] - 朝日新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE4tekRrZGxZNnpRckZoNmY2d1hSa2d1WUR3bzUzRmgtMkh6MUpqTlRvdUEzSW42M21Ec1dfekRpRVBfS0MwS2VDb2FQVXFFbVpWZEZVem5VWVVieWtQOC05eE1hWQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">第51回広島県民スポーツ大会 空手道競技スポーツ少年団の部 結果 - JKFan NEWS International</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1zai1DQlFXU2hSc29hdkU5TVN4WWlBYUM5Q2UyZWRtQnZXNzUyRnhZdWM1eWhIOE1leWdZWWJneEtTYXdYNWlrbG45RzJGcGxFazBmX1BtUUpFVmpvVndCdUtpbVFqanhBNTJCOF9QMHhMZWlEVHV6NWZxdjZRamc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】国内ＦＡ権行使の坂倉将吾、条件面は「全てでもない」…地元・ロッテ＆西武が条件提示 宣言残留も可能「そろそろしっかり決めたい」（スポーツ報知） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE82MTdQM01BcXhLemNkVzUzM2FsYXFFczhER0xPWWtJWVE1R19DeTJUZTJIdGtrdW4zYXBsV0lRX3RoZWkwemNWTllVT1lQcklZMlN4RVNvUnE4ckRaVURPTm93?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】国内ＦＡ権行使の床田寛樹「まだです」今後も交渉の予定あり 中日が獲得に乗り出す 宣言残留も可能 - スポーツ報知</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiR0FVX3lxTFBDVExBekVWcnhLeG01b1Fld1lwVnA5NnNRMGFyRjNEbEIxZ2FWNVhLbmRLTU1qYXdyX2Q2Q1EtbEVRLWs3azJr?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 森下ＦＡ「答え出したいけど悩んでいる部分がある」坂倉は「そろそろしっかり決めたい気持ち」近日中決断へ - スポーツブル</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604237?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米ネトフリ 日本作品への投資拡大</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604216?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO サイバー攻撃防ぐ構想発表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604276?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">疲弊する管理職 重荷を下ろす制度</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604282?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">美容クリーム誤認表示疑い 返金へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604277?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">南海フェリー 撤退回避の壁高く</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604215?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">マイナアプリ 旧Ver.に脆弱性</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604165?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AIの果実を国民へ 米台韓で動き</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604146?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「ひとり情シス」役場職員の不安</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604193?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">新INFOBAR 日本の若者に刺さるか</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604140?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">実刑判決 AIとの会話履歴が証拠に</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604258?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">文科相の問責案否決 火種消えず</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604266?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">基礎控除上乗せ見直し 先送り方針</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604259?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">政治資金パーティーの収入 37%増</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604244?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">関氏18年食事会で300万円収入計上</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6604269?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">気温変化 暖かい雨から冷たい雨へ</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 12:37</p>
