# 🏡 Family Portal 11/09

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 58,847円 | USD: 158.24円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(347.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(210 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">11じ 35ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE16S0hfOHNOejJVMk8zMENEQ0NsdU9NRmEtOW43d2dSMnd1VGVfRHJKSXQ2Q0lPMWRmcnZMbE41eEs1ajNYVjg1REFDdlU2Sm85S0ZEaEFCaVFwUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島駅の商業施設エキエで大きな音 安全確認で利用客が一時待避 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijAFBVV95cUxNT01Zd2t2Y0U1M2FkbWZLWGNUNy1LUEI1aTV0QXhpeVRHSzFzcXlSM3VvS2pfRUVlZkZnSUFHTkRiSVNZZzIxbFp5NGZLcC1nS01WVDhnS2JDRG14c0t2NnJHZ3YxVnN4X1hXZ2ZoVGFNemhKYTdXY2pRUElCU1FqSGhIRUhWVXNDNG1Hbg?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【動画】夜の広島めぐる「赤い路面電車」おひとりさま乗車体験 酒や食も楽しめるぜいたくな90分 - 産経ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBQRU51dVo4Njk4d1NNblQ2T0dBQlpXU0V0TGo0SjNGOUNqeklIMHFmejBvcmR0SVRRY21MLWxYbW50VkFRZHVMcXR0MkVTdmpBRjBkTmZ1NjZaYzFQY3JxNWoyN01WMzg2aFBvQ19udVJRaFJWV0MtdVh6QUp0aWs?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">Ｊ１広島・鈴木章斗 代表入りと海外挑戦に意欲「一度はプレーしたいという思いがある」（東スポWEB） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTFB4WVRUcUxYcmdhby1tLUpKYmtya3ZUTmFGcVVhcU0wVFBOTjJpempBeGhidzJKNWlEdktuWHd5d2dSSjFHdGFSOVJNVGZyclcycFhQS1M1QkpQNThVelNKbGl3?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「マツダKDセンター」、広島港出島地区に竣工…全海外生産拠点へKD部品を供給する物流拠点に - レスポンス（Response.jp）</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE81aHRQcXdzUjNpY0V0WUc5Y0p4anFzUmxoeTlsb1ZLTkJidEJCT0pFVTFyVl9HcmR6YnFxUmlzXzBCSVplcGpxNG0wVXAzTTlYbTRsRko0Q2cxOHZNb3BsWnBLVWQxbnYzNmZsaWxsUHMwWS1INUIwS1g4dmFsb1E?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">全国高校サッカー選手権広島県大会 如水館が広島皆実を下し創部37年で悲願の初優勝 - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601877?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">7/30に過去最大円買い介入7.9兆円</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601868?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">CEOと工作員の関係 NVIDIA調査</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601813?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">MAZDA3セダン 北米で売れる理由</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601793?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">倉庫には古米の山 赤字覚悟で販売</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601864?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">舎人ライナー 資金不足陥る可能性</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601870?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">北朝鮮ハッカーのチャットか 入手</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601816?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「お砂糖」仮想空間の人間関係は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601787?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">個人情報「手放す」企業が続々</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601743?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「なりすまし電話」巧妙化 対策は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601694?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO謝罪会見なぜ炎上 プロ解説</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601858?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">9日 関東-北海道で師走並みの寒さ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601872?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中国を「脅威」見送りへ 政府方針</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601806?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相 金正恩氏との首脳会談に意欲</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601782?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自民 消費減税採決棄権で処分検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601819?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">清貧であるべき? 議員語る違和感</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:16</p>
