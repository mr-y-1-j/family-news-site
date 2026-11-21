# 🏡 Family Portal 11/21

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: くもり</span>
  <span>📈 日経: 56,437円 | USD: 159.71円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(305.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(60 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">10じ 10ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE1BVlpuSWNubzM4OVRnV1RpYl8xYlVXX3ZLaVhnZ3RsZDNrSzRfNktqYnJqMWVyaDMtd19kVEIxTnNCdjAxMGhaNlBwejduREREczNiVWtkSDRuUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">スーパーのロピア「宇品コーナン店」12月4日オープン 広島の宇品エリア、ディスカウント店含め競争激しく - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBHOUhlUE52UUtpell5OWs4emoyTGdHR1M5LU1kbUhRRTdnRGNEMmZ1SE5TcDFFb2RuQnQxY1hwRkFaTXdSa2FWdDNlcVBjbkhUVE5ZNWN6c0FDcDdaMXB3bHFDNS1la2JjNzd1aFFOd2pvWlo0QjhiS0xnQ2FySE0?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「まさかここまで…」ソフトバンク、昨秋ドラフト全体〝最下位〟の116番目指名から1軍デビュー右腕がアップ更改 広島移籍の東浜巨と合同自主トレを計画（西スポWEB OTTO!） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE90aU9LdmhnNHJYQV9KNTBnZFpqUzZwUWk3cXhzX2F0V3U2V24wTXhGdTFaalUzM3BRXzZibmtyeHVtc1loZHlLU0tmdnUyYkJuSDdnT0FELUt2RTRhNElLLXZGclpZZlpwSFUzSGMyM3dXZE1aWlRwMnIwRFZqRHc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「西武に来てくれますよね？」去就注目の広島FA戦士にファン反応 セ・リーグ3位の得点圏打率 勝負強い打撃も持ち味「喉から手が出るほど欲しい選手」「捕手としてやりたいのかな」（CoCoKARAnext） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5oa0Q1STBaYUlzYWl6aTJJTnA5ZEN2bzFDb3VOVURyVnhET0kxUnRyQVptdDRMOV9sRWJ3LXpydEROdTBHZ05oSF9ITTZXclJnV25CazZzVDI1Zk16RzRPOVM0bW4ySlpfU2tYQUV4bmFZR0VsbHBXOF9GYmpwa0U?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島で“初雪” 21日午前4時半ごろ「みぞれ」観測 平年より17日 去年より12日早い「初雪」 広島気象台（RCC中国放送） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiV0FVX3lxTE9QamNnUVdwcEJfRVR3WTlJaFFrRmptd2dqWk1JRU5BZ2g5SThXYlZLaXZPQWpiazZmRGFoT2ktLXFaZDVYUm9yYmpPUXRNekQ4bUJZbU1POA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島で“初雪” 21日午前4時半ごろ「みぞれ」観測 平年より17日 去年より12日早い「初雪」 広島気象台 - TBS NEWS DIG</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603352?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米株式市場急落 ナスダック5%安</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603347?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">EV補助金受け付け終了 予算枯渇</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603327?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ココイチ売却 米KKRに優先交渉権</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603379?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">なぜ実家暮らし 40代未婚者の答え</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603281?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ホンダ 新型3列SUVを世界初公開</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603360?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「リーマン予想」生成AIが証明か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603349?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ZOZOTOWN 1518万人の情報漏洩</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603339?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「KARTE」情報漏えい延べ2200社</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603344?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">丸井 EC顧客名など883万件漏えい</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603320?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">政府内部資料流出か 不正アクセス</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603354?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相 APECで台湾代表と会談せず</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603370?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">定数削減 野党の懸念を置き去りに</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603366?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相中国到着時の段差 木原氏説明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603335?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">安保3文書素案 原潜「検討着手」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6603382?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">未着工原発計画に交付金計165億円</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 11:53</p>
