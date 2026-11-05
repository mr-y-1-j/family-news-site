# 🏡 Family Portal 11/05

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 61,864円 | USD: 158.05円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(260.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(240 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">8じ 40ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE42a1Y4bURWdV84ZEhySTBJNHVFRzFnMlpPSnpfT0syNk1aazRMZ2pKckNSQzcxUnRPNTFRczhHc3BVRkhVdG40NXZISWxEOW5nM1A4VnJza2dtdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島県西部のイベント情報＆おでかけガイド【11月5日号】 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiTkFVX3lxTFBqTE12Nmc5RVR6X05tZ3lMbDVkU3lRbG5QbEROWG9pSW1UcHc5MTE0eUotR0VjZHFKb0gtRGs2ZEllckZETUIycGtyLVpmZw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島電鉄】真っ赤な電車『トランルージュ』でお食事はいかが！？９０分の大人時間！個人向けプラン登場！【広島発】 - FNNプライムオンライン</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiUEFVX3lxTFBsWUJ5RlpESXo5QkgtQWJrcWQyV0dCVTJLdHNDVGJ6bzlTOF9ZUjVDdlVGeVRSaXZ2WWR5NEVTd2JVRk1hdjlKbXlFU3FMVThJ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・森下がFA行使 胸中明かす - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBHS243NVlVOEhjUVdBVWNmclBNeG5lS2VpWk9sWmNBS3J3REZLZnhRRGpvaWRla1Q2X3ZfNnZLRDEzVjhVenVJZ24wMlhyUVJGaHhRLTRRSHBIMUgzOUxrTEYwSDFSR01zaHZUejNkSWcwZndlNVoydndGWXFSRUk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】森下暢仁が国内ＦＡ権行使を表明「今も残留するか、移籍するか悩んでいます」申請書類を提出 巨人など複数球団が獲得調査 広島を含め大争奪戦へ（スポーツ報知） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiTkFVX3lxTE5VR0E1eXc5SGxYcDQxRUItaVNBMmdiM3BlekNsUXY4VGNQd29USWFVLU0zbVJVb2NYY1M3OS1qQlZFLV9JeC1GQW9mQVR5QQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">カープ森下投手 ＦＡ権行使を表明「たくさん考えて決めたい」２０２０年に新人王、先発ローテの中心で活躍【広島発】 - FNNプライムオンライン</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601343?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米中間選挙 日本経済への影響は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601373?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ダウ一時1500ドル高 選挙から一夜</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601365?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">リニア工事費 再び増額へ検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601346?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">金融庁 ソニーFGに立ち入り検査</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601352?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ゆうちょ銀 松井証券に20%出資</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601387?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">仏銀行サイバー攻撃 177億円流出</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601361?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">e-Taxに不審な通信 緊急メンテ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601325?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">免許証画像漏えい SNS悪用詐欺も</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601331?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">無印良品 クレカ番号など流出か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601264?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">1兆円盗難 バイナンスが手口公表</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601367?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">関東や伊豆諸島 大雨災害に警戒</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601376?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">消費税減税 あすにも衆院通過へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601371?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「書道」無形文化遺産に登録へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601372?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サイバー救援隊を創設へ 政府案</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6601362?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米中間選挙 日本政府は動向注視</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:52</p>
