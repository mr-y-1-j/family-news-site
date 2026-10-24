# 🏡 Family Portal 10/25

<div style="display: flex; gap: 10px; font-weight: bold; background: #f0f0f0; padding: 10px; border-radius: 5px;">
  <span>⛅ 広島: 雨</span>
  <span>📈 日経: 62,693円 | USD: 156.81円</span>
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
      
      <line x1="50" y1="50" x2="50" y2="25" stroke="#e74c3c" stroke-width="4" stroke-linecap="round" transform="rotate(75.0 50 50)" />
      <line x1="50" y1="50" x2="50" y2="15" stroke="#2c3e50" stroke-width="2" stroke-linecap="round" transform="rotate(180 50 50)" />
      <circle cx="50" cy="50" r="3" fill="#333" />
    </svg>
    
      <br><br>
      <details>
        <summary style="cursor: pointer; background: #1abc9c; color: white; padding: 8px 15px; border-radius: 20px; display: inline-block;">こたえをみる</summary>
        <p style="font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 10px;">2じ 30ふん</p>
      </details>
    </div>
    </div>
  <div></div>
</div>

<br>

## 📰 詳しく見る
<details><summary>🍁 広島のニュース</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5IWl9Zckk5OGlISG9rRDR2Q3ZQeDV6ZXBZRmJXUDJTRG9hSFpkMkcta3JvclV3S1dZUW1aZ0I3SnZ2MGl4U0RvQUlRUWNWczFFLS1xbTg3UmZlZEV2bnZGekluWVVRZ20taWItNVhKQXl2Y3FUWkZwSEg0UlVNcVk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島を戦力外の前川誠太、ＳＮＳで違法薬物の疑惑を否定…１６日に不起訴「一切関わっていません」「これからも野球に真摯に」 - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTFBOVVVQR3NvZThUbE1xWGFzblJXWjZFaVZoWWJlc01iLVVFLTRrSU12NUJkS0FMMEgxdXNfbFRQd2thX3BWZ1d1aW9tTklabzNHb3gzZEswMHFiVkQwNFljM3dXbzBlYTNvQlpxX29mMlplbjlNYU5kNkMwakItOUk?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島戦力外の前川誠太内野手「違法な薬物には一切関わっていません」 ＳＮＳで不起訴処分報告 「これからも野球に真摯に向き合い」」などと思い綴る（デイリースポーツ） - Yahoo!ニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMirAFBVV95cUxOWGV4cW8yYTJ4MXlpSEJwX0RSOTF5MTZSOVVRRklldVdVMHBzQld2V2RGUkxMWVN5M2ZuWTJVOHFUUGRZN05XeEJNay02RHJnX0puVTdMMzFVenJxdUw2ek05RXUzY21CNFJkSDBGUVJFelR5VHJRYUZNY3YtNk1icUtZNF9RZ1VtaGR1Z0dyWE5JV3B1QjNfSzU1SVlpV2Z2Zl9BYlIxZl9JS3B10gGyAUFVX3lxTFBQcDhDUTdqYUUtREJ3SFFRWWNhQzUxNTZIQ09JcTNMN3lPeWZiSlR2TUNXSGZucEpPYUJFbmRjOWxpcEZmTkhwV3U4d19BQlZLMVRTSldtV3lzRlhwRmptT1Q4QkFhQnZTNk1pQWtpWkpVS0Z4N1N5ZjNvb3MwLUtNTVB4RTREWFZfRU9yVDNaclpibFhlS2ZzU2FiSFctN2JlV21qNDVXMkNnZ3BfWXUzMUE?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">広島から戦力外通告の前川誠太「不起訴処分となりました…私は、違法な薬物には一切関わっていません」 - ｄメニューニュース</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMiV0FVX3lxTFBSblFZa0g3S1p4NldjVDQteGJLanhSSVBVZ2wzeHRZeE50ZDBxWlZlRXdwcUFQcGFYMGZmMThrRzg2VVVIdVE5cVRLdkxPNXI5djBEQ2UxWQ?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】【戦力外】ケムナ誠 「自分の思い描いていた成績は出せなかった」 一問一答 - TBS NEWS DIG</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE01LU5NVlVOaGZuVlhrOW1QWmNqajBXTXJIUUF4blRfd254clB0ZlljbzRMQzhjYVREaXpyclBsNl82XzdSMTdhNWZ5SlYyT1JELVlhNXBMVDQtNXVuZnpGWHkwQXl0UGhIazFKUFRINkktVk5PY01sUUxYcUpLemc?oc=5" target="_blank" style="text-decoration: none; color: #0366d6;">【広島】ケムナ誠ら６選手に戦力外通告 人的補償で入団の日高暖己も 今オフ計10人（日刊スポーツ） - Yahoo!ニュース</a></li>
</ul>
</details>
<details><summary>💰 経済・ビジネス</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599894?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">裁量労働制 乱用防止へ労使が一致</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599864?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">タイムズカー情報流出 集団訴訟へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599952?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">OKURA不適切還付 追徴額5.8億円</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599996?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「Used in Japan」世界注目 なぜ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599969?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">大阪IR ディーラー人材確保に課題</a></li>
</ul>
</details>
<details><summary>💻 テクノロジー</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599992?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO不正接続 一瞬で119万円消失</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599979?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">能動サイバー防御要請 政府側慎重</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599928?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">GMO 能動的サイバー防御を要請</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599967?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">自殺予防にAI 厚労省が効果検証へ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599943?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">個人情報売買 ダークウェブの実態</a></li>
</ul>
</details>
<details><summary>🚨 国内・社会</summary><ul style="list-style-type: none; padding: 0;">
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599995?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">台風 26日にかけ警報級の大雨恐れ</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599923?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">皇室典範「安定継承」議論乏しく</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599886?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">皇族数確保へ 改正皇室典範が施行</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599997?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">「軍民両用」産業育成へ 年内策定</a></li>
<li style="margin-bottom: 8px; border-bottom: 1px dashed #ddd; padding-bottom: 4px;">📰 <a href="https://news.yahoo.co.jp/pickup/6599983?source=rss" target="_blank" style="text-decoration: none; color: #0366d6;">小林鷹之氏 ガソリン補助縮小必要</a></li>
</ul>
</details>

---
<p style="text-align: right; color: #888; font-size: 0.8em;">Updated: 08:50</p>
