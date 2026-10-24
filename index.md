# 🏡 Family Portal 10/24

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 62,693円 | USD: 156.81円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(200.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(240 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">6じ 40ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE44dlo1R0RQa2tpUm9qcW53UzZTRERDV1dua0ZzVXo5ZkFSOTBLbUVqdTY5VTNpTjB1dDhvMzB0cWsxR3Y2dXIxMlFWbDBtQ0dFdXg3RGtFbms1M0Nrcko4?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島県と広島市 “不正アクセスで個人情報漏えいか”発表 - NHKニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5MMm5QX3hEUU9jZ3BQMFY5cDFiZFNSaWhRREQ3VXpoVFhxMk9VZjJiUUZBSnQtYU9rcDlsQjRENUdISVlMYzNSUnROUjFSTDlzSlhWRDdjcWFYSGhFYVY5SF8yREJIZjdfMm9HSEVMT0pFeDVCQjJBQlEtLU9hcFk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">キャッシュレス決済が！ 広島電鉄の「モビリーデイズ」に不具合 復旧見込み立たず 支払いは現金のみで（テレビ新広島） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiS0FVX3lxTE5nSTBoQklzM2NkN2hsbzVaMUlfNGI1bUZxRVBpdHR1ZWJ3bVhQT09ySmhaVjhoeEVlUmQwT0xGaUptVVlwZWNiMEpJVQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【火事】広島県北広島で民家全焼 - 47NEWS</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1yeURyN0FJQlBybEY3WkpTeERjNHpIcjJQZm0wWF9uZmFTZ25sY2xXbkZFbGdKUG1BSVYtSDRiQkVMdzljNzhiQWZBbVFXU3RsemowOGVGcEExS3cxZ3I5TDMzX1BDdWpjVU9XZnlIYlZFeEhiTkdaTUZFbXM1SVk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「なんでしたのか分からない」スカート盗んだ商工労働局の女性主事を停職処分 広島県（中国新聞デジタル） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE4yemhZSHlxSU0yZzkzZTRFMnQ3ZTBCNGtKX1NRSzd4VHZNQjMyN3JXYy1JWVc4YTE4U0xtZmg3MzB4cnR3TmdYdnRlYXI0MTEta3ZVc0xfa3hoQkNoa0UzOXR6ckI3bGhwbXRiUHJialdseFlsNFNrcEtWTjVYbUk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">パセーラに来月６日『ヤマダデンキ広島本店』開業 来春にかけ西日本初タカラトミープラネットなど新店続々（テレビ新広島） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599846?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">滋賀銀と池田泉州HD 経営統合へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599845?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">物価上昇2%到達判断の公算大 日銀</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599819?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">佐川急便で情報流出 最大5323万件</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599823?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">パーク24 流出の146万人に見舞金</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599864?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">タイムズカー情報流出 集団訴訟へ</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599891?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PHP問題 災害情報メールにも影響</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599728?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PHP巡り一般ユーザーは対策必要?</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599702?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">PHP脆弱性悪用の試み増 数百万件</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599885?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">パナG従業員情報 外部AIにアップ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599841?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">意図しないFX取引 損害600万円超</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599886?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">皇族数確保へ 改正皇室典範が施行</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599881?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">強い台風30号は九州へ 警報級大雨</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599859?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">生活保護訴訟 利用者側の勝訴確定</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599872?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">無人機墜落 機体引き揚げ作業終了</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599832?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">燃料油補助の見直し検討 首相指示</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 09:07</p>
