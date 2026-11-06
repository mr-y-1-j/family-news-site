# 🏡 Family Portal 11/06

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 57,491円 | USD: 157.86円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(17.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(210 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">12じ 35ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBNYzBpaUlIeUFaSkNhbFpOWnYwWkJZZjFyTzQ4ckhqQnFLc09pSGZPSGZXb1MxUFNVWlFzZXdxNVlqT2F3TGZIYU5LWmZlZDk3UnNkVU0wN2c3ZVE4SEFJRDdqTjBrZGR1QTBkckNhY0RKMlFZLVc5MDktbFFsRGc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 ソフトバンク・東浜巨を無償トレードで獲得 功労者の移籍先模索→先発陣強化の思惑が一致（スポニチアネックス） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE9Yb3EzTHJ3dWh6VDBmckVuRUxRWlA0LUc1ZUpJNUNaWjJNeXdWWlpCRXQwQlhTbkVRd3o3V0RwVV9GMnJsRDJTd3dSX09OeDFKLVM0NmJpTDhuUTRVVEJQcGV1czR5WGhYVXZQeEIwannSAXhBVV95cUxNTzhiZTVsOUF1eVVqcGZKWGxENGtMSFRfM3pFRC16Yk5aYko0TGdnUmEzWGpGbXlJNTFOdDdNWUZoaUZyYTJLU0x4Und3SEpfeGpKdUlkdjRSVnJyM1pXYzc0bGhReDkyRVJfRFRZeDBrN3JWdjd0d0k?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【ソフトバンク】東浜巨の無償トレードでの広島移籍を発表「ファンには感謝の気持ちしかない」 - 日刊スポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9WazA2Qkp5am9IWGZQTkpPaGhOcWo1VUhjS01GQnNXQ1NFVlJySmNKN1RZZndVT1ZDVDFCTkNwT0dGT1BkNzFYNGZZSlNwbmlqS3laT2JUT0tvZllnUDdlclJNWFd6SUE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ソフトバンクの東浜巨が無償トレードで広島へ 17年最多勝の36歳 - 朝日新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTE5BMG9MdHlhQ0RDR19jZVk1Mm1GcDd5MTJBM3MtWkVBUGxra3RILUVxS2lxdUNDSGE1NXZleVdJWjRpNUh2aE5yaTEzSnd1MGpINTd1VWNRT2R5VS12Ung3ODcwRXI?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ヤマダＨＤが広島に中国地方最大の店舗オープン、３００ｍ先にはエディオン…商品手に取れる「体験・体感型の売り場」充実 - 読売新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1MM1VyZDAzVE1UYWVlakFFTnRtc3p1VTh4d1NFZHktVnIzX0xoTnpaZG5iVDJ2QWZuX3dFZXU4VzVGUTdmVnREMjVzMnRmaG42R1B0eTU0d0JLX3dWaWx4SmZoT0haWnBnWlgxN3FXUGUtX1ZXekg4QnNTb0Qza1E?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ヤマダデンキ『新店舗』 広島市中心部に６日オープン その全貌と戦略とは？ キーワードは体験・体感型（テレビ新広島） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601497?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日経平均 一時4000円以上値下がり</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601489?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">経産省 中部電力に業務改善命令</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601477?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">NYダウ急落 一時1800ドル超安</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601493?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">9月の実質賃金 9カ月連続プラス</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601473?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日本製紙 八代工場の紙生産断念へ</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601482?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ドコモ通信障害が復旧 原因を公表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601413?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ドコモ オンラインサービス停止</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601439?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サイバー攻撃 10月は国内4億件超</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601404?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「e-Tax」の運用を再開 国税庁</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601401?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AI効果「期待超えた」日本企業9%</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601453?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">6日 全国的に気温高く夏日予想も</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601463?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相 米大統領と協力していきたい</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601490?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サイバー攻撃で強制遮断検討 政府</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601499?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">取り調べ拒否24年以降158件 調査</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601451?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">個人向け国債「複利型」導入検討</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:52</p>
