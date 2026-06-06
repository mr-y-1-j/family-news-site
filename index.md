# 🏡 Family Portal 06/07

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 天気不明</span>
  <span>📈 日経: 66,588円 | USD: 160.29円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(282.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(150 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">9じ 25ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE90ZGQ0bVlsTmVDaHB1MDRESngtQkUyUmZzTGpfeTBuaWlRTXU3aDFKZllkcm9NQ1VUN2JWN0x6SGJmeGQtSTdhckE2TXhKVHhfNGtaQ25CaHhDUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">森保一監督が慕う広島市の焼き肉店 亡くなったオーナーの次男、ワールドカップに期待 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiUEFVX3lxTE9idkRkNjdOQk9Xa20wM240eEJEMDdCX0FWd3pBU3A5VVB2MVVHZDRrT2RfNlRCYjY3UDlqRkwzYnZ0Ul9SNVoxZHdybmU0c2t6?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">日本生命セ・パ交流戦 振替試合のご案内 - 広島東洋カープ公式サイト</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE1HcjNaZTlBanEzM0RIcWdKUFhPY0l2SkxPblZ5TWd4eVYxX2pxX0NFeTFueFJZdXR0c1VnWXhSVWtJQXRKLWpCZjBraDd1LUlXZDBmaXVuaEFJMDQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【現地レポ】約160店舗が集結！広島ゲートパークの大型マルシェに多くの人出 - 旅やか広島</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiXkFVX3lxTE9fWHhrYTJhU2hrZmN5aEpZZFY2bmI1WGNBVXRraDhxdlR5TnJDR1pjVUV4anFnWDVGZjhjU1dSQXZON2s5TEdxTk5rRkQxbXNWTzFuLUE4YWtVZU1BVkE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【公式】川崎Ｆvs広島の試合結果・データ（明治安田Ｊ１百年構想リーグ：2026年6月6日）：Ｊリーグ公式サイト（J.LEAGUE.jp） - jleague.jp</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMickFVX3lxTE1YWElWOFkyWkZsdnhWYTdxekh3S0JZT2p4anV3OWJFbXBoOFNOYXZNeW42UTNLTUkxYXN4N0FyM2FVS05XV1VhVDljZXBWeTExeUpZRkdEeExFS2liMlZFUWljb1BCLXNTeUxkM3FJajdVdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">川崎F vs 広島 : プレーオフラウンド 第2戦 (7-8位決定戦) 【明治安田J1百年構想リーグ】 - ABEMA</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583222?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">世界の原油在庫が急減 相場急騰も</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583177?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">外国人の起業 法改正後に4割減か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583201?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">レアメタルが調達難 中国輸出規制</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583237?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">豪産小麦が収穫減へ うどん影響か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583249?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">葬儀社との料金トラブル 多発</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583214?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Switch2「転売屋」利する格好に</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583127?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">マイナちゃん巡り 担当相が説明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583068?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日立 ミュトスへのアクセス権取得</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583063?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Grokでビキニ写真 英議員が提訴</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583003?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米AI計画に日本が800億円拠出へ</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583242?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">鹿児島と宮崎 線状降水帯発生恐れ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583227?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「飛鳥・藤原」地元たゆまぬ努力</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583193?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">都構想挑戦 吉村氏連立入りで決断</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583212?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">平岡秀夫元法相 中道離党を表明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6583230?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">国旗寄せ書きは? 損壊罪対象外例</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:53</p>
