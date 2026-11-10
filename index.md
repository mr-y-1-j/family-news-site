# 🏡 Family Portal 11/10

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 60,081円 | USD: 157.93円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(192.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(150 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">6じ 25ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5RcVR2QU41QjdKWnNEcFMwcldmWnBGaVBxOThieFVWQ3hybkdsWkNzbTI4UUxTOElqbTlOcGlJbjNXay1NaldOS2t0d1pNZmtCN211VGFldnNSMjdsSFo1eXN5X29LekJuTHE1VnRMal9seGx2V2RaSE41dE5vYUE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「カープあたりなんかなって想像してるけど…」トライアウト不参加組にファン熱視線 中日3年で戦力外の25歳内野手に「二遊間守れて、右打ちの選手は貴重」（CoCoKARAnext） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMigwFBVV95cUxQT0dUemxyQUV5bHhZOE9CS1h0VXQtYktZTGhOQmpWdWVnS3kyaGN2eGlxVjkxeGMwYWJHZ1R2RkNXMUN0cHhERWxWY3BiOHhhLXM0ZzRtQk9DdlZ3M2RyWldZd1ZJdHh3U3pEc3NIcGQ5SXdub2R5R0QxMDJiNGdlSUtaRQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ＳＴＵ４８が１日店長 ファミリーマート地域密着企画 広島（広島ホームテレビ） - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBFUlJUc2VUeXpqQ2o1MlRaZDB1VFhrUUFoNW82dGZxOUM3ak1OZWxKd1ZqVklLRlgwWGhNb0dlQThhTDFsVDdPQlVmNXBxMFVmSVRhdng0SXdhdTZqU0hjNlJ0UnN6eFg1NElqWTRrdGhWcVUxZU1PWmhYUElKZGM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】球団史上初のＦＡ補強なるか 楽天・太田光を獲得調査 広陵出身の強肩捕手 １１日の交渉解禁に備えて準備 - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE55Q2UwWkdPRHdtN3FCd1Zvb254V2FHSEZMS0RlcFo3b2ZDRWJoaXV3TlJhOW5NVlZURnRuUWRqNW9FVy1UcU1oMU14TFVfcEdraExWckJ0UXdWU0pJWnd6VkN4U0VvaURQU0ZzdjBUczJJUTJ0eWtkRVc0dGl6SEE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】国内ＦＡ権行使の楽天・太田光を獲得調査…球団首脳が明言「キャリアのある捕手が必要。現場からの声もあった」ＦＡ選手獲得なら球団史上初（スポーツ報知） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE84VXl0TExZeGl4NjJnRDdwYWtMRjRfZVBWc2ZLNjZZNi1YUGQ1US1ib054NlJmSHd1REthUXQxeW5ISVVJUjFDc2U3QU9VYVJKQy1zMTRUTE5kdDFJOFhBQUFDRk5uOFAx?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島がＦＡ権行使の楽天・太田光捕手を獲得調査へ、今季１００試合に出場…「うちにフィットする」と球団首脳 - 読売新聞</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601981?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">個人向け国債人気 発行額8兆円超</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601998?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ホンダ 米オハイオ州に工場新設へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601959?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">麻生コンクリ JIS認証取り消し</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601941?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">NTT 保有するNEC全株売却を発表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601985?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">火葬料 公営と民間で大きな差</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602006?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ホワイトハッカー 学生なぜ目指す</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601969?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">VRで美少女化 30代男性の苦悩</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601958?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">IPOに向けた準備に着手 サカナAI</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601943?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">NTTなど5社 衛星連携へ協業検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601934?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ニトリ 最大3762万件の情報流出か</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601996?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">石破氏ら戒告の自民 引き締め躍起</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601954?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">石破氏 戒告処分厳粛に受け止め</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601976?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">石破前首相ら戒告処分 参院側不満</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601979?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自衛官定員削減 安保3文書明記へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601992?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「国内間通信」も監視対象に 検討</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 12:52</p>
