# 🏡 Family Portal 11/16

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 60,497円 | USD: 159.68円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(145.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(300 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">4じ 50ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiV0FVX3lxTE1EUE92Sko5czBRcmEyZDAyMUYtQU1rNEZpNG11ODBOSGliZ0ZRb1V3UHBIUUFJaWtYazBSVEdLWHlUbTd2M0I4amFIeFRXMnVvTUlGbXpsMA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【中国中学校駅伝】女子は熊野東中が３連覇を達成 5区間12.3Kmでタスキを繋ぎ 広島【結果一覧】 - TBS NEWS DIG</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5MekVaLXRTNXo2ZUl4NElTaUUtaE1JVTVxM3pHYjRDeTJXRzdCQWtMOHNxU05TbThCcDBISU1GZ3lZYlRkMHhTa0hDU2hWRmd2TUJHNjhfTGNDdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【火事】「屋上付近から白煙が見える」 東広島の閉鎖ホテルで火災 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFAwOVZ2aF84dnJ6VDlYaG5OSjFwejYwbG5ZazUxTnRvdDdFZzZUSy14UTg0OUpETUdrcVVpZWphLTlTM0wxTFJtZE13TjdoRHVuN0RqRFJMT05FMVVxeUlvSlVXd2VwV1VCRFFEOW5wNENlcm45bWpBSGhqdjJkS3M?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・宮島口近くの渋滞緩和へ実験 広島岩国道路の割引やAI活用（朝日新聞） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMihgFBVV95cUxPRnlJazl2SVVfOWdEWGRTZmVDaXZfcjI0eDFwUnJkN2Q4ckxwT1JwdEpYb1ZMbzZ3RHA1V3dXVDYyOVpMOFZtS2gtdlp5RkwzWUhQdjBWZEN3QkhjREkzU3lla1R4YktzYW14Rkl2cnNMSkxLRGhHLXA0Rlk1OVRQVUZMMmlSUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">信号機のない横断歩道での一時停止率、広島県は全国平均上回る約7割 - 朝日新聞</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBsUWl3NlkzUmZIeW1zRnp2cEhwWFgtWktHMDZFQmhNX0RIelNGajF0V1NQN19sbm9ud21lWS0tMVhtZi1ueHphZUcxaV9jZFFUd3BlTzhaNDZycjJKbVdla05rcEs5dWxIcWlBRDVXX0x1VFBBb3RPd2RVY0FYMlk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">「なぜまだ日本代表に入っていないのか」。サンフレッチェ広島・鈴木章斗はまるでケイン。味方も絶賛する23歳の才能【英国人の視点】（フットボールチャンネル） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602758?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">7-9月期実質GDP 4期ぶりマイナス</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602744?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">フアン氏がNVIDIA復帰協議 報道</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602747?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">JSR売却 差益9000億円超の見込み</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602755?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">そごう・西武大規模改装に400億円</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602745?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大学発ベンチャー過去10年で3.5倍</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602761?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ウが露ネット関連施設攻撃 狙いは</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602749?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AIに思考丸投げ 16歳「今後怖い」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602748?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AI敵視から融和へ Disney路線変更</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602643?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">検事の取り調べ AIでチェックへ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602642?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AIエージェント普及 問われる対応</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602735?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">原潜の保有「反対」52% 読売調査</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602696?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">消費減税「効果小さい」63% 共同</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602679?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">週後半 日本海側で暴風・大雪恐れ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602756?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">介護事業所 昨年度は38.3%が赤字</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602674?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">首相APEC出席へ 焦点は日中関係</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:27</p>
