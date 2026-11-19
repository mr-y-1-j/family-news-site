# 🏡 Family Portal 11/19

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 59,141円 | USD: 159.45円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(155.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(60 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">5じ 10ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE85TGc4UjhYMG9CMHRZbmhtcTFtUWNpQUJzazJSb1B5d1VrQkdRdFdiUmp3QzlOUkpDLXlzLUdLTDlRNkVjTXhTTWoxOUF4a0JSWVFfSUp3MEFpdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">JR広島駅近くの「開かずの踏切」廃止へ 人の取り残し解消、車は横断不可に - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1mSVlxRERJVmZkNDQ5cllVSWtMQ2lfU0tvdHlUYV9RUnZycThOY2UtNElVU1RUUTRUZ0VhRGxGRjBRckV3SDd4T1RxanExRGJELXVhb0FKVDU2Zw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島県の新病院建設計画、概算工事費が929億円に ゼネコンのフジタなど提示 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9Gd0U0V3VYNXJObnlfU1hsQTFlQ3R1Wk83NmloS0h4clA5ekFEdmF2SDV4YTRtTnh1VGlPOWtXLVRzS2k5eDlUY0NqUkN3dXRBQkVTbkV1YW1lWkFzeXo3SEZmRGRDU1hsSFBOencwOUQxRXpwNURCRm0ybnE5ME0?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】東浜巨が入団会見 背番号は１２「いい番号を用意していただいた」先発ローテ候補として期待…ソフトバンクから無償トレードで加入（スポーツ報知） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1qWUxqZjd1eWc4SGZIRUl3SjY2ekxsR2RIbmJmYjZxWHpzOVJwNU9obUVtQk9kSE1jNkJ0U21VbHZXU3JCN1FDOFZ5NkRFWGRRMlprM2Y1b09FVmJNSm9BLW4tcVZlaUw2Y19seDQyYVVrNmxCVUdCOGdqbzdYcmc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島空港の再整備事業、国際線がより快適に…到着ロビーを国内線と一体化「選ばれる空港を目指す」（読売新聞オンライン） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1TNzVzUU9pRlZUZXN1MFhXUTdHR1A1dzZoMGNBTFdFaGNXck83bjFVMWFwRV9tTjNGdWRPS1F5R1NNOGhEeThCejB0cDd5bms4M3U3VXNxOEJXZw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">東広島の山陽道で大型トラック焼く 西条IC―高屋JCT間上り線で通行止め - 中国新聞デジタル</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603047?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日本車の部品 一部共通化する方針</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603078?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SA・PAのゴミ箱 280カ所で廃止へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603054?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Suica「紫のうさぎ」得票率51.7%</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603124?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">賃上げより手取り増 食事補助注目</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603046?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Suica新キャラ A案とC案も活用へ</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603112?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サーバーソフト「nginx」に脆弱性</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603058?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">DHC 顧客氏名など1911万件漏えい</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603117?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Anthropic IPO公開価格は83ドル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603062?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">顧客情報漏えいか 楽天証券が説明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603030?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">楽天証券 情報漏えいの確認方法</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603109?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">21日にかけ風強まる 暴風など警戒</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603096?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相 プーチン大統領と30分対話</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603135?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日露首脳対話 関係改善の道険しく</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603099?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">防衛費財務省案 自民内で異論噴出</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603076?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">支援金 対象年収下限「56万円」案</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 11:52</p>
