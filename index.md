# 🏡 Family Portal 06/04

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 天気不明</span>
  <span>📈 日経: 68,402円 | USD: 159.95円</span>
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
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE0zRXEwc25wZFhaV3dQY0N2NDlaN2lOZXNEeGMzdFlrNFFIQjU4M3N3VkViZktkY3E1WWxCQUhvM3R2cmMxZ2VsZE1EZUR5U3A2TzNER3gtQ0tnUQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">作業中転落か、60代男性死亡 北広島の工場 - 北海道新聞デジタル</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pYzUzNzI5MkFiRzgzMHlTRFVCMmZqd1VFUDVQTGk0TUREWHJXUnRhYmJjQkJPYUxudFkyNDlfdl83NnBGZlFVRXhmbzFycU1NOUl1V0xrUEJkcEZoNDZReEVKLUc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【きょう6/4(木)広島天気】どんよりとした雲広がる 日中弱い雨 夜から本降りに - TBS NEWS DIG</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE9LQ2xRbHlIcE9rZDE1SC1vcXhXNGFpZXQwLVJ5R1d5U0hUVTVrcGdfSXhBV0ZEaVpaV0RWTWhKbFVIb2hWSnJlc3dmYS1WSy03VV9VelFTM1B4QlltdTNTOGJCNzM5WUdCZFdQYmozWEEyOUt0UDlKdHBtMXpjaFE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">日本ハム・新庄監督 敵地広島ファンに異例の言及「やっぱり真っ赤に染まったスタンドが選手の力になる」「少し前ガラガラの映像見た時にすごい寂しく。きてほしいですよね、球場に」（デイリースポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1NaUFaMnFQWGpPQ0taYmZKRWxLSDNRVmMta0Nva041bU9aR28tZnA5UjVtN256YjV3ekNGd05xVWR0SkRYOE9uWUJKMmZlbEV4ZVlrQ3NhdEJDbWxmeGNnRXU0WklRRDE0UFZ6cDdLSE1XMTN3cFBVSXJkNkNqdDA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">流れ引き寄せた坂倉の盗塁 広島の交流戦初勝利は「主導権を握ったことが大きかった」と安仁屋宗八氏（デイリースポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMic0FVX3lxTE51UGdRYmN2czRRNmx6MGpJWXJCbmpGalJncTRMYWhOTUVFd3AzSE9vNGIwNkE0NE00SW55ZXpINmVGV3RfZlFSMGpsMjhFTkwzZFJ4aEZtXzJldW5OZWlFRmRSbS1hWEI3aFQycU5VN3VUSFk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 マツダでファイターズガールが「きつねダンス」披露 交流戦ならではの企画で球場盛り上げる - デイリースポーツ</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582867?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ヤマダHDとEDION 経営統合の方針</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582835?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">日銀総裁 利上げに前向き姿勢示す</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582814?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">前橋唯一の百貨店 閉店残念と知事</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582831?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">中川政七商店 売上高100億円超え</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582834?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">無断キャンセル200個 弁当店無念</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582855?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">不法滞在巡る市のX 抗議受け削除</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582816?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">藤田医科大病院 患者情報漏えいか</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582779?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">高性能AI なぜ政府がアクセス要請</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582772?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">警察庁 サイバー対策に民間専門家</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582763?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">トランプ氏 AI規制強化で大統領令</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582782?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">25年出生数67万人 10年連続で最少</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582798?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">歯止めかからぬ少子化 対策拡充は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582861?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">食料品の消費税1% 今月最終判断へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582824?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ガソリン補助金を縮小へ 首相検討</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6582848?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">マスコミなぜ避ける 問われた首相</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 08:25</p>
