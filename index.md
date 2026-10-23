# 🏡 Family Portal 10/23

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 62,908円 | USD: 156.20円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(90.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(0 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">3じ 0ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBiOU1zT0k5M2pURXQzam1TcVd6M0tQaVFqN2ZUNUhFaXV0M211RmY4NGhVQlBxa0FEWDRhMkw2NzRPcnVlbk5yd1BTemZ4SHl5VS1wS3RSNkZwMXNjSWZWX3pQbm5KVXh2dEx2Yjh1WlhDMXQ1U04zczZNTEVJZ2s?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【ドラフト】「笑顔でよかった……」 広島1位指名、山里宝の反応にファン安ど 「大事に育ててやってくれえの」 - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9qRTV2ZjhSZ0FVcGlRenlUbWZzVVBOTkZRSjNVSlRUdXFKRi1GcmlIaGVXQ0EweTUzcHBXeDBjbWIxS3JjdGpDY19fUG1GdXdWMk5ON05Fb015MUNLLVlWR3VOTkFMUlFiamlwWlloZS16ZmNaZXJpYzhleVJLalU?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【ドラフト】広島新井監督「是が非でも欲しいと」即戦力遊撃手１位指名「危機感」松田オーナー（日刊スポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBfYmtzRlVtSzBIYUxILVZOaVktV2FicmZWT09LOVlCNm9MTzVVel80V0tncTU1NENtWHpZWkpsQzhBeEFXLS1IaW1DMm9GRjdXdFhJa3VLb3F5aDdnYXBOVnJBX3o0dXJDWXZzZjJPQlM2NWxwWDRicjBFQXlGWWc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 球団初の高校生指名ゼロ 松田オーナー「バッチリ。狙い通りでホッとしている」田村スカウト部長「即戦力に近い選手」 - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFA5TjlCMzJfM1hqQTBwTmNtSTJPZDRDX3RRaVg2ZnMtVmJ0MW9XMWlCVjBUVnhCV3FNUDRTcU9WUmdqUG9wRU51bGR3Nkd3YTJGc2ktZzhFamZFZGk4ODdYcVE1TnNhQWJmNXItdFBuSEt4SWN2cnVQOXQ5eVlVSU0?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">そごう広島店 コスメフロアが23日にリニューアルオープン（2026年10月22日掲載） - 日テレNEWS NNN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1OZk1xWHkzTUJYSmJMZi1FejlseC03Y0F0SE9lRlBhYnp6YjRzUmw1WDVKSjZzNzg0Q21RU2s0TU9nYmgtUnUtSnBkTXVubEZqSERMUmJtVVNCcFBPZ20zMWFVa1VaY0RqLUhWSVJCNkN2amhWZXdJQjBwM0kxcFE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">そごう広島店が化粧品売り場を刷新 「顧客起点がすべて」（FASHIONSNAP） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599772?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「PHP」暮らし直撃 徹夜の社員も</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599679?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PHP巡り 企業など対応に追われる</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599768?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">食料品消費税1% 買い物は変わるか</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599762?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ANAが追加出資検討 中堅航空2社</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599759?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大成建設・鹿島 国交省が処分方針</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599763?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">デジ庁HPの問い合わせ内容漏洩か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599733?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">漢字検定X「祭」の漢字間違える</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599728?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PHP巡り一般ユーザーは対策必要?</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599702?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PHP脆弱性悪用の試み増 数百万件</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599674?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PHPの脆弱性 10年以上発見されず</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599757?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">台風30号が先島諸島接近へ 警戒を</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599724?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">発足1年の高市政権 麻生氏が評価</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599683?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PHP問題 政府機関の被害報告なし</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599693?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市氏 自民内から再選支持相次ぐ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599765?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">生活保護利用者の車保有 緩和検討</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 09:13</p>
