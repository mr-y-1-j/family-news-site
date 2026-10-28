# 🏡 Family Portal 10/28

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 晴れ</span>
  <span>📈 日経: 63,946円 | USD: 157.85円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(227.5 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(210 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">7じ 35ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE1YS05iTjV4NnNNSzlhYjJXaXlBNGpjWTZYOHVjUDFvc0VJMlpvNUtiTEJOaDdGc0Z6ZDlyaGRTazhObW45cXZPZWlFdjNKUXNKMzhuTDg4TGpLRWdTdlhDRjBfZ2Z3Zzh2QXA0eHFpZ3Etc1BzbjZEX1ZEMy1nUFE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島 床田寛樹「絶対に出たいというわけでもないし、絶対残りたいわけでもない」球団と交渉 ＦＡ権行使は熟考の姿勢変わらず - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiekFVX3lxTFBrakkwQ2hBbGt5OE92RHpDR1NLbVNIdE0tQXNVZmt0bGRiRXJWWFlvT0lMc2xXOHN6dGNXWXhFUVREeTN4cFRkSm51c3AzR0dOOXI0ck1Nd09IZnBfQVM5UVJRa3kybElTYks3TlRDcDZjMXhENWxUSHhn0gF_QVVfeXFMTzhOaFMxczhVUzBPazRkZWRIX1V1QU92dzVvOXdza09SbTJrZnd3bnp6cllVVzB2MDRvNmJSYzhka1dlbVg3dkZZeWk4ZlI4NlFfdnExdDNnbWswUEFBTnZHM19LRGRXWHBsWi0xVWJQWi1veWJOcW1lS0F3TTBjYw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・床田「絶対に出たいというわけでもないし、絶対残りたいわけでもない」　ＦＡ権行使熟考　代理人同席では初交渉、既に条件提示 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMijwFBVV95cUxNWVN4Z25MT3JveHQzRkVzYlY2ZGtwOFVqa2xWOUMzWDZmQ21mNURpTXRIZXJjcUdYcTFtZjl4RmhwWjlST1ROTEtldU9lSWJMV2dSdVlNSkgzbFBDcWlXWU5Zd3ZsNThnN0hsTzk5bGR0Nk9IMU5jUlFLaVZNU2R2eC1kSGtRQm1Rcjl4Ml9Xdw?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島・床田寛樹「しっかり考えて（決断）できたら」FA権取得で初の残留交渉、熟考の構え - スポニチ Sponichi Annex</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTFB0MmJtS3NySnFhWElCRVNIWkxDX0dzdXZZNnFfUlVhZDhqUnhxcF9CdW5oa2t2X0R0WjJ0bG1FMVZwMEFaZGh6LS03ZWp6NkZBUC1YbA?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">10/28（水）広島戦 新商品発売およびニッパツ三ツ沢球技場グッズストア出店のお知らせ - 横浜F・マリノス 公式サイト</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE95clhNREZLaHZObzdhNlNVNkUxNERKU2xnSGFGMEtPc20yRHZTX0h1MGlDN3VLdlk1S2VSVXJHVmc5N2V4TE1pYjdfMHQ5QS1mNVF6NWxnVnF1bWYzYmZGTWdzX1lFV0FYRHlHekptdHdRY3d3QzhEbGNOZExiZ2M?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【ルヴァン杯4回戦見どころ】連覇狙う広島は横浜FM戦！ 新体制水戸、唯一のJ2鳥栖にも注目（スポーティングニュース日本版） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600353?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">イオン熊本 一部再開意向を伝える</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600319?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">ニデック 創業者ら9人を提訴へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600248?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">米MS 6万人に退職パッケージ提示</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600265?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大手生保 国債の入れ替え加速</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600331?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">たまごの平均価格 最高値を更新</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600375?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">サイバー攻撃 サイト経由型が急増</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600371?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">Siri AIが日本語対応 使い勝手は</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600364?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO攻撃 被害者は「恐怖しか」</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600351?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO不正アクセス 警視庁が捜査</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600341?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO 被害者に最大300万円見舞金</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600361?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">安保3文書で「拒否力」防衛の柱に</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600379?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自民 衆院比例で「統一名簿」提案</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600346?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">農相の関連団体 計85万円の不記載</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600343?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">副首都 要件満たせば4道府県指定</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6600325?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">北日本 今季一番強い寒気襲来へ</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 09:47</p>
