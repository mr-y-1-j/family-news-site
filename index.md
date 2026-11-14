# 🏡 Family Portal 11/14

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 雨</span>
  <span>📈 日経: 61,142円 | USD: 159.88円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(115.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(300 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">3じ 50ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBPU0F5d0JlXzdSRGpYbjlUZ3J6Z2NxVk1pUEhKRExmVzUtNVFpUGRnSlZSa2l2QTAzN3FONEt0S011QlJpaFZHdzhBd3MtWHZxZTAyQ1JGWHlDVXBlVy1aY1hIVWdzSUdsQ2dTSGJ5NklSclFoNjBJVzY2S1FtTXc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【独自】長男（30代）を放火の疑いで逮捕 3人の遺体発見の住宅火災 家族3人と連絡とれず・広島県福山市（広島テレビ ニュース） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiS0FVX3lxTE1yYnhnYmZGQW9SR2FRRlRzTWxUTVJxNTg0aVk5Rm5fN0wwQUl0dVpzVHIxem04dkI0WWN6aGg0M2FBb0dqT3R4UFdpMA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島市、文化ホールのあり方を検討 費用も踏まえた「広響の拠点」と3機能の整備を考える - AND BUILD HIROSHIMA</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBDX25LNTlWWUpjSDFYOFhUb3hiSGRXTWxNU0twVkdBVVZzbWE2R3NtR1lESEEwUlFpalgzb2JHTGZIeDFRV3pYUlZKSHVWZG1RbTFabEczd3ZwQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島電鉄、ICOCAなど利用時の「3秒エラー」解消へ 年内に決済端末画面の表示を改良 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ZQ0VBM2RERmtCNVZfQldZbjk3dHpFMExTU2VuQkEzenhZc3AtdTBkNmtCRThzSHFrNkt4V0kxdlNvZjh0eHVXZDl3R3dPbjQ2ZDdNNzJORGMzQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">たびまちゲート広島、広電車両モチーフの目印チャーム発売へ 圧縮タオルも - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiUkFVX3lxTE8yb1k0WlBrNHdkc2NsaEVmZ19CRjFYWjFjdGJCRFZ4ajdBdTZqQlNoQXNyTUZDRHZjR1VCc3A1dlRXQUpXSC1hLXFvZWg1dTFKTlE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島電鉄 創業記念イベント】「ひろでんの日2026ーみんなあつまれ！ワクワク秋まつりー」を開催！ - 山陽新聞</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602519?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">タマホーム 保険代理業を廃業へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602512?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">3メガバンク中間決算 最高益更新</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602514?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">FRB 市場の最大脅威は「AI関連」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602468?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「週明け怖い」MS障害の影響広く</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602497?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「人生初FAX」MS障害で代替手段</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602508?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">マイクロソフト 大規模障害を謝罪</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602492?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">MS「復旧が進み、安定した状態」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602486?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">マネックス証券 免許証画像流出か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602430?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO攻撃 被害申告は29.9億円に</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602427?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Google 韓国地図サービス強化へ</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602504?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">防衛費5年で60兆円規模 政府調整</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602480?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自衛官の給与引き上げ法が成立</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602418?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">政府 ロシアに首脳会談を打診</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602431?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">支援金 勤労者全体の5割以上検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602494?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">声や肖像 AIの無断利用に規制案</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:53</p>
