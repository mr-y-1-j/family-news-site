# 🏡 Family Portal 11/07

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 57,435円 | USD: 157.50円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(27.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(330 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">12じ 55ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE9VR1U0QUprQzJEbERjZ0U0UjVvNV9LZUNVVUtBNWRYeFhyMVBIcElEbzI4dFFEZ21YVUFvVTZ3U2trVFQ1NmRrcGowZm1sSE1XQVNtbDlhei1uVGJwZ1A4N0NR?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「『2位でも獲れた』はナンセンス」なぜ広島は「まさかのドラ1」を“単独指名”した？ スカウトが語った「ドラフトは単なる実力番付じゃない」の真意 - Number Web</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1vam1oeWNXdWxlTWJSb3dENFNiazJPc0lhSV94Yjh1d3hMeVdtRFBZaHpEYUsxSU4wSWE1eUhUNktqV3IzbFQ3SEtZclh5dXdRZkhHbEJiZW5kOXhwX3lRZXhUOHZwczFkVld4bEY1bmdGS1J5WWxGV2VTYWJSd2M?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【カープ秋季キャンプ２日目】玉村昇悟「強い回転を意識、変化球を磨く」 齊藤汰直はコントロール強化特訓（テレビ新広島） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBiMlFTTWVQVGRtTTZkUmZ2eXVVMkNqdW9iWThGSTlVc2VlM0dUWFNPYVBNT2RGY2dSeEtrN0RwdG93Uy0zZVRmUlhqdDlRUmtwR0VWaER3NHNjYWxvUU16eC1tZDJ6S3ZTMF96SFVXTlN2d2Z0WDVEYThmNEJDTHM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【ソフトバンク】広島移籍・東浜巨が力説「なぜ鷹は強いのか」 在籍14年でリーグ優勝７度、日本一８度（東スポWEB） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE5aN3JHWm1KOE1hZVhhVXRVNXU3RWl6RzhidURUQkNOZVIyZlhkOWVuM21LNi1OV0lVT3Jod1NBOVpGaUxheldnejJIT0RBYnVoT3dZZjBvNEo0eWJMX1BnUGFmY2pvMzkw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島がソフトバンク・東浜巨投手を無償トレードで獲得…今季は一軍登板なし - 読売新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFA5U3kwUmlHVzBOVlRiSlFZbXNtSW9EYjVLMWh2c1JmdXd2NWR0MlhIQzBWWUU1TlZiaDJKbGJFT1AyNlJBZFRqbmZVN2NLREMzaW43SEdLckRaTllXMTQ2a2NZV3BqSWlDN3JFcTRXR3BuR2M4WTJCZ3ZUYWFjRkk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島は東浜巨を無償トレードで獲得も主力3名がFA宣言… 申請期限9日に向け大物選手の行使が相次ぐか【11月6日までの去就・戦力外・引退リスト】（高校野球ドットコム） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601587?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米10月雇用16.5万人増 予想上回る</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601571?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">信金のシステム障害 すべて復旧</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601546?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中間選挙ショック 世界で株安連鎖</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601580?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">KDDI社長 決算会見で2つのおわび</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601548?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">破産手続き中の全東信 社長が死去</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601566?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ドコモ 流出の対象者に見舞金検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601482?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ドコモ通信障害が復旧 原因を公表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601413?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ドコモ オンラインサービス停止</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601541?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">無印良品のネットストア 一時停止</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601559?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「推し活疲れ」スマホが一因に?</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601599?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市首相「中国は重要な隣国」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601535?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">石破前首相ら減税法案の採決退席</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601568?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">石破氏ら採決退席 首相言及控える</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601610?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">岸田氏 国債NISAは慎重な検討必要</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601612?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">超党派議連 ICC赤根所長らを激励</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:23</p>
