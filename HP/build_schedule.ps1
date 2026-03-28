$idx = Get-Content "$PSScriptRoot\index.html" -Raw -Encoding UTF8
$heroIdx = $idx.IndexOf('<!-- Hero Section -->')
$footerIdx = $idx.IndexOf('<footer class="site-footer">')
$header = $idx.Substring(0, $heroIdx).Replace('<title>東京真隼 TOKYO MACH - ホークス私設応援団</title>','<title>試合日程 - 東京真隼 TOKYO MACH</title>')
$footer = $idx.Substring($footerIdx)

function CalH { return '<div class="cal-header sun">日</div><div class="cal-header">月</div><div class="cal-header">火</div><div class="cal-header">水</div><div class="cal-header">木</div><div class="cal-header">金</div><div class="cal-header sat">土</div>' }
function E { return '<div class="cal-day empty"></div>' }
function D($n,$c='') { return "<div class=""cal-day""><span class=""day-num $c"">$n</span></div>" }
function VG($n,$c,$opp,$ven,$tm='18:00') { return "<div class=""cal-day visitor-day""><span class=""day-num $c"">$n</span><div class=""game-info visitor-game""><span class=""game-opponent"">vs $opp</span><span class=""game-venue"">$ven</span><span class=""game-time"">$tm</span></div></div>" }
function HG($n,$c,$opp,$ven='PayPay',$tm='14:00') { return "<div class=""cal-day""><span class=""day-num $c"">$n</span><div class=""game-info home-game""><span class=""game-opponent"">vs $opp</span><span class=""game-venue"">$ven</span><span class=""game-time"">$tm</span></div></div>" }

$pageHero = @'
<section class="page-hero">
  <div class="page-hero-content">
    <span class="page-hero-label">SCHEDULE</span>
    <h1>試合日程</h1>
    <p>2026シーズン ホークス試合日程</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="schedule-nav">
      <button class="schedule-month-btn" data-month="pre3">3月</button>
      <button class="schedule-month-btn active" data-month="3">3-4月</button>
      <button class="schedule-month-btn" data-month="5">5月</button>
      <button class="schedule-month-btn" data-month="6">6月</button>
      <button class="schedule-month-btn" data-month="7">7月</button>
      <button class="schedule-month-btn" data-month="8">8月</button>
      <button class="schedule-month-btn" data-month="9">9月</button>
      <button class="schedule-month-btn" data-month="10">10-11月</button>
    </div>
    <p class="schedule-legend">
      <span class="legend-item"><span class="legend-dot visitor"></span>ビジター</span>
      <span class="legend-item"><span class="legend-dot home"></span>ホーム</span>
    </p>
'@

# pre3
$pre3 = '<div class="calendar-wrapper" id="month-pre3" style="display:none;"><h3 class="calendar-month-title">2026年3月（オープン戦）</h3><div class="calendar-grid">'
$pre3 += CalH
$pre3 += (D 1 'sun')+(D 2)+(D 3)+(D 4)+(D 5)+(D 6)
$pre3 += (VG 7 'sat' '巨人' '東京ドーム' '14:00')+(VG 8 'sun' '巨人' '東京ドーム' '13:00')
$pre3 += (D 9)+(D 10)+(D 11)+(D 12)+(D 13)
$pre3 += (VG 14 'sat' 'ヤクルト' '神宮' '14:00')+(VG 15 'sun' 'ヤクルト' '神宮' '13:00')
$pre3 += (D 16)+(D 17)+(D 18)+(D 19)+(D 20)+(D 21 'sat')
$pre3 += (D 22 'sun')+(D 23)+(D 24)+(D 25)+(D 26)+(D 27)+(D 28 'sat')
$pre3 += (D 29 'sun')+(D 30)+(D 31)+(E)+(E)+(E)+(E)
$pre3 += '</div></div>'

# 3-4
$m3 = '<div class="calendar-wrapper" id="month-3"><h3 class="calendar-month-title">2026年3月 - 4月</h3><div class="calendar-grid">'
$m3 += CalH
$m3 += (E)+(E)+(E)+(E)+(E)
$m3 += (VG 27 '' '楽天' '楽天モバイル')+(VG 28 'sat' '楽天' '楽天モバイル' '14:00')
$m3 += (VG 29 'sun' '楽天' '楽天モバイル' '13:00')+(D 30)+(VG 31 '' '西武' 'ベルーナ')
$m3 += (VG 1 '' '西武' 'ベルーナ')+(VG 2 '' '西武' 'ベルーナ')+(D 3)
$m3 += (HG 4 'sat' 'ロッテ')+(HG 5 'sun' 'ロッテ' 'PayPay' '13:00')+(D 6)
$m3 += (VG 7 '' '日本ハム' 'エスコン')+(VG 8 '' '日本ハム' 'エスコン')+(VG 9 '' '日本ハム' 'エスコン')+(D 10)
$m3 += (HG 11 'sat' 'オリックス')+(HG 12 'sun' 'オリックス' 'PayPay' '13:00')+(D 13)
$m3 += (VG 14 '' 'ロッテ' 'ZOZOマリン')+(VG 15 '' 'ロッテ' 'ZOZOマリン')+(VG 16 '' 'ロッテ' 'ZOZOマリン')+(D 17)
$m3 += (HG 18 'sat' '西武')+(HG 19 'sun' '西武' 'PayPay' '13:00')
$m3 += (D 20)+(D 21)+(D 22)+(D 23)+(D 24)
$m3 += (HG 25 'sat' '楽天')+(HG 26 'sun' '楽天' 'PayPay' '13:00')+(D 27)
$m3 += (VG 28 '' 'オリックス' '京セラ')+(VG 29 '' 'オリックス' '京セラ')+(VG 30 '' 'オリックス' '京セラ')+(E)
$m3 += '</div></div>'

# 5
$m5 = '<div class="calendar-wrapper" id="month-5" style="display:none;"><h3 class="calendar-month-title">2026年5月</h3><div class="calendar-grid">'
$m5 += CalH
$m5 += (E)+(E)+(E)+(E)+(E)
$m5 += (VG 1 '' '楽天' '楽天モバイル')+(VG 2 'sat' '楽天' '楽天モバイル' '14:00')
$m5 += (VG 3 'sun' '楽天' '楽天モバイル' '13:00')+(D 4)
$m5 += (VG 5 '' '西武' 'ベルーナ')+(VG 6 '' '西武' 'ベルーナ')+(D 7)+(D 8)
$m5 += (HG 9 'sat' '日本ハム')+(HG 10 'sun' '日本ハム' 'PayPay' '13:00')
$m5 += (D 11)+(D 12)+(D 13)+(D 14)+(D 15)
$m5 += (HG 16 'sat' 'ロッテ')+(HG 17 'sun' 'ロッテ' 'PayPay' '13:00')+(D 18)
$m5 += (VG 19 '' 'DeNA' '横浜')+(VG 20 '' 'DeNA' '横浜')+(VG 21 '' 'DeNA' '横浜')+(D 22)
$m5 += (VG 23 'sat' '中日' 'バンテリン' '14:00')+(VG 24 'sun' '中日' 'バンテリン' '14:00')
$m5 += (D 25)+(D 26)+(D 27)+(D 28)+(D 29)
$m5 += (HG 30 'sat' 'オリックス')+(HG 31 'sun' 'オリックス' 'PayPay' '13:00')
$m5 += '</div></div>'

# 6
$m6 = '<div class="calendar-wrapper" id="month-6" style="display:none;"><h3 class="calendar-month-title">2026年6月</h3><div class="calendar-grid">'
$m6 += CalH
$m6 += (D 1)+(VG 2 '' '日本ハム' 'エスコン')+(VG 3 '' '日本ハム' 'エスコン')+(VG 4 '' '日本ハム' 'エスコン')+(D 5)
$m6 += (HG 6 'sat' '西武')+(HG 7 'sun' '西武' 'PayPay' '13:00')+(D 8)
$m6 += (VG 9 '' '広島' 'マツダ')+(VG 10 '' '広島' 'マツダ')+(VG 11 '' '広島' 'マツダ')+(D 12)
$m6 += (VG 13 'sat' '阪神' '甲子園' '14:00')+(VG 14 'sun' '阪神' '甲子園' '14:00')
$m6 += (D 15)+(D 16)+(D 17)+(D 18)+(D 19)
$m6 += (HG 20 'sat' 'ロッテ')+(HG 21 'sun' 'ロッテ' 'PayPay' '13:00')+(D 22)
$m6 += (VG 23 '' 'ロッテ' 'ZOZOマリン')+(VG 24 '' 'ロッテ' 'ZOZOマリン')+(VG 25 '' 'ロッテ' 'ZOZOマリン')+(D 26)
$m6 += (HG 27 'sat' '楽天')+(HG 28 'sun' '楽天' 'PayPay' '13:00')+(D 29)+(D 30)+(E)+(E)+(E)+(E)
$m6 += '</div></div>'

# 7
$m7 = '<div class="calendar-wrapper" id="month-7" style="display:none;"><h3 class="calendar-month-title">2026年7月</h3><div class="calendar-grid">'
$m7 += CalH
$m7 += (E)+(E)+(E)
$m7 += (VG 1 '' '巨人' '東京ドーム')+(VG 2 '' '巨人' '東京ドーム')+(VG 3 '' '巨人' '東京ドーム')
$m7 += (HG 4 'sat' 'オリックス')+(HG 5 'sun' 'オリックス' 'PayPay' '13:00')+(D 6)
$m7 += (VG 7 '' '西武' 'ベルーナ')+(VG 8 '' '西武' 'ベルーナ')+(VG 9 '' '西武' 'ベルーナ')+(D 10)
$m7 += (HG 11 'sat' '日本ハム')+(HG 12 'sun' '日本ハム' 'PayPay' '13:00')
$m7 += (D 13)+(D 14)+(D 15)+(D 16)+(D 17)+(D 18 'sat')+(D 19 'sun')+(D 20)
$m7 += '<div class="cal-day"><span class="day-num allstar">21</span><div class="game-info allstar-info"><span class="game-opponent">オールスター</span></div></div>'
$m7 += '<div class="cal-day"><span class="day-num allstar">22</span><div class="game-info allstar-info"><span class="game-opponent">オールスター</span></div></div>'
$m7 += (D 23)+(VG 24 '' '楽天' '楽天モバイル')+(VG 25 'sat' '楽天' '楽天モバイル' '14:00')+(VG 26 'sun' '楽天' '楽天モバイル' '13:00')
$m7 += (D 27)+(D 28)+(D 29)+(D 30)+(D 31)+(E)
$m7 += '</div></div>'

# 8
$m8 = '<div class="calendar-wrapper" id="month-8" style="display:none;"><h3 class="calendar-month-title">2026年8月</h3><div class="calendar-grid">'
$m8 += CalH
$m8 += (E)+(E)+(E)+(E)+(E)
$m8 += (HG 1 'sat' '西武' 'PayPay' '18:00')+(HG 2 'sun' '西武' 'PayPay' '18:00')+(D 3)
$m8 += (VG 4 '' 'オリックス' '京セラ')+(VG 5 '' 'オリックス' '京セラ')+(VG 6 '' 'オリックス' '京セラ')+(D 7)
$m8 += (HG 8 'sat' 'ロッテ' 'PayPay' '18:00')+(HG 9 'sun' 'ロッテ' 'PayPay' '18:00')
$m8 += (D 10)+(D 11)+(D 12)+(D 13)+(D 14)
$m8 += (HG 15 'sat' '日本ハム' 'PayPay' '18:00')+(HG 16 'sun' '日本ハム' 'PayPay' '18:00')+(D 17)
$m8 += (VG 18 '' 'ロッテ' 'ZOZOマリン')+(VG 19 '' 'ロッテ' 'ZOZOマリン')+(VG 20 '' 'ロッテ' 'ZOZOマリン')+(D 21)
$m8 += (VG 22 'sat' '日本ハム' 'エスコン' '14:00')+(VG 23 'sun' '日本ハム' 'エスコン' '13:00')+(D 24)
$m8 += (VG 25 '' '楽天' '楽天モバイル')+(VG 26 '' '楽天' '楽天モバイル')+(D 27)+(D 28)
$m8 += (HG 29 'sat' 'オリックス' 'PayPay' '18:00')+(HG 30 'sun' 'オリックス' 'PayPay' '18:00')+(D 31)
$m8 += '</div></div>'

# 9
$m9 = '<div class="calendar-wrapper" id="month-9" style="display:none;"><h3 class="calendar-month-title">2026年9月</h3><div class="calendar-grid">'
$m9 += CalH
$m9 += (E)+(E)
$m9 += (VG 1 '' '西武' 'ベルーナ')+(VG 2 '' '西武' 'ベルーナ')+(VG 3 '' '西武' 'ベルーナ')+(D 4)
$m9 += (HG 5 'sat' '楽天')+(HG 6 'sun' '楽天' 'PayPay' '13:00')+(D 7)
$m9 += (VG 8 '' 'オリックス' '京セラ')+(VG 9 '' 'オリックス' '京セラ')+(VG 10 '' 'オリックス' '京セラ')+(D 11)
$m9 += (HG 12 'sat' 'ロッテ')+(HG 13 'sun' 'ロッテ' 'PayPay' '13:00')+(D 14)
$m9 += (VG 15 '' '日本ハム' 'エスコン')+(VG 16 '' '日本ハム' 'エスコン')+(VG 17 '' '日本ハム' 'エスコン')+(D 18)
$m9 += (HG 19 'sat' '西武')+(HG 20 'sun' '西武' 'PayPay' '13:00')
$m9 += (D 21)+(D 22)+(D 23)+(D 24)+(D 25)
$m9 += (HG 26 'sat' '日本ハム')+(HG 27 'sun' '日本ハム' 'PayPay' '13:00')+(D 28)
$m9 += (VG 29 '' '楽天' '楽天モバイル')+(VG 30 '' '楽天' '楽天モバイル')+(E)+(E)+(E)
$m9 += '</div></div>'

# 10-11
function CS($n,$c,$lbl) { return "<div class=""cal-day cs-day""><span class=""day-num $c"">$n</span><div class=""game-info cs-info""><span class=""game-opponent"">$lbl</span></div></div>" }
function NS($n,$c) { return "<div class=""cal-day""><span class=""day-num $c"">$n</span><div class=""game-info ns-info""><span class=""game-opponent"">日本シリーズ</span></div></div>" }

$m10 = '<div class="calendar-wrapper" id="month-10" style="display:none;"><h3 class="calendar-month-title">2026年10月 - 11月（CS・日本シリーズ）</h3><div class="calendar-grid">'
$m10 += CalH
$m10 += (E)+(E)+(E)+(E)+(D 1)+(D 2)+(D 3 'sat')
$m10 += (D 4 'sun')+(D 5)+(D 6)+(D 7)+(D 8)+(D 9)
$m10 += (CS 10 'sat' 'CS 1st')+(CS 11 'sun' 'CS 1st')+(CS 12 '' 'CS 1st')+(D 13)
$m10 += (CS 14 '' 'CS Final')+(CS 15 '' 'CS Final')+(CS 16 '' 'CS Final')
$m10 += (CS 17 'sat' 'CS Final')+(CS 18 'sun' 'CS Final')+(CS 19 '' 'CS Final')
$m10 += (D 20)+(D 21)+(D 22)+(D 23)
$m10 += (NS 24 'sat')+(NS 25 'sun')+(D 26)+(NS 27 '')+(NS 28 '')+(NS 29 '')+(D 30)
$m10 += (NS 31 'sat')+(NS 1 'sun')+(E)+(E)+(E)+(E)+(E)+(E)
$m10 += '</div></div>'

$script = @'
<script>
document.querySelectorAll('.schedule-month-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.schedule-month-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.calendar-wrapper').forEach(w => w.style.display = 'none');
    const target = document.getElementById('month-' + btn.dataset.month);
    if (target) target.style.display = 'block';
  });
});
</script>
'@

$body = $pageHero + $pre3 + $m3 + $m5 + $m6 + $m7 + $m8 + $m9 + $m10 + '</div></section>' + $script
$html = $header + $body + "`n" + $footer
[System.IO.File]::WriteAllText("$PSScriptRoot\schedule.html", $html, [System.Text.Encoding]::UTF8)
Write-Output "Created: schedule.html"
