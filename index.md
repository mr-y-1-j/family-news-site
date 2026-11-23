# 🏡 Family Portal 11/23

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 56,437円 | USD: 158.93円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(185.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(60 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">6じ 10ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE53MHJyVFNSMFdwVV9VMVdhMmtLLUo2d1NGY1h6Y3FuV1R3Mm9iYl9zdV9kSFBrTkNkT3FNdjhVY0Z6MHFHbWNLNUEwZkhGM245bFM5dGpvd0NYZw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">山陽道の通行止め解除、 広島―広島東の上り線 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxOZUpxeUFYWVJsNlFjQ0FtWmRsTXJZRFBpMHY0dzZyWTJTWV9GOGphU3NCS3ZJUm0xd2luRmxUdjJiS0EyQ0JBLXVESVdERC1WcWozTkxFY2xYMzVKanY5NzhuUFJqMGF0WGZFS0FSMm9zZ2c3VTdUa3RuVlNudHFLSEx3RUo5R1E?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島で初雪を観測 西日本で今シーズン初（2026年11月20日掲載）｜広テレ！NEWS NNN - 日テレNEWS NNN</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5mZDNaWXlTMHVtd0NSdEk4R0RwMWxnVWFTV2k1VDFVcWhacTNJWVNDdEF6V1UxRFZsV0hMVFA4QW82cHZnVXV5T1Y5T3dpOGxtLVlHczhDWHRaRGFaNExMTEoxc09DQmFWTERzaUtHdVpPTlBzSnFzbU5VT3dWd3c?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">三原則例外「言語道断」 広島の被爆者が批判（共同通信） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiV0FVX3lxTFBoTFFoRi1UX2h3SUMwa0p3a2Q0bzNxaklWU1ExMUZGZUNrZnFXZnVzQlMyRGFYaFlCVjEzMFBwMTdEOHRkMUxKUDBjSkhmTFNQZW5DR2dkbw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">記者会見する広島県原爆被害者団体協議会理事長の原田浩さん（左）と広島被爆者団体連絡会議の田中聡司事務局長（右）＝22日午後、広島市 - 三原則例外「言語道断」 広島の被爆者が批判 - 写真・画像(1/1) - 西日本新聞me</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE9WMjFVdy1vY2FBRENwdlNGcmM1SHNWTVQ1RThJSmVadUJhQ0swMVZfRUQ0WHh0VlE2ZnRFWW9PLTE3eV83U3hocjhLYkVSNU9Rd254M3JhTnZPdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">三原則例外「言語道断」 広島の被爆者が批判 - 北海道新聞デジタル</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603628?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">SOS見せず突然退職 企業どう防ぐ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603609?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">アンソロピックIPO巡り銀行に制約</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603591?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「サイバー保険」に加入 企業増加</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603509?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">地方銀行再編 各地でくすぶる火種</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603620?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">24年の1億円超所得者 10年で倍増</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603626?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">攻撃急増 背景にセキュリティ軽視</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603588?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">タワーレコード 1100万件情報流出</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603568?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">リーマン予想 AI証明巡り共同声明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603398?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AIでリーマン予想証明か 精査続く</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603531?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">既婚者専用マッチングアプリ 実態</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603632?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相の国会出席削減 自民が議論</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603622?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">連休最終日 西-東日本は行楽日和</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603638?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">野党 文科相の「問責」提出の構え</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603601?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">文科相の「交代示唆」木原氏否定</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603563?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">益永死刑囚が死亡 連続企業爆破</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 11:03</p>
