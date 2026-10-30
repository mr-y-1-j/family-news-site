# 🏡 Family Portal 10/30

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 雨</span>
  <span>📈 日経: 63,034円 | USD: 157.41円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(330.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(0 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">11じ 0ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE0yRzlrTTllUlhfR2hseVc5QzJPRmpjSVY4VjVvY3d5Q19vamstQWUwUU5sYWpUbDdWR3F6dWhqU3UzSFEtS2pmeXE3b2g4bGtVaUg5cmxYTnltQi1qa3hWYmVGVFlhT2VEMGN3dnpoQU9OZUg1ajM1OUNlYTJVbkE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・床田寛樹は“男気”残留か「残るっしょ？」FA権取得の先輩投手２人への“引き留め工作”がブーメランに（週刊女性PRIME） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiUEFVX3lxTE1fVF9RREtTdUFTYzF3NV9HMVVaUVhXaUtGeEhkaTE4WllWVTczcHdXblFXNVRiYlpmNUxEMGwzTDVTM1hPekRabXg4dU8wSWN5?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">小川淳司氏 編成担当就任記者会見！ - 広島東洋カープ公式サイト</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxOTGRMMnl3aFNzaTAyaFcxRmhNekFGaFI4Tk9IUnBaM25laGRrNXByTDgybTZseVpwbWplLUVIOEROT2VkQmNyWjE0NTcxRTlUczMxdTM3aUpRRDYyWFB6aFJBYkdWNmJtcW5XaUhvemstUHNxNlV6cGZKbWtvdXhmOdIBhgFBVV95cUxNUjNRRUVMeHowSk5XTDhJZmRsbnJQcnp2SkRLMHdHcDZLb2FtNUtxNmZJX3FRNFROTmJTbEx0ZG50QXV4SGxQdHNLV2FybDUtVDdGS21za3pvcnNLMTZrZGJ4bldrZHBNV0NTdnlpRVlzSllOb3k5Y3BQd0NMNWVDZFlsY1pMUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島市植物公園　キク展 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE45TERJMjMzeUxoVzlId0NWRy1tWTd4NDFiTnYxSDRWaVdUclVVNnZFQ0lRdzdEeGFwR1h6RzVvRFcxUnBoNEVaMWI2U2hDOFVWQzljZmRpcHYtbVBGRzd3RGVSSTc1Y0ZH?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">元プロ野球・広島投手、池谷公二郎さん死去 74歳 初優勝に貢献 - 毎日新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9EbGdNeHNkVi16QXlsUm9iZjBKTVllcjZhT3pJal8zUlUzelZhSnhXQ1M2MVlWdVB5cjNTZmd6aXpxSXR1OURRZzRjcDdsd0w4WENodHd6b1lpQ2VwMlRN?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">プロ野球 広島元投手 池谷公二郎さん死去 広島の黄金期支える - NHKニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600561?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ANA AIRDOなど完全子会社化へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600623?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">欧州中銀 2会合ぶり金利据え置き</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600594?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中部電 27年3月期の特損3800億円</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600589?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">11月電気代 大手7社で過去最高値</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600657?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">のぞみ1hで14本運行目指す JR</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600644?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">情報漏えい 4月以降延べ2.6億人分</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600574?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">コミックシーモア 一部再開を発表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600552?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">四足歩行モビリティ 実用化の壁</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600531?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMOサイバー攻撃 捜査の焦点は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600536?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO社長「犯人特定の有力情報」</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600646?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">全国的に大気不安定 急な雷雨注意</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600631?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ガソリン補助金 12月から段階縮小</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600608?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">電気ガス代補助 12月-来年2月実施</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600526?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">衆院比例議席減 自維国が正式合意</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600604?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市首相のX投稿800件超 傾向は</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:24</p>
