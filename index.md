# 🏡 Family Portal 10/31

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 63,290円 | USD: 157.80円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(255.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(180 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">8じ 30ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFA2eURXYm5qZ1F1cWd0cUxiSEZEV3dPY243R0c1akpTbEpMUS1FXzVJYkV2Q1YxMDc2TW56bFJXR1c4NXRRYkh5Z3dhSlpPVzdXazF2TEdfb1ZHQQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">FAの制度変更、カープにはメリットに - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBaanFDQkNSUWdSRWl1d054NnNhSWJKMmNka3RSaGV2bWpGOGc3UTJKQlVaLVd0TjFLRGhhY0hqSHF4d2pva0h2ZWZXS3ZteFRfbGU5dzZEMnRmUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島県高校駅伝、男女とも例年にない接戦予想 11月1日号砲 - 中国新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1jd0c5YUFJMEZKSVh1VmFzRC1mMnlyTUJJQUxnRlhuWVI2T05Qa1hwOWR4Q0w5TE5CRVJ6WEpnOXJkT3ZIUWQtQXdQMWxwY0VFLVJ3Uk5wd3VfYnRTdmxaNF9MWDhkWkRTTERhVURjeHhiV0FfdFE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">＜駅が街を変える① 広島駅南口ルポ＞ 駅ビル2階へ「吸い込まれる」路面電車 - 産経ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMie0FVX3lxTFBZZHFfVmFrZmxra1F0U2thNkZ1MEMxR0tHWWFQMVlQbWh5S1Vya0xBOVRMeFY1blJfeFlxNm43WlR5eTR2T0JPX3JMS1Q0SWNzb3N1aEczZ0ExbHFUTklmUi1BNWxPRmxadW5ZNkxZa0NPQlFpWlIyMm9Pdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島辰見鴻之介】「失敗できた」「未来のため」局面で前を向くスピードスターの証言 - 日刊スポーツ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5OODFmaEhnTVc4MHRpZXVIRmViSE90NnI5SlNELWM1V3hQUC1EMmVRWnZLU3ZEbV9rNHUyXzdGdlMxMHg2V1lSOHZUaG9GT1VvV2gyOTV6RTBwVDJhdzJBTWdRYTUtdmM3cFJxRUhvZldrV1hNNHpONldBdlZYUUU?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">池谷公二郎さん通夜 広島ＯＢが悼む 山本浩二氏「寂しいね。でも、本当によく頑張ったんじゃないかなと思う」安仁屋宗八氏「天国からもカープにどんどん喝を入れてほしい」（デイリースポーツ） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600770?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">東京メトロ 29年3月値上げ目指す</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600712?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">キオクシア 4-12月純利益24倍予想</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600721?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中国産オクラ 相次ぎ基準超え農薬</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600733?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ジャングリア 出資に数社が関心</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600763?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">神戸の「モザイク」全面改装へ</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600746?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">バイナンス 盗難被害の手口を公表</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600711?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">AI生成曲検知 JASRACが導入検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600708?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">バイナンス被害 北朝鮮が関与か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600689?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">暗号資産取引大手に不正侵入か</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600686?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">無印良品 最大2726万件情報流出か</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600756?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">消費減税と定数削減 水面下の交渉</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600743?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">茂木外相 露外相に記者の解放要求</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600698?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ウが日本に迎撃弾の供与を要望</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600753?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">発達障害増加 支援学校の教員不足</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600723?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">31日関東-北海道で天気急変に注意</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 10:10</p>
