# 🏡 Family Portal 05/14

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 63,272円 | USD: 157.78円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(340.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(120 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">11じ 20ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiV0FVX3lxTFBFUTJwT3pyTm4yeE10WXpobENHTjFtNmNnMzdxQXVIRXRBRkFhNHpRYzJ4cm1xc2tQZGNzOWtVY1lTQ3R2blVzVHdGMHRrcHpKcU9LMkFFOA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">特別養護老人ホームで46人に虐待 広島市が行政指導 ベッドの四方を柵で覆うなど 広島 - TBS NEWS DIG</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1Pd0Z1Z1JDc0xkTGo0M2ZVMV9FU1dmaEpLQVRfZFFEc001Ylk3SnNBMzJDYXU3YWpCcFZhUDlXSTRSU1pKWURIV252ZVJLbEVkaUtzbDBQbm5zNWNHSkpB?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島市 特養で入居者46人に対する虐待行為確認 行政指導 - NHKニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE84MlhkY3hzZnlkV2VxZGduNXdMVzh0SmRpbEd5Qzh3MXhqMU85a3h2QnhCcUl6SHRrcVk2a2xHWmtqRUIyS19rYW9uZ3dCXzhGaU9XdUszdUxUUlNOOUdnT2R5UmlDUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">特養が入所者４６人に虐待、広島市が行政指導…ベッドの四方を柵で囲う・車いすにベルトで固定 - 読売新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1SWUhhYlVBT085ZDVrRElwN0tCTldrdWtVYkNWdEE3RDc2RlBlNkRWbzhZbzZ4LTI2eDZLbENic0F1RVpKUUJJcVA2MDJPamttTFluT0xFd1dpUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「クマらしき動物」広島市佐伯区で目撃情報 関係機関が確認中、小学校1校が臨時休校 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE9Tc3dPb1A5TzVqZmN4MUIwQmhYaFNiSmlSUGJOUnh2TDJBZTRNdVpfYzBMN28zeTNhSzlOYkZWMWxSYjBSaHVKYkdvSGZXYlFNaGticWRRR0c?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 佐伯区でクマの目撃情報相次ぐ 近くの小学校は臨時休校 - NHKニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6580035?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日産自動車 2年連続の巨額赤字</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579964?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「物価高倒産」再び急増に転じる</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6580008?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">不動産大手5社 売上高が過去最高</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579977?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">コメ価格 下がるか高止まりか</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6580006?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">華麗なる一族の題材 日鉄吸収合併</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6580033?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">3メガ銀 AIミュトス利用の見通し</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579942?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">選挙の偽情報対策 自民検討案判明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579859?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">コインチェック KDDIと業務提携</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579858?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">有人の二足歩行ロボ 中国企業発表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579837?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">クマ威嚇 オオカミロボの注文3倍</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6580025?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">岩手県で最大震度4 津波心配なし</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6579988?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">再審見直し法案 自民部会が了承</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6580018?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">再審見直し案 検察からは不満の声</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6580002?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">政府 電気ガス料金の補助検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6580016?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高市氏 G7前の英と伊訪問を調整</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 07:55</p>
