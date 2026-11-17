# 🏡 Family Portal 11/17

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 雨</span>
  <span>📈 日経: 58,885円 | USD: 159.24円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(30.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(0 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">1じ 0ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBrd0tFTHNxNmF1RVBOMEpMMDdmcEtWWTM5dzZKNzlDYjllUzlhMnJTYnBTR25HWTJtdUpPNXBJTGNEcTItaU9sQjJxRkk4NjJWRVVZaDRQbURiVVFoalhhNF83SEhEVk9QVDdlTXNkUlhvT0lHb21VNGNnbV9aZVU?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">ゾンビたばこ処分不服で広島球団に要請書 矢野雅哉、前川誠太、田村俊介の代理人弁護士が送付「発言は撤回されるべき」「正論を述べるだけでは届かない」法的措置も検討（デイリースポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9fTkl6N0xWOWhJdlJfMW5BNGFRejg0anNTZnhoV3Q3RHJzaUttaURKRkFtbFZzTXBxYnNUWTdGTGJhb0N5WHBOM3cxSEFPTEktYmJ3YmJJb3hOUGdMbkJtZFdCN2N1aEd0QkE5ZkxlNmZwMDUybXBJd2tKNnM5dW8?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【戦力外】矢野・前川・田村がカープに要請書 「契約結ばない」真の理由など開示求める（HOME広島ホームテレビ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5vdHJ1eF9UVEVSeGhONXFkUXBvSjNBZW45ZnVUZ1ZXM3pxS3luaXJNeTFXNUVidWhJWTY3YXBrQjdyVkpiaWxaUWR0OUY5Yy1PUlJLZnktRTRhSlU0VTlWN2hNMkdpb0s5LUktR2pWTDFHd0I4eDdPRjNmNFI2ZFU?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">“ゾンビたばこ”巡る3選手が広島に抗議も、小園海斗は我関せず「決まったか？」加速する“新天地決定”のフラグ - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxOVGFJQng1Ym9UekVOeXVIelRDd0FsSnpILXI0Z3dQVHdtalg1eEhHR0JNRU9pYktJVllXcHpkRGV1dFpuWWtOSTVKMVBWVDI0R0IwNkI2SlN1Q0ZVUjlpenFqZGs2TDRVb1pacU9oZEw5LTJoYi0tUXpQU2ZGQkc5cXBsTlNuLUVjQkI0VE5R0gGTAUFVX3lxTE0yOWpwbHdldmI5WjUwWVNjT1k5QWd6ZDB0Uk8wVlp1WDdFSVZYMklmZVRRV0RoNTVSM3JHdFA5elNNbzY0VVI2aFBuOENfd1BheHY0a09aNXpnbnpSR0tvSlpTWnU2bVRWZnVwM19NQUl3N0FESkhUWUxwQVFmUDZORHVfdXNCcGplWXRrRVkwcWc1bw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">前広島・小園海斗のNPB球団との契約について球界OBの見解「あのまま終わってしまうのは」 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBHY2ZVMl80dHFFM19uUmZraVNkYnlKMmtuOFhrZzc2MGRtN0E4X245cTVUTlpFRjJGdUFHcy1tY3RIR0RFOHJ4dEtjaTA0U1NyRTFfc1diQmdUcVd1bVRqMnVKZzVmdjVlWEpMRnQ3Mmt6Y1UzVFp4NGdkejBERnM?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">元広島・小園海斗、獲得するNPB球団はあるのか 海外でのプレー選択肢も...識者は「もったいない」 - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602852?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">NY株大幅反落 ハイテク株に売り</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602778?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">フアン氏復帰求める署名 16万人超</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602816?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">タイムズカーの会員数 1.4万人減</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602817?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">マンション短期売買 課税強化検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602820?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">いきステに復活の兆し 改革の成果</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602871?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">MS大規模障害 幹部が原因を説明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602840?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">卵サンドつかむ客動画炎上 店説明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602807?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ドコモ「5G SA」で障害 完全復旧</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602790?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">富岳に不正アクセス 理研が明かす</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602770?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サイバー攻撃 AI「自律化」が脅威</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602882?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">推定ロシア機領空侵犯 福岡沖ノ島</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602866?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「防衛産業基盤戦略」概要が判明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602863?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日米豪印の共同文書案 概要が判明</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602819?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">政府 19日の米中ロ首脳会談を注視</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6602825?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">コカイン摘発 過去最多更新ペース</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 13:13</p>
