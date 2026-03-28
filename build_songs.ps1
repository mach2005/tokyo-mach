$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$pitchers = "10 上沢 直之;我らが待ち望む　勝利を手にする為　多彩な持ち球を 繰り出せ上沢`n" +
"11 津森 宥紀;男勝負の時だ 思い切り投げ込め 気迫あふれる闘志で 勝利へ導け`n" +
"16 東浜 巨;立ち向かえよ 勝利の為 この地に今輝いて 高み目指せ`n" +
"19 大津 亮介;制球乱れなく 緩急手繰る腕 青き翼を広げ羽ばたけ 魅せろ多彩な魔球`n" +
"39 尾形 崇斗;夢を賭けた マウンドで　尾形崇斗よ 今見せてやれ`n" +
"40 杉山 一樹;高い位置から 速いボールで 敵を追い込み 勝利を掴め`n" +
"47 大関 友久;ほとばしる汗の中 歓声を胸に秘め 男なら今ここで 勝つんだ大関`n" +
"48 藤井 皓哉;辛い時を乗り超えて 来たぞ夢の舞台 心ひとつに腕を振り抜き 勝利へ導けよ`n" +
"NEW!49 松本 晴;鍛えたその腕を 自信持って振り抜き 揺るがぬ覚悟胸に 松本晴輝け`n" +
"NEW!53 大山 凌;魂込めて ボールを投げ込め 果敢に攻めて 勝利へ導け`n" +
"66 松本 裕樹;胸元突き刺す 速い球みせ 決めろその球で 敵を討ち取れ`n" +
"120 長谷川 威展;気迫溢れる その球で 行（ゆ）けよ威展 ひたむきに"

$pitchers_general = "右投手汎用;恐れるな 立ち向かえ 気持ち見せろ 仲間を信じて 全て賭け闘え`n" +
"左投手汎用;抑えるチャンス 物にするぞ この腕で 必ず掴むぞ"

$catchers = "12 嶺井 博希;高み目指す男よ 立ち上がれさぁ 嶺井博希今こそ 強く闘え`n" +
"NEW!45 谷川原 健太;鋭い打球飛ばし 鋭い肩で魅せろ 今こそ本当（マジ）決めろよ さあ谷川原行（ゆ）け`n" +
"62 海野 隆司;歓声背に受け 熱い想い胸に秘め 攻守に輝き 勝利へ導け"

$infielders = "0 川瀬 晃;風の如く駆け抜け グラブ捌き魅せるぜ 快音を響かせ バットも魅せるぜ`n" +
"4 ジーター・ダウンズ;ラララ～ ジーター 君の出番だ（Let's go!!） オオオ～（オイ！）掴めVictory`n" +
"32 山川 穂高;どかんと一発 山川 ホットに飛ばせ スタンドへ 勝利の一撃 期待を込めて 放て山川`n" +
"6 今宮 健太;生まれ持つセンス 風を切り走れ 空高く飛ばせ 柔らかなリストで`n" +
"8 牧原 大成;みなぎるそのエナジー 轟け地の果てまで 縦横無尽に駆け抜け 男になれ`n" +
"24 栗原 陵矢;輝く時だ 後世に語り継がれる 伝説を今から 作れよ栗原`n" +
"99 野村 勇;ここで見せろ力強く 敵を凌駕する一撃 全速前進フルスピードで 勇ましく走れ"

$outfielders = "3 近藤 健介;極めた技で 打球が冴え渡る 遥か夢追い求めて 頂へと進め`n" +
"7 中村 晃;新たな扉を 今から開け 愛する男さ 中村晃`n" +
"9 柳田 悠岐;光のような足と 突き刺すようなスロー いざ一振り決めて 輝け柳田`n" +
"23 周東 佑京;たゆまぬ努力で さぁ時代を築け 志ひとつに 行けスピードソルジャー`n" +
"31 正木 智也;狙い研ぎ澄まし 殊勲の一打を 高らかに放て 正木の一振りで`n" +
"32 柳町 達;熾烈な争いを 勝ち上がる為 闘う男の一振り 華麗に打ち捌け`n" +
"NEW!57 緒方 理貢;夢追いかけ 打て魂乗せ 行（い）けダイヤモンド駆け抜け 今緒方魅せろよ"

$fielders_general = "右打者汎用;待ちわびた場所で 真の力を解け 限界超えるその日まで 夢の道繋げろ`n" +
"左打者汎用;今舞台が出来たぞ お前が輝く 最高の瞬間 羽ばたけ"

$chance_data = "アッチャン;【導入】\n熱く燃えろ（選手名）×３\n\nラーララララララー\nラーララララララー\nここで決めて勝つんだ\nそうだ俺達が\n勝利の使者になろう\nLet’s Go Let’s Go\n\n【本編】\nチャンス チャンス 今チャンス\n拳を挙げて オイオイオイ\nチャンス チャンス 今チャンス\n燃やせよ魂 オイオイオイ\nチャンス チャンス 今チャンス\nオー オイオイオイオイ\nチャンス チャンス 今チャンス\nオー そーれ\n決めろ 決めろ （選手名）決めろ\n燃えろ 燃えろ 熱く燃えろ（選手名）`n" +
"押忍！チャンス;(お楽しみは) これからだー\nワン ツー スリー フォー\nオー よっしゃ行くぞ！\n\n行け行け行け行け 押せ押せ押せ押せ\n撃て撃て撃て撃て 撃て 撃て（選手名）\n行け行け行け行け 押せ押せ押せ押せ\nオイオイオイオイ オイ オイ（選手名）\n行け 行け 押せ 押せ\nGo Go Let’s Go! Let’s Go （選手名）\n行～け 押～せ オー よっしゃ行くぞ！`n" +
"関東チャンス;【前奏】\nオイオイオイ\nオイオイオイ\n突き放せ\n\n【本編】\nかっとばせ（選手名） （選手名） ここで一発\nかっとばせ（選手名） 狙えスタンドへ\nかせかせ（選手名） かせかせ（選手名）\nいざ行け （選手名）`n" +
"北のチャンス;【前奏】\n野球場の中から\nがんばれって言っている\n激しく熱く\n今ここで がんばれ！\n\n【本編】\n燃える闘志今見せてやれ\n（選手名）一振りで決めてやれ\n勝利決まれば お前の夜だ\n（選手名）（選手名）\nいまここで がんばれ！`n" +
"鷹の道;行けよ男たち チャンスだ燃え上がれ\n俊足巧打で突き進め それが鷹의道`n" +
"アッコちゃん;オーオーオー… そ～れ いけいけ\nオーオーオー… そ～れ いけいけ\n（選手名）～ 今こそ～ 戦え～\nさあ行こう 俺らならやれるさ\n熱くなれ 男なら行こうぜ\n（選手名）～ 今こそ～ 戦え～`n" +
"オオサカツンデレラ;ラララララララララ…\n（選手名）（選手名）（選手名）\n（選手名）ラララー`n" +
"令和;ウォイ！ウォイ！ウォイ！（選手名）\n\n今宵勝利の為に 俺ら叫び続ける\n争覇期する時まで 此処にいる仲間と共に\n\nウォイ！ウォイ！ウォイ！（選手名）`n" +
"藤本;わっしょいわっしょい 「選手名」\nわっしょいわっしょい 「選手名」\n行け！打て！ 「選手名」 熱くなれ！`n" +
"若井;「選手名」 「選手名」 「選手名」\n燃えろ燃えろ 「選手名」\nかっ飛ばせ 「選手名」\nチャンスに強いガッツマン 我らの 「選手名」\nかっ飛ばせ 「選手名」`n" +
"鷹の爪;勝利を掴みとれ ～～ 「選手名」\n\n勝利に向かって突き進め 打ちまくれ～打ちまくれ～\nお前の力を見せてくれ それ行け 「選手名」\n\n男性：ここで決めろ！\n女性：ここで決めろ！\n「選手名」"

$multi_theme_data = "G.F.V (GO FOR VICTORY);【導入】\nオイ × 2\n\n【本編】\nラララーララーラーラー\nラーラーラーラーラーラー\n熱いそのハートで\n突き進め\n\nラララーララーラーラー\nラーラーラーラーラーラー\n攻めまくれ 掴み取れ\n今日の勝利を オイ！オイ！オイ！`n" +
"勝利目指して;【導入】\nオイ × 2\n\n【本編】\n勝利目指して\nオーーオーオオーオオーー\n勝利目指して\nオイ！オイ！オイ！オイ！\n勝利目指して\nオーーオーオオーオオーー\n勝利目指して\nいざゆけ\nホークス！ホークス！\n絶対勝つぞ！ホークス！"

function Format-Song {
    param($text, $allowTheme = $false)
    $res = ""
    $lines = $text -split "`n"
    foreach ($line in $lines) {
        $line = $line.Trim()
        if ($line -eq "") { continue }
        $parts = $line -split ";"
        if ($parts.Length -lt 2) { continue }
        
        $titleRaw = $parts[0]
        $lyricsRaw = $parts[1]
        
        $isNew = $titleRaw -match "^NEW!"
        $titleRaw = $titleRaw -replace "^NEW!", ""
        
        $badge = ""
        if ($isNew) { $badge = "<span class='new-badge'>NEW</span>" }
        
        $lyrics = $lyricsRaw -replace '\\n', '<br>' -replace ' ', '<br>' -replace '　', '<br>'
        
        $m = [regex]::match($titleRaw, "^(\d+)\s+(.+)")
        $headerHtml = ""
        $audioHtml = ""
        # Map player numbers to audio files
        if ($m.Success) {
            $num = $m.Groups[1].Value
            switch ($num) {
                "45" { $audioHtml = "<div class='song-audio'><audio controls src='./public/audio/45_tanigawara.aac'></audio></div>" }
                "49" { $audioHtml = "<div class='song-audio'><audio controls src='./public/audio/49_matsumoto_hare.m4a'></audio></div>" }
                "53" { $audioHtml = "<div class='song-audio'><audio controls src='./public/audio/53_oyama.m4a'></audio></div>" }
                "57" { $audioHtml = "<div class='song-audio'><audio controls src='./public/audio/57_ogata.m4a'></audio></div>" }
            }
        }
        
        $res += "<div class='song-card'>`n"
        $res += "  <div class='song-header'>`n"
        $res += "    " + $headerHtml + "`n"
        $res += "    " + $badge + "`n"
        $res += "  </div>`n"
        $res += "  <div class='song-lyrics'>`n"
        $res += "    " + $lyrics + "`n"
        $res += "  </div>`n"
        $res += "  " + $audioHtml + "`n"
        $res += "</div>`n"
    }
    return $res
}

$top = "<!DOCTYPE html>`n" +
"<html lang='ja'>`n" +
"<head>`n" +
"  <meta charset='UTF-8'>`n" +
"  <meta name='viewport' content='width=device-width, initial-scale=1.0'>`n" +
"  <title>応援歌 - 東京真隼 TOKYO MACH</title>`n" +
"  <meta name='description' content='東京真隼（TOKYO MACH）は福岡ソフトバンクホークスの私設応援団です。'>`n" +
"  <link rel='preconnect' href='https://fonts.googleapis.com'>`n" +
"  <link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>`n" +
"  <link href='https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;700;900&display=swap' rel='stylesheet'>`n" +
"  <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css'>`n" +
"  <link rel='stylesheet' href='./public/style.css'>`n" +
"  <link rel='icon' href='./public/favicon.svg' type='image/svg+xml'>`n" +
"  <style>`n" +
"    .songs-nav { display: flex; justify-content: center; gap: 10px; margin-bottom: 40px; }`n" +
"    .generic-badge { background: #eee; color: #333; border-radius: 4px; padding: 4px 10px; font-weight: bold; display: inline-block; }`n" +
"    .song-audio { margin-top: 15px; border-top: 1px solid #eee; padding-top: 10px; }`n" +
"    .song-audio audio { width: 100%; height: 32px; border-radius: 4px; }`n" +
"    /* Premium audio player styling */`n" +
"    .song-audio audio::-webkit-media-controls-enclosure { background-color: #f8f8f8; }`n" +
"    .song-audio audio::-webkit-media-controls-panel { background-color: #f8f8f8; }`n" +
"    .song-tab-btn { background: #fff; border: 2px solid #ddd; padding: 10px 20px; font-size: 1.1rem; font-weight: bold; cursor: pointer; border-radius: 5px; color: #333; transition: all 0.3s; }`n" +
"    .song-tab-btn.active, .song-tab-btn:hover { background: #ffcc00; border-color: #ffcc00; color: #111; }`n" +
"    .tab-content { display: none; }`n" +
"    .tab-content.active { display: block; }`n" +
"    .role-section { margin-bottom: 50px; }`n" +
"    .role-section h3 { font-size: 1.5rem; color: #111; border-bottom: 3px solid #ffcc00; padding-bottom: 8px; margin-bottom: 25px; display: inline-block; padding-right: 30px; }`n" +
"    .songs-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }`n" +
"  </style>`n" +
"</head>`n" +
"<body>`n" +
"<nav class='main-nav' id='mainNav'>`n" +
"  <div class='nav-inner'>`n" +
"    <a href='./index.html' class='nav-logo'>`n" +
"      <span class='nav-logo-main'>東京真隼</span>`n" +
"      <span class='nav-logo-sub'>TOKYO MACH</span>`n" +
"    </a>`n" +
"    <button class='hamburger' id='hamburger' aria-label='メニュー'>`n" +
"      <span></span><span></span><span></span>`n" +
"    </button>`n" +
"    <ul class='nav-links' id='navLinks'>`n" +
"      <li><a href='./index.html'>HOME</a></li>`n" +
"      <li><a href='./schedule.html'>日程</a></li>`n" +
"      <li><a href='./songs.html' class='active'>応援歌</a></li>`n" +
"      <li><a href='./gallery.html'>ギャラリー</a></li>`n" +
"      <li><a href='./faq.html'>Q&amp;A</a></li>`n" +
"      <li><a href='https://t.co/NuiNCqluh0' target='_blank' rel='noopener' class='nav-cta'>団員募集</a></li>`n" +
"    </ul>`n" +
"  </div>`n" +
"</nav>`n" +
"`n" +
"<section class='page-hero'>`n" +
"  <div class='page-hero-content'>`n" +
"    <span class='page-hero-label'>FIGHT SONGS</span>`n" +
"    <h1>応援歌</h1>`n" +
"    <p>2026シーズン 選手応援歌・チャンステーマ</p>`n" +
"  </div>`n" +
"</section>`n" +
"`n" +
"<section class='section'>`n" +
"  <div class='container'>`n" +
"    <div class='songs-nav'>`n" +
"      <button class='song-tab-btn active' data-tab='pitcher'>投手</button>`n" +
"      <button class='song-tab-btn' data-tab='fielder'>野手</button>`n" +
"      <button class='song-tab-btn' data-tab='chance'>チャンステーマ</button>`n" +
"      <button class='song-tab-btn' data-tab='multi'>マルチテーマ</button>`n" +
"    </div>"

$bot = "  </div>`n" +
"</section>`n" +
"`n" +
"<footer class='site-footer'>`n" +
"  <div class='footer-inner'>`n" +
"    <div class='footer-top'>`n" +
"      <div class='footer-brand'>`n" +
"        <div class='footer-logo'>東京真隼</div>`n" +
"        <p class='footer-tagline'>TOKYO MACH - 世界最強のホークス私設応援団</p>`n" +
"        <p class='footer-desc'>世界最強を目指し、<br>ビジターの地でホークスの勝利を叫ぶ。</p>`n" +
"      </div>`n" +
"      <div class='footer-links-grid'>`n" +
"        <div class='footer-col'>`n" +
"          <h4>メニュー</h4>`n" +
"          <ul>`n" +
"            <li><a href='./index.html'>HOME</a></li>`n" +
"            <li><a href='./schedule.html'>日程</a></li>`n" +
"            <li><a href='./songs.html'>応援歌</a></li>`n" +
"          </ul>`n" +
"        </div>`n" +
"        <div class=" + '"' + "footer-col" + '"' + ">`n" +
"          <h4>コンテンツ</h4>`n" +
"          <ul>`n" +
"            <li><a href='./gallery.html'>ギャラリー</a></li>`n" +
"            <li><a href='./faq.html'>Q&amp;A</a></li>`n" +
"            <li><a href='https://t.co/NuiNCqluh0' target='_blank' rel='noopener'>団員募集</a></li>`n" +
"          </ul>`n" +
"        </div>`n" +
"        <div class='footer-col'>`n" +
"          <h4>SNS</h4>`n" +
"          <ul>`n" +
"            <li><a href='https://x.com/tokyo_mach' target='_blank' rel='noopener'><i class='fab fa-x-twitter'></i> X (Twitter)</a></li>`n" +
"            <li><a href='https://www.instagram.com/tokyo_mach/' target='_blank' rel='noopener'><i class='fab fa-instagram'></i> Instagram</a></li>`n" +
"          </ul>`n" +
"        </div>`n" +
"      </div>`n" +
"    </div>`n" +
"    <div class='footer-bottom'>`n" +
"      <div class='footer-sns-icons'>`n" +
"        <a href='https://x.com/tokyo_mach' target='_blank' rel='noopener' aria-label='X'><i class='fab fa-x-twitter'></i></a>`n" +
"        <a href='https://www.instagram.com/tokyo_mach/' target='_blank' rel='noopener' aria-label='Instagram'><i class='fab fa-instagram'></i></a>`n" +
"      </div>`n" +
"      <p>&copy; 2026 東京真隼 TOKYO MACH. All Rights Reserved.</p>`n" +
"    </div>`n" +
"  </div>`n" +
"</footer>`n" +
"<script>`n" +
"document.getElementById('hamburger').addEventListener('click', function() {`n" +
"  this.classList.toggle('active');`n" +
"  document.getElementById('navLinks').classList.toggle('active');`n" +
"});`n" +
"window.addEventListener('scroll', () => {`n" +
"  const nav = document.getElementById('mainNav');`n" +
"  if (window.scrollY > 50) nav.classList.add('scrolled');`n" +
"  else nav.classList.remove('scrolled');`n" +
"});`n" +
"document.querySelectorAll('.song-tab-btn').forEach(btn => {`n" +
"  btn.addEventListener('click', () => {`n" +
"    document.querySelectorAll('.song-tab-btn').forEach(b => b.classList.remove('active'));`n" +
"    btn.classList.add('active');`n" +
"    document.querySelectorAll('.tab-content').forEach(w => w.classList.remove('active'));`n" +
"    document.getElementById('tab-' + btn.dataset.tab).classList.add('active');`n" +
"  });`n" +
"});`n" +
"</script>`n" +
"</body>`n" +
"</html>"

$mid = ""

# Pitcher tab
$mid += "<div class='tab-content active' id='tab-pitcher'>`n"
$mid += "  <div class='role-section'>`n"
$mid += "    <div class='songs-grid'>`n"
$mid += (Format-Song $pitchers) + "`n"
$mid += (Format-Song $pitchers_general $true) + "`n"
$mid += "    </div>`n  </div>`n"
$mid += "</div>`n"

# Fielder tab
$mid += "<div class='tab-content' id='tab-fielder'>`n"
$mid += "  <div class='role-section'><h3>捕手</h3><div class='songs-grid'>" + (Format-Song $catchers) + "</div></div>`n"
$mid += "  <div class='role-section'><h3>内野手</h3><div class='songs-grid'>" + (Format-Song $infielders) + "</div></div>`n"
$mid += "  <div class='role-section'><h3>外野手</h3><div class='songs-grid'>" + (Format-Song $outfielders) + "</div></div>`n"
$mid += "  <div class='role-section'><h3>汎用</h3><div class='songs-grid'>" + (Format-Song $fielders_general $true) + "</div></div>`n"
$mid += "</div>`n"

# Chance tab
$mid += "<div class='tab-content' id='tab-chance'>`n"
$mid += "  <div class='role-section'>`n"
$mid += "    <div class='songs-grid'>`n"
$mid += (Format-Song $chance_data $true) + "`n"
$mid += "    </div>`n  </div>`n"
$mid += "</div>`n"

# Multi theme tab
$mid += "<div class='tab-content' id='tab-multi'>`n"
$mid += "  <div class='role-section'>`n"
$mid += "    <div class='songs-grid'>`n"
$mid += (Format-Song $multi_theme_data $true) + "`n"
$mid += "    </div>`n  </div>`n"
$mid += "</div>`n"

$finalHtml = $top + $mid + $bot
[System.IO.File]::WriteAllText("$PSScriptRoot\songs.html", $finalHtml, [System.Text.Encoding]::UTF8)
Write-Output "Done"
