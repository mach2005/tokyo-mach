import os
import re

# 2026 Season Player Data (Source of Truth)
PITCHERS = """10 上沢 直之;我らが待ち望む　勝利を手にする為　多彩な持ち球を 繰り出せ上沢
11 津森 宥紀;男勝負の時だ 思い切り投げ込め 気迫あふれる闘志で 勝利へ導け
16 東浜 巨;立ち向かえよ 勝利の為 この地に今輝いて 高み目指せ
19 大津 亮介;制球乱れなく 緩急手繰る腕 青き翼を広げ羽ばたけ 魅せろ多彩な魔球
39 尾形 崇斗;夢を賭けた マウンドで　尾形崇斗よ 今見せてやれ
40 杉山 一樹;高い位置から 速いボールで 敵を追い込み 勝利を掴め
47 大関 友久;ほとばしる汗の中 歓声を胸に秘め 男なら今ここで 勝つんだ大関
48 藤井 皓哉;辛い時を乗り超えて 来たぞ夢の舞台 心ひとつに腕を振り抜き 勝利へ導けよ
NEW!49 松本 晴;鍛えたその腕を 自信持って振り抜き 揺るがぬ覚悟胸に 松本晴輝け
NEW!53 大山 凌;魂込めて ボールを投げ込め 果敢に攻めて 勝利へ導け
66 松本 裕樹;胸元突き刺す 速い球みせ 決めろその球で 敵を討ち取れ
120 長谷川 威展;気迫溢れる その球で 行（ゆ）けよ威展 ひたむきに"""

PITCHERS_GEN = """右投手汎用;恐れるな 立ち向かえ 気持ち見せろ 仲間を信じて 全て賭け闘え
左投手汎用;抑えるチャンス 物にするぞ この腕で 必ず掴むぞ"""

CATCHERS = """12 嶺井 博希;高み目指す男よ 立ち上がれさぁ 嶺井博希今こそ 強く闘え
NEW!45 谷川原 健太;鋭い打球飛ばし 鋭い肩で魅せろ 今こそ本当（マジ）決めろよ さあ谷川原行（ゆ）け
62 海野 隆司;歓声背に受け 熱い想い胸に秘め 攻守に輝き 勝利へ導け"""

INFIELDERS = """0 川瀬 晃;風の如く駆け抜け グラブ捌き魅せるぜ 快音を響かせ バットも魅せるぜ
4 ジーター・ダウンズ;ラララ～ ジーター 君の出番だ（Let's go!!） オオオ～（オイ！）掴めVictory
5 山川 穂高;鮮烈な一打を 放てスタンドの彼方へ 一振りで決めるぞ 高く遠く飛ばせ
6 今宮 健太;生まれ持つセンス 風を切り走れ 空高く飛ばせ 柔らかなリストで
8 牧原 大成;みなぎるそのエナジー 轟け地の果てまで 縦横無尽に駆け抜け 男になれ
24 栗原 陵矢;輝く時だ 後世に語り継がれる 伝説を今から 作れよ栗原
99 野村 勇;ここで見せろ力強く 敵を凌駕する一撃 全速前進フルスピードで 勇ましく走れ"""

OUTFIELDERS = """3 近藤 健介;極めた技で 打球が冴え渡る 遥か夢追い求めて 頂へと進め
7 中村 晃;新たな扉を 今から開け 愛する男さ 中村晃
9 柳田 悠岐;光のような足と 突き刺すようなスロー いざ一振り決めて 輝け柳田
23 周東 佑京;【前奏】光のその先 切り拓け 鷹の勇者（ヒーロー） 【本編】たゆまぬ努力で さぁ時代を築け 志ひとつに 行けスピードソルジャー
31 正木 智也;狙い研ぎ澄まし 殊勲の一打を 高らかに放て 正木の一振りで
32 柳町 達;熾烈な争いを 勝ち上がる為 闘う男の一振り 華麗に打ち捌け
NEW!57 緒方 理貢;夢追いかけ 打て魂乗せ 行（い）けダイヤモンド駆け抜け 今緒方魅せろよ"""

FIELDERS_GEN = """右打者汎用;待ちわびた場所で 真の力を解け 限界超えるその日まで 夢の道繋げろ
左打者汎用;今舞台が出来たぞ お前が輝く 最高の瞬間 羽ばたけ"""

CHANCE = """アッチャン;【導入】\\n熱く燃えろ（選手名）×３\\n\\nラーララララララー\\nラーララララララー\\nここで決めて勝つんだ\\nそうだ俺達が\\n勝利の使者になろう\\nLet’s Go Let’s Go\\n\\n【本編】\\nチャンス チャンス 今チャンス\\n拳を挙げて オイオイオイ\\nチャンス チャンス 今チャンス\\n燃やせよ魂 オイオイオイ\\nチャンス チャンス 今チャンス\\nオー オイオイオイオイ\\nチャンス チャンス 今チャンス\\nオー そーれ\\n決めろ 決めろ （選手名）決めろ\\n燃えろ 燃えろ 熱く燃えろ（選手名）
押忍！チャンス;(お楽しみは) これからだー\\nワン ツー スリー フォー\\nオー よっしゃ行くぞ！\\n\\n行け行け行け行け 押せ押せ押せ押せ\\n撃て撃て撃て撃て 撃て 撃て（選手名）\\n行け行け行け行け 押せ押せ押せ押せ\\nオイオイオイオイ オイ オイ（選手名）\\n行け 行け 押せ 押せ\\nGo Go Let’s Go! Let’s Go （選手名）\\n行～け 押～せ オー よっしゃ行くぞ！
関東チャンス;【前奏】\\nオイオイオイ\\nオイオイオイ\\n突き放せ\\n\\n【本編】\\nかっとばせ（選手名） （選手名） ここで一発\\nかっとばせ（選手名） 狙えスタンドへ\\nかせかせ（選手名） かせかせ（選手名）\\nいざ行け （選手名）
北日本チャンス;【前奏】\\n野球場の中から\\nがんばれって言っている\\n激しく熱く\\n今ここで がんばれ！\\n\\n【本編】\\n燃える闘志今見せてやれ\\n（選手名）一振りで決めてやれ\\n勝利決まれば お前の夜だ\\n（選手名）（選手名）\\nいまここで がんばれ！
鷹の道;行けよ男たち チャンスだ燃え上がれ\\n俊足巧打で突き進め それが鷹の道
アッコちゃん;オーオーオー… そ～れ いけいけ\\nオーオーオー… そ～れ いけいけ\\n（選手名）～ 今こそ～ 戦え～\\さあ行こう 俺らならやれるさ\\n熱くなれ 男なら行こうぜ\\n（選手名）～ 今こそ～ 戦え～
オオサカツンデレラ;ラララララララララ…\\n（選手名）（選手名）（選手名）\\n（選手名）ラララー
令和;ウォイ！ウォイ！ウォイ！（選手名）\\n\\n今宵勝利の為に 俺ら叫び続ける\\n争覇期する時まで 此処にいる仲間と共に\\n\\nウォイ！ウォイ！ウォイ！（選手名）
藤本;わっしょいわっしょい 「選手名」\\nわっしょいわっしょい 「選手名」\\n行け！打て！ 「選手名」 熱くなれ！
若井;「選手名」 「選手名」 「選手名」\\n燃えろ燃えろ 「選手名」\\nかっ飛ばせ 「選手名」\\nチャンスに強いガッツマン 我らの 「選手名」\\nかっ飛ばせ 「選手名」
鷹の爪;【前奏】\\n勝利を掴みとれ 「選手名」\\n\\n【本編】\\n勝利に向かって突き進め 打ちまくれ～打ちまくれ～\\nお前の力を見せてくれ それ行け 「選手名」\\n\\n男性：ここで決めろ！\\n女性：ここで決めろ！\\n「選手名」"""

MULTI = """G.F.V (GO FOR VICTORY);【導入】\\nオイ × 2\\n\\n【本編】\\nラララーララーラーラー\\nラーラーラーラーラーラー\\n熱いそのハートで\\n突き進め\\n\\nラララーララーラーラー\\nラーラーラーラーラーラー\\n攻めまくれ 掴み取れ\\n今日の勝利を オイ！オイ！オイ！
勝利目指して;【導入】\\nオイ × 2\\n\\n【本編】\\n勝利目指して\\nオーーオーオオーオオーー\\n勝利目指して\\nオイ！オイ！オイ！オイ！\\n勝利目指して\\nオーーオーオオーオオーー\\n勝利目指して\\いざゆけ\\nホークス！ホークス！\\n絶対勝つぞ！ホークス！"""

# ===== HTML GENERATION LOGIC =====

def format_song(text, allow_theme=False):
    res = ""
    lines = text.strip().split('\n')
    for line in lines:
        line = line.strip()
        if not line: continue
        parts = line.split(';')
        if len(parts) < 2: continue
        
        title_raw = parts[0]
        lyrics_raw = parts[1]
        
        is_new = title_raw.startswith("NEW!")
        title_raw = title_raw.replace("NEW!", "")
        
        badge = ""
        if is_new: badge = "<span class='new-badge'>NEW</span>"
        
        lyrics = lyrics_raw.replace('\\n', '<br>').replace(' ', '<br>').replace('　', '<br>')
        
        m = re.match(r"^(\d+)\s+(.+)", title_raw)
        if m:
            num = m.group(1)
            name = m.group(2)
            header_html = f"<div class='song-num'>{num}</div><div class='song-name'>{name}</div>"
        else:
            if allow_theme:
                header_html = f"<div class='generic-badge'>{title_raw}</div>"
            else:
                header_html = f"<div class='song-num'>*</div><div class='song-name'>{title_raw}</div>"
        
        audio_html = ""
        audio_map = {
            "45": "../public/audio/45_tanigawara.aac",
            "49": "../public/audio/49_matsumoto_hare.m4a",
            "53": "../public/audio/53_oyama.m4a",
            "57": "../public/audio/57_ogata.m4a"
        }
        if m and m.group(1) in audio_map:
            audio_html = f"<div class='song-audio'><audio controls src='{audio_map[m.group(1)]}'></audio></div>"

        res += f"""
        <div class="song-card">
          <div class="song-header">
            {header_html}
            {badge}
          </div>
          <div class="song-lyrics">
            {lyrics}
          </div>
          {audio_html}
        </div>"""
    return res

DIR = os.path.dirname(os.path.abspath(__file__))

# Read Template from Index
with open(os.path.join(DIR, '../HP/index.html'), 'r', encoding='utf-8') as f:
    index = f.read()

# Common Styles for Audio & Card
extra_style = """
  <style>
    .songs-nav { display: flex; justify-content: center; gap: 10px; margin-bottom: 40px; border-bottom: 2px solid #eee; padding-bottom: 20px; flex-wrap: wrap; }
    .song-tab-btn { background: #fff; border: 2px solid #ddd; padding: 10px 20px; font-size: 1.1rem; font-weight: bold; cursor: pointer; border-radius: 5px; color: #333; transition: all 0.3s; }
    .song-tab-btn.active, .song-tab-btn:hover { background: #ffcc00; border-color: #ffcc00; color: #111; }
    .tab-content { display: none; }
    .tab-content.active { display: block; }
    .role-section { margin-bottom: 50px; }
    .role-section h3 { font-size: 1.5rem; color: #111; border-bottom: 3px solid #ffcc00; padding-bottom: 8px; margin-bottom: 25px; display: inline-block; padding-right: 30px; }
    .songs-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }
    .generic-badge { background: #eee; color: #333; border-radius: 4px; padding: 4px 10px; font-weight: bold; display: inline-block; }
    .song-audio { margin-top: 15px; border-top: 1px solid #eee; padding-top: 10px; }
    .song-audio audio { width: 100%; height: 32px; border-radius: 4px; }
    @media (max-width: 768px) { .songs-grid { grid-template-columns: 1fr; } }
  </style>
"""

# Base HTML Construction
# 1. Header (up to Hero Section)
header_end = index.find('<!-- Hero Section -->')
head_with_style = index[:index.find('</head>')] + extra_style + index[index.find('</head>'):header_end]
head_with_style = head_with_style.replace('<title>東京真隼 TOKYO MACH - ホークス私設応援団</title>',
                        '<title>応援歌 - 東京真隼 TOKYO MACH</title>')

# 2. Hero Section for Songs
hero_html = """
<section class="page-hero">
  <div class="page-hero-content">
    <span class="page-hero-label"> FIGHT SONGS</span>
    <h1>応援歌</h1>
    <p>2026シーズン 選手応援歌・チャンステーマ</p>
  </div>
</section>
"""

# 3. Footer
footer_start = index.find('<footer class="site-footer">')
footer = index[footer_start:]

# Content Tabs
mid = """
<section class="section">
  <div class="container">
    <div class="songs-nav">
      <button class="song-tab-btn active" data-tab="pitcher">投手</button>
      <button class="song-tab-btn" data-tab="fielder">野手</button>
      <button class="song-tab-btn" data-tab="chance">チャンステーマ</button>
      <button class="song-tab-btn" data-tab="multi">マルチテーマ</button>
    </div>
"""

# Tab Sections
mid += "    <div class='tab-content active' id='tab-pitcher'>\n"
mid += "      <div class='role-section'><div class='songs-grid'>\n" + format_song(PITCHERS) + format_song(PITCHERS_GEN, True) + "</div></div>\n"
mid += "    </div>\n"

mid += "    <div class='tab-content' id='tab-fielder'>\n"
mid += "      <div class='role-section'><h3>捕手</h3><div class='songs-grid'>" + format_song(CATCHERS) + "</div></div>\n"
mid += "      <div class='role-section'><h3>内野手</h3><div class='songs-grid'>" + format_song(INFIELDERS) + "</div></div>\n"
mid += "      <div class='role-section'><h3>外野手</h3><div class='songs-grid'>" + format_song(OUTFIELDERS) + "</div></div>\n"
mid += "      <div class='role-section'><h3>汎用</h3><div class='songs-grid'>" + format_song(FIELDERS_GEN, True) + "</div></div>\n"
mid += "    </div>\n"

mid += "    <div class='tab-content' id='tab-chance'>\n"
mid += "      <div class='role-section'><div class='songs-grid'>" + format_song(CHANCE, True) + "</div></div>\n"
mid += "    </div>\n"

mid += "    <div class='tab-content' id='tab-multi'>\n"
mid += "      <div class='role-section'><div class='songs-grid'>" + format_song(MULTI, True) + "</div></div>\n"
mid += "    </div>\n"

mid += """
  </div>
</section>

<script>
document.querySelectorAll('.song-tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.song-tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.tab-content').forEach(w => w.classList.remove('active'));
    document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
  });
});
</script>
"""

# Write Output
with open(os.path.join(DIR, '../HP/songs.html'), 'w', encoding='utf-8') as f:
    f.write(head_with_style + hero_html + mid + footer)

print("Generated ../HP/songs.html")
