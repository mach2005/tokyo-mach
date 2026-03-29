import os
DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DIR, '../HP/index.html'), 'r', encoding='utf-8') as f:
    index = f.read()

header_end = index.find('<!-- Hero Section -->')
header = index[:header_end]
footer_start = index.find('<footer class="site-footer">')
footer = index[footer_start:]

def make_page(filename, title, content):
    h = header.replace('<title>東京真隼 TOKYO MACH - ホークス私設応援団</title>',
                        f'<title>{title} - 東京真隼 TOKYO MACH</title>')
    full = h + content + '\n' + footer
    path = os.path.join(DIR, '../HP/', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(full)
    print(f'Created: ../HP/{filename}')

# ===== SCHEDULE PAGE =====
schedule_content = '''
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
'''

def cal_headers():
    return '''<div class="cal-header sun">日</div><div class="cal-header">月</div><div class="cal-header">火</div><div class="cal-header">水</div><div class="cal-header">木</div><div class="cal-header">金</div><div class="cal-header sat">土</div>'''

TEAM_LOGOS = {
    '日本ハム': 'https://npb.jp/img/common/logo/2026/logo_f_s.gif',
    '楽天': 'https://npb.jp/img/common/logo/2026/logo_e_s.gif',
    'ロッテ': 'https://npb.jp/img/common/logo/2026/logo_m_s.gif',
    '西武': 'https://npb.jp/img/common/logo/2026/logo_l_s.gif',
    'オリックス': 'https://npb.jp/img/common/logo/2026/logo_b_s.gif',
    '巨人': 'https://npb.jp/img/common/logo/2026/logo_g_s.gif',
    'ヤクルト': 'https://npb.jp/img/common/logo/2026/logo_s_s.gif',
    'DeNA': 'https://npb.jp/img/common/logo/2026/logo_db_s.gif',
    '中日': 'https://npb.jp/img/common/logo/2026/logo_d_s.gif',
    '阪神': 'https://npb.jp/img/common/logo/2026/logo_t_s.gif',
    '広島': 'https://npb.jp/img/common/logo/2026/logo_c_s.gif',
    'セントラル': 'https://npb.jp/img/common/logo/2026/logo_cl_s.gif',
    'パシフィック': 'https://npb.jp/img/common/logo/2026/logo_pl_s.gif'
}

def day(num, cls='', day_cls='', game=None):
    dc = f' {day_cls}' if day_cls else ''
    nc = f' {cls}' if cls else ''
    g = ''
    if game:
        gc = game.get('gc','visitor-game')
        # 新旧両方のキーに対応
        opp_name = game.get('opp_name', game.get('opp', '').replace('vs ', ''))
        logo_url = TEAM_LOGOS.get(opp_name, '')
        logo_img = f"<img src='{logo_url}' alt='{opp_name}' class='team-logo-img'> " if logo_url else ""
        g = f'<div class="game-info {gc}"><span class="game-opponent">{logo_img}{opp_name}</span>'
        if 'venue' in game: g += f'<span class="game-venue">{game["venue"]}</span>'
        if 'time' in game: g += f'<span class="game-time">{game["time"]}</span>'
        g += '</div>'
    return f'<div class="cal-day{dc}"><span class="day-num{nc}">{num}</span>{g}</div>'

def empty():
    return '<div class="cal-day empty"></div>'

def vg(opp_name, venue, time='18:00'):
    return {'opp_name': opp_name, 'opp': f'vs {opp_name}', 'venue': venue, 'time': time, 'gc': 'visitor-game'}

def hg(opp_name, venue='みずほPayPay', time='18:00'):
    # 福岡（PayPay）または北九州以外は「ビジター扱い（黄色）」にする
    is_fukuoka = any(x in venue for x in ['PayPay', '北九州'])
    gc = 'home-game' if is_fukuoka else 'visitor-game'
    return {'opp_name': opp_name, 'opp': f'vs {opp_name}', 'venue': venue, 'time': time, 'gc': gc}

def day_with_cls(num, cls='', game=None):
    # ゲームがある場合、そのクラスに合わせて day_cls も設定する
    day_cls = game.get('gc', '').replace('-game', '-day') if game else ''
    return day(num, cls, day_cls, game)

# 3月 オープン戦
schedule_content += f'''
<div class="calendar-wrapper" id="month-pre3" style="display:none;">
  <h3 class="calendar-month-title">2026年3月（オープン戦）</h3>
  <div class="calendar-grid">
    {cal_headers()}
    {day(1,'sun')}{day(2)}{day(3)}{day(4)}{day(5)}{day(6)}
    {day(7,'sat','visitor-day',vg('巨人','東京ドーム','14:00'))}
    {day(8,'sun','visitor-day',vg('巨人','東京ドーム','13:00'))}
    {day(9)}{day(10)}{day(11)}{day(12)}{day(13)}
    {day(14,'sat','visitor-day',vg('ヤクルト','神宮','14:00'))}
    {day(15,'sun','visitor-day',vg('ヤクルト','神宮','13:00'))}
    {day(16)}{day(17)}{day(18)}{day(19)}{day(20)}{day(21,'sat')}
    {day(22,'sun')}{day(23)}{day(24)}{day(25)}{day(26)}{day(27)}{day(28,'sat')}
    {day(29,'sun')}{day(30)}{day(31)}{empty()}{empty()}{empty()}{empty()}
  </div>
</div>
'''

# 3-4月
schedule_content += f'''
<div class="calendar-wrapper" id="month-3">
  <h3 class="calendar-month-title">2026年3月 - 4月</h3>
  <div class="calendar-grid">
    {cal_headers()}
    {empty()}{empty()}{empty()}{empty()}{empty()}
    {day(27,'','visitor-day',vg('楽天','楽天モバイル'))}
    {day(28,'sat','visitor-day',vg('楽天','楽天モバイル','14:00'))}
    {day(29,'sun','visitor-day',vg('楽天','楽天モバイル','13:00'))}
    {day(30)}{day(31,'','visitor-day',vg('西武','ベルーナ'))}
    {day(1,'','visitor-day',vg('西武','ベルーナ'))}
    {day(2,'','visitor-day',vg('西武','ベルーナ'))}
    {day(3)}
    {day(4,'sat','',hg('ロッテ'))}
    {day(5,'sun','',hg('ロッテ','PayPay','13:00'))}
    {day(6)}
    {day(7,'','visitor-day',vg('日本ハム','エスコン'))}
    {day(8,'','visitor-day',vg('日本ハム','エスコン'))}
    {day(9,'','visitor-day',vg('日本ハム','エスコン'))}
    {day(10)}
    {day(11,'sat','',hg('オリックス'))}
    {day(12,'sun','',hg('オリックス','PayPay','13:00'))}
    {day(13)}
    {day(14,'','visitor-day',vg('ロッテ','ZOZOマリン'))}
    {day(15,'','visitor-day',vg('ロッテ','ZOZOマリン'))}
    {day(16,'','visitor-day',vg('ロッテ','ZOZOマリン'))}
    {day(17)}
    {day(18,'sat','',hg('西武'))}
    {day(19,'sun','',hg('西武','PayPay','13:00'))}
    {day(20)}{day(21)}{day(22)}{day(23)}{day(24)}
    {day(25,'sat','',hg('楽天'))}
    {day(26,'sun','',hg('楽天','PayPay','13:00'))}
    {day(27)}
    {day(28,'','visitor-day',vg('オリックス','京セラ'))}
    {day(29,'','visitor-day',vg('オリックス','京セラ'))}
    {day(30,'','visitor-day',vg('オリックス','京セラ'))}
    {empty()}
  </div>
</div>
'''

# 5月
schedule_content += f'''
<div class="calendar-wrapper" id="month-5" style="display:none;">
  <h3 class="calendar-month-title">2026年5月</h3>
  <div class="calendar-grid">
    {cal_headers()}
    {empty()}{empty()}{empty()}{empty()}{empty()}
    {day(1,'','visitor-day',vg('楽天','楽天モバイル'))}
    {day(2,'sat','visitor-day',vg('楽天','楽天モバイル','14:00'))}
    {day(3,'sun','visitor-day',vg('楽天','楽天モバイル','13:00'))}
    {day(4)}
    {day(5,'','visitor-day',vg('西武','ベルーナ'))}
    {day(6,'','visitor-day',vg('西武','ベルーナ'))}
    {day(7)}{day(8)}
    {day(9,'sat','',hg('日本ハム'))}
    {day(10,'sun','',hg('日本ハム','PayPay','13:00'))}
    {day(11)}{day(12)}{day(13)}{day(14)}{day(15)}
    {day(16,'sat','',hg('ロッテ'))}
    {day(17,'sun','',hg('ロッテ','PayPay','13:00'))}
    {day(18)}
    {day(19,'','visitor-day',vg('DeNA','横浜'))}
    {day(20,'','visitor-day',vg('DeNA','横浜'))}
    {day(21,'','visitor-day',vg('DeNA','横浜'))}
    {day(22)}
    {day(23,'sat','visitor-day',vg('中日','バンテリン','14:00'))}
    {day(24,'sun','visitor-day',vg('中日','バンテリン','14:00'))}
    {day(25)}{day(26)}{day(27)}{day(28)}{day(29)}
    {day(30,'sat','',hg('オリックス'))}
    {day(31,'sun','',hg('オリックス','PayPay','13:00'))}
  </div>
</div>
'''

# 6月
schedule_content += f'''
<div class="calendar-wrapper" id="month-6" style="display:none;">
  <h3 class="calendar-month-title">2026年6月</h3>
  <div class="calendar-grid">
    {cal_headers()}
    {day(1)}
    {day_with_cls(2,'',vg('中日','バンテリン'))}
    {day_with_cls(3,'',vg('中日','バンテリン'))}
    {day_with_cls(4,'',vg('中日','バンテリン'))}
    {day_with_cls(5,'',vg('DeNA','横浜'))}
    {day_with_cls(6,'sat',vg('DeNA','横浜','14:00'))}
    {day_with_cls(7,'sun',vg('DeNA','横浜','13:00'))}
    {day(8)}
    {day_with_cls(9,'',hg('阪神'))}
    {day_with_cls(10,'',hg('阪神'))}
    {day_with_cls(11,'',hg('阪神'))}
    {day_with_cls(12,'',hg('ヤクルト'))}
    {day_with_cls(13,'sat',hg('ヤクルト','みずほPayPay','14:00'))}
    {day_with_cls(14,'sun',hg('ヤクルト','みずほPayPay','13:00'))}
    {day(15)}{day(16)}{day(17)}{day(18)}
    {day_with_cls(19,'',vg('日本ハム','エスコン'))}
    {day_with_cls(20,'sat',vg('日本ハム','エスコン','14:00'))}
    {day_with_cls(21,'sun',vg('日本ハム','エスコン','13:00'))}
    {day(22)}
    {day_with_cls(23,'',hg('オリックス'))}
    {day_with_cls(24,'',hg('オリックス'))}
    {day_with_cls(25,'',hg('オリックス'))}
    {day_with_cls(26,'',vg('ロッテ','ZOZOマリン'))}
    {day_with_cls(27,'sat',vg('ロッテ','ZOZOマリン'))}
    {day_with_cls(28,'sun',vg('ロッテ','ZOZOマリン','17:00'))}
    {day(29)}
    {day_with_cls(30,'',hg('西武','東京ドーム'))}
    {empty()}{empty()}{empty()}{empty()}{empty()}
  </div>
</div>
'''

# 7月
schedule_content += f'''
<div class="calendar-wrapper" id="month-7" style="display:none;">
  <h3 class="calendar-month-title">2026年7月</h3>
  <div class="calendar-grid">
    {cal_headers()}
    {empty()}{empty()}{empty()}
    {day(1,'','visitor-day',vg('巨人','東京ドーム'))}
    {day(2,'','visitor-day',vg('巨人','東京ドーム'))}
    {day(3,'','visitor-day',vg('巨人','東京ドーム'))}
    {day(4,'sat','',hg('オリックス'))}
    {day(5,'sun','',hg('オリックス','PayPay','13:00'))}
    {day(6)}
    {day(7,'','visitor-day',vg('西武','ベルーナ'))}
    {day(8,'','visitor-day',vg('西武','ベルーナ'))}
    {day(9,'','visitor-day',vg('西武','ベルーナ'))}
    {day(10)}
    {day(11,'sat','',hg('日本ハム'))}
    {day(12,'sun','',hg('日本ハム','PayPay','13:00'))}
    {day(13)}{day(14)}{day(15)}{day(16)}{day(17)}{day(18,'sat')}{day(19,'sun')}
    {day(20)}{day(21)}{day(22)}
    {day(23)}
    {day(24,'','visitor-day',vg('楽天','楽天モバイル'))}
    {day(25,'sat','visitor-day',vg('楽天','楽天モバイル','14:00'))}
    {day(26,'sun','visitor-day',vg('楽天','楽天モバイル','13:00'))}
    {day(27)}
    <div class='cal-day visitor-day'><span class='day-num'>28</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_cl_s.gif' alt='セ・リーグ' class='team-logo-img'> <span class='team-name'>セントラル</span></span><span class='game-venue'>東京ドーム</span><span class='game-time'>18:30</span></div></div>
    <div class='cal-day visitor-day'><span class='day-num'>29</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_cl_s.gif' alt='セ・リーグ' class='team-logo-img'> <span class='team-name'>セントラル</span></span><span class='game-venue'>富山市民球場</span><span class='game-time'>18:30</span></div></div>
    {day(30)}{day(31)}{empty()}
  </div>
</div>
'''

# 8月
schedule_content += f'''
<div class="calendar-wrapper" id="month-8" style="display:none;">
  <h3 class="calendar-month-title">2026年8月</h3>
  <div class="calendar-grid">
    {cal_headers()}
    {empty()}{empty()}{empty()}{empty()}{empty()}
    {day(1,'sat','',hg('西武','PayPay','18:00'))}
    {day(2,'sun','',hg('西武','PayPay','18:00'))}
    {day(3)}
    {day(4,'','visitor-day',vg('オリックス','京セラ'))}
    {day(5,'','visitor-day',vg('オリックス','京セラ'))}
    {day(6,'','visitor-day',vg('オリックス','京セラ'))}
    {day(7)}
    {day(8,'sat','',hg('ロッテ','PayPay','18:00'))}
    {day(9,'sun','',hg('ロッテ','PayPay','18:00'))}
    {day(10)}{day(11)}{day(12)}{day(13)}{day(14)}
    {day(15,'sat','',hg('日本ハム','PayPay','18:00'))}
    {day(16,'sun','',hg('日本ハム','PayPay','18:00'))}
    {day(17)}
    {day(18,'','visitor-day',vg('ロッテ','ZOZOマリン'))}
    {day(19,'','visitor-day',vg('ロッテ','ZOZOマリン'))}
    {day(20,'','visitor-day',vg('ロッテ','ZOZOマリン'))}
    {day(21)}
    {day(22,'sat','visitor-day',vg('日本ハム','エスコン','14:00'))}
    {day(23,'sun','visitor-day',vg('日本ハム','エスコン','13:00'))}
    {day(24)}
    {day(25,'','visitor-day',vg('楽天','楽天モバイル'))}
    {day(26,'','visitor-day',vg('楽天','楽天モバイル'))}
    {day(27)}{day(28)}
    {day(29,'sat','',hg('オリックス','PayPay','18:00'))}
    {day(30,'sun','',hg('オリックス','PayPay','18:00'))}
    {day(31)}
  </div>
</div>
'''

# 9月
schedule_content += f'''
<div class="calendar-wrapper" id="month-9" style="display:none;">
  <h3 class="calendar-month-title">2026年9月</h3>
  <div class="calendar-grid">
    {cal_headers()}
    {empty()}{empty()}
    {day(1,'','visitor-day',vg('西武','ベルーナ'))}
    {day(2,'','visitor-day',vg('西武','ベルーナ'))}
    {day(3,'','visitor-day',vg('西武','ベルーナ'))}
    {day(4)}
    {day(5,'sat','',hg('楽天'))}
    {day(6,'sun','',hg('楽天','PayPay','13:00'))}
    {day(7)}
    {day(8,'','visitor-day',vg('オリックス','京セラ'))}
    {day(9,'','visitor-day',vg('オリックス','京セラ'))}
    {day(10,'','visitor-day',vg('オリックス','京セラ'))}
    {day(11)}
    {day(12,'sat','',hg('ロッテ'))}
    {day(13,'sun','',hg('ロッテ','PayPay','13:00'))}
    {day(14)}
    {day(15,'','visitor-day',vg('日本ハム','エスコン'))}
    {day(16,'','visitor-day',vg('日本ハム','エスコン'))}
    {day(17,'','visitor-day',vg('日本ハム','エスコン'))}
    {day(18)}
    {day(19,'sat','',hg('西武'))}
    {day(20,'sun','',hg('西武','PayPay','13:00'))}
    {day(21)}{day(22)}{day(23)}{day(24)}{day(25)}
    {day(26,'sat','',hg('日本ハム'))}
    {day(27,'sun','',hg('日本ハム','PayPay','13:00'))}
    {day(28)}
    {day(29,'','visitor-day',vg('楽天','楽天モバイル'))}
    {day(30,'','visitor-day',vg('楽天','楽天モバイル'))}
    {empty()}{empty()}{empty()}
  </div>
</div>
'''

# 10-11月
def cs(label):
    return {'opp': label, 'gc': 'cs-info'}
def ns(label='日本シリーズ'):
    return {'opp': label, 'gc': 'ns-info'}

schedule_content += f'''
<div class="calendar-wrapper" id="month-10" style="display:none;">
  <h3 class="calendar-month-title">2026年10月 - 11月（CS・日本シリーズ）</h3>
  <div class="calendar-grid">
    {cal_headers()}
    {empty()}{empty()}{empty()}{empty()}
    {day(1)}{day(2)}{day(3,'sat')}
    {day(4,'sun')}{day(5)}{day(6)}{day(7)}{day(8)}{day(9)}
    <div class="cal-day cs-day"><span class="day-num sat">10</span><div class="game-info cs-info"><span class="game-opponent">CS 1st</span></div></div>
    <div class="cal-day cs-day"><span class="day-num sun">11</span><div class="game-info cs-info"><span class="game-opponent">CS 1st</span></div></div>
    <div class="cal-day cs-day"><span class="day-num">12</span><div class="game-info cs-info"><span class="game-opponent">CS 1st</span></div></div>
    {day(13)}
    <div class="cal-day cs-day"><span class="day-num">14</span><div class="game-info cs-info"><span class="game-opponent">CS Final</span></div></div>
    <div class="cal-day cs-day"><span class="day-num">15</span><div class="game-info cs-info"><span class="game-opponent">CS Final</span></div></div>
    <div class="cal-day cs-day"><span class="day-num">16</span><div class="game-info cs-info"><span class="game-opponent">CS Final</span></div></div>
    <div class="cal-day cs-day"><span class="day-num sat">17</span><div class="game-info cs-info"><span class="game-opponent">CS Final</span></div></div>
    <div class="cal-day cs-day"><span class="day-num sun">18</span><div class="game-info cs-info"><span class="game-opponent">CS Final</span></div></div>
    <div class="cal-day cs-day"><span class="day-num">19</span><div class="game-info cs-info"><span class="game-opponent">CS Final</span></div></div>
    {day(20)}{day(21)}{day(22)}{day(23)}
    <div class="cal-day"><span class="day-num sat">24</span><div class="game-info ns-info"><span class="game-opponent">日本シリーズ</span></div></div>
    <div class="cal-day"><span class="day-num sun">25</span><div class="game-info ns-info"><span class="game-opponent">日本シリーズ</span></div></div>
    {day(26)}
    <div class="cal-day"><span class="day-num">27</span><div class="game-info ns-info"><span class="game-opponent">日本シリーズ</span></div></div>
    <div class="cal-day"><span class="day-num">28</span><div class="game-info ns-info"><span class="game-opponent">日本シリーズ</span></div></div>
    <div class="cal-day"><span class="day-num">29</span><div class="game-info ns-info"><span class="game-opponent">日本シリーズ</span></div></div>
    {day(30)}
    <div class="cal-day"><span class="day-num sat">31</span><div class="game-info ns-info"><span class="game-opponent">日本シリーズ</span></div></div>
    <div class="cal-day"><span class="day-num sun">1</span><div class="game-info ns-info"><span class="game-opponent">日本シリーズ</span></div></div>
    {empty()}{empty()}{empty()}{empty()}{empty()}{empty()}
  </div>
</div>
'''

schedule_content += '''
  </div>
</section>
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
'''
make_page('schedule.html', '試合日程', schedule_content)

# ===== SONGS PAGE =====
songs_content = '''
<section class="page-hero">
  <div class="page-hero-content">
    <span class="page-hero-label">CHEER SONGS</span>
    <h1>応援歌</h1>
    <p>みんなで声を合わせて、選手を後押ししよう！</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="songs-nav">
      <button class="songs-tab active" data-target="pitchers">投手</button>
      <button class="songs-tab" data-target="batters">野手</button>
      <button class="songs-tab" data-target="chance">チャンステーマ</button>
    </div>
    <div class="songs-section active" id="pitchers">
      <h3 class="songs-category-title"><i class="fas fa-baseball-ball"></i> 投手応援歌</h3>
      <div class="songs-grid songs-grid-3col">
'''

pitchers = [
    (11,'有原 航平','風を切り裂け 有原<br>唸る剛腕 打ち砕け<br>勝利を掴め 有原航平'),
    (13,'東浜 巨','闘志を燃やせ 東浜<br>気迫の投球 見せつけろ<br>勝利をもぎ取れ 東浜巨'),
    (15,'スチュワート','力で抑えろ スチュワート<br>唸る速球 打者を斬れ<br>勝利へ導け スチュワート'),
    (16,'モイネロ','稲妻の如く モイネロ<br>鋭く攻めろ 三振奪え<br>守護神の誇り モイネロ'),
    (18,'大津 亮介','腕を振れ 大津<br>魂の一球 投げ込め<br>勝利を呼べ 大津亮介'),
    (29,'石川 柊太','気高く投げろ 石川<br>誇りを胸に マウンドへ<br>勝利を掴め 石川柊太'),
]
for num, name, lyrics in pitchers:
    songs_content += f'''
        <div class="song-card-compact common-card">
          <div class="song-header-compact">
            <span class="song-number">{num}</span>
            <span class="song-name">{name}</span>
          </div>
          <div class="song-lyrics-compact">{lyrics}</div>
        </div>'''

songs_content += '''
      </div>
    </div>
    <div class="songs-section" id="batters">
      <h3 class="songs-category-title"><i class="fas fa-baseball-ball"></i> 野手応援歌</h3>
      <div class="songs-grid songs-grid-3col">
'''

batters = [
    (1,'近藤 健介','打て打て 近藤<br>飛ばせ 遥か彼方<br>歓喜を呼べ 近藤健介'),
    (2,'今宮 健太','華麗に決めろ 今宮<br>守備の名手 ここにあり<br>走れ 打て 今宮健太'),
    (3,'柳田 悠岐','豪快に振り抜け ギータ<br>弾丸ライナー スタンドへ<br>轟け 柳田悠岐'),
    (7,'中村 晃','巧みに打て 中村<br>鮮やかなバッティング<br>輝け 中村晃'),
    (9,'甲斐 拓也','砲丸送球 甲斐<br>強肩で刺せ ランナー<br>打って守れ 甲斐拓也'),
    (24,'栗原 陵矢','勝負強く打て 栗原<br>ここ一番で 頼れる男<br>決めろ 栗原陵矢'),
    (32,'周東 佑京','電光石火 周東<br>誰にも止められない<br>走れ走れ 周東佑京'),
    (51,'上林 誠知','空高く打ち上げろ 上林<br>外野を越えろ 大きく<br>見せろ 上林誠知'),
    (65,'山川 穂高','どかんと一発 山川<br>アーチを架けろ スタンドへ<br>轟け 山川穂高'),
]
for num, name, lyrics in batters:
    songs_content += f'''
        <div class="song-card-compact common-card">
          <div class="song-header-compact">
            <span class="song-number">{num}</span>
            <span class="song-name">{name}</span>
          </div>
          <div class="song-lyrics-compact">{lyrics}</div>
        </div>'''

songs_content += '''
      </div>
    </div>
    <div class="songs-section" id="chance">
      <h3 class="songs-category-title"><i class="fas fa-fire"></i> チャンステーマ</h3>
'''

chance_themes = [
    ('チャンステーマ1','かっ飛ばせー（選手名）！<br>それゆけ ホークス<br>勝利をつかめ 今こそ<br>燃えろ 俺たちのホークス'),
    ('チャンステーマ2','行くぞ ホークス<br>チャンスだ 攻めろ<br>俺たちの声で 押し出せ<br>さぁ行こう 勝利の道を'),
    ('チャンステーマ3','燃えろよ ホークス<br>今がその時だ<br>一打に懸けろ 魂を<br>栄光を掴め ホークス'),
]
for name, lyrics in chance_themes:
    songs_content += f'''
      <div class="song-card chance-card">
        <div class="song-header"><span class="song-name">{name}</span></div>
        <div class="song-lyrics">{lyrics}</div>
      </div>'''

songs_content += '''
    </div>
  </div>
</section>
<script>
document.querySelectorAll('.songs-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.songs-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    document.querySelectorAll('.songs-section').forEach(s => s.classList.remove('active'));
    document.getElementById(tab.dataset.target).classList.add('active');
  });
});
</script>
'''
make_page('songs.html', '応援歌', songs_content)

# ===== GALLERY PAGE =====
gallery_items = [
    ('fa-bullhorn','応援風景'), ('fa-train','遠征の様子'), ('fa-users','集合写真'),
    ('fa-music','トランペット演奏'), ('fa-flag','旗振り応援'), ('fa-drum','太鼓パフォーマンス'),
    ('fa-trophy','勝利の瞬間'), ('fa-utensils','遠征グルメ'), ('fa-heart','ファン交流'),
]
gallery_cards = ''
for icon, cap in gallery_items:
    gallery_cards += f'''
      <div class="gallery-card">
        <div class="gallery-placeholder"><i class="fas {icon}"></i></div>
        <div class="gallery-caption">{cap}</div>
      </div>'''

gallery_content = f'''
<section class="page-hero">
  <div class="page-hero-content">
    <span class="page-hero-label">GALLERY</span>
    <h1>ギャラリー</h1>
    <p>東京真隼の活動の様子をお届けします</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <p class="gallery-intro">最新の活動写真は <a href="https://www.instagram.com/tokyo_mach/" target="_blank" rel="noopener">Instagram (@tokyo_mach)</a> でも公開中！</p>
    <div class="gallery-grid">{gallery_cards}
    </div>
    <div class="gallery-sns-cta">
      <p>もっと写真を見たい方はSNSをチェック！</p>
      <div class="gallery-sns-links">
        <a href="https://x.com/tokyo_mach" target="_blank" rel="noopener" class="btn btn-dark"><i class="fab fa-x-twitter"></i> X (Twitter)</a>
        <a href="https://www.instagram.com/tokyo_mach/" target="_blank" rel="noopener" class="btn btn-gradient"><i class="fab fa-instagram"></i> Instagram</a>
      </div>
    </div>
  </div>
</section>
'''
make_page('gallery.html', 'ギャラリー', gallery_content)

# ===== FAQ PAGE =====
faqs = [
    ('東京真隼とはどんな団体ですか？','東京真隼（TOKYO MACH）は、福岡ソフトバンクホークスの私設応援団です。主にビジター球場（関東圏を中心に、北海道から広島まで）でホークスを応援しています。トランペット・太鼓・旗振り・リードによる本格的な応援を行っています。'),
    ('誰でも入団できますか？','はい！年齢・性別・経験を問わず、ホークスが好きな方なら誰でも入団できます。トランペットや太鼓の経験がなくても、入団後に先輩団員が丁寧に指導します。'),
    ('入団にかかる費用はありますか？','入団費・年会費などの団費は一切いただいておりません。試合のチケット代・交通費・宿泊費等は一般の観戦ファンと同様、自己負担となります。'),
    ('どこで活動していますか？','北海道（エスコン）から広島（マツダスタジアム）まで、全国のビジター球場で活動しています。関東圏の試合（西武球場、ZOZOマリン、東京ドーム、横浜スタジアムなど）が特に多いです。'),
    ('毎試合参加しないといけませんか？','いいえ、毎試合の参加は必須ではありません。ご自身の都合に合わせて、参加できる試合に参加していただければ大丈夫です。お気軽にご参加ください。'),
    ('見学はできますか？','はい、大歓迎です！実際の応援の様子を見てから入団を検討していただくことも可能です。見学希望の方は、X (Twitter) のDMまたは応募フォームからご連絡ください。'),
    ('球団公式の応援団ですか？','いいえ、東京真隼は「私設」応援団です。球団公式の応援団とは異なりますが、球団のルールおよびマナーを遵守して活動しています。'),
    ('どうやって応募すればいいですか？','下記の応募フォームからお申し込みいただくか、X (Twitter) の <a href="https://x.com/tokyo_mach" target="_blank" rel="noopener">@tokyo_mach</a> にDMをお送りください。お気軽にご連絡ください！'),
]
faq_items = ''
for q, a in faqs:
    faq_items += f'''
      <div class="faq-item">
        <button class="faq-question"><span>{q}</span><i class="fas fa-chevron-down"></i></button>
        <div class="faq-answer"><p>{a}</p></div>
      </div>'''

faq_content = f'''
<section class="page-hero">
  <div class="page-hero-content">
    <span class="page-hero-label">FAQ</span>
    <h1>Q&amp;A</h1>
    <p>よくあるご質問をまとめました</p>
  </div>
</section>
<section class="section">
  <div class="container container-narrow">
    <div class="faq-list">{faq_items}
    </div>
    <div class="faq-cta">
      <p>入団を希望される方は<br>下記フォームよりお申し込みください</p>
      <div class="faq-cta-buttons">
        <a href="https://t.co/NuiNCqluh0" target="_blank" rel="noopener" class="btn btn-primary btn-lg"><i class="fas fa-paper-plane"></i> 応募フォーム</a>
      </div>
    </div>
  </div>
</section>
<script>
document.querySelectorAll('.faq-question').forEach(btn => {{
  btn.addEventListener('click', () => {{
    const item = btn.closest('.faq-item');
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
  }});
}});
</script>
'''
make_page('faq.html', 'Q&A', faq_content)

print('\\nAll pages built successfully!')
