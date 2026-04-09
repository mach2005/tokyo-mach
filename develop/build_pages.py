import os
import sys
DIR = os.path.dirname(os.path.abspath(__file__))
# 自作バックアップユーティリティを追加
sys.path.append(DIR)
import backup_util

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
    # backup_util.backup_file(path) # 自動バックアップを停止（セッション最終版のみ対応）
    print(f'Created: ../HP/{filename}')

# ===== SCHEDULE PAGE (Full Restoration Build #113) =====
schedule_content = r'''
<section class="page-hero">
  <div class="page-hero-content">
    <span class="page-hero-label">SCHEDULE</span>
    <h1>試合日程</h1>
    <p>2026シーズン ホークス試合日程</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class='schedule-nav-outer'>
      <div class='schedule-nav'>
        <button class='schedule-month-btn active' data-month='3'>3月</button>
        <button class='schedule-month-btn' data-month='4'>4月</button>
        <button class='schedule-month-btn' data-month='5'>5月</button>
        <button class='schedule-month-btn' data-month='6'>6月</button>
        <button class='schedule-month-btn' data-month='7'>7月</button>
        <button class='schedule-month-btn' data-month='8'>8月</button>
        <button class='schedule-month-btn' data-month='9'>9月</button>
        <button class='schedule-month-btn' data-month='10'>10月</button>
      </div>
    </div>
    <p class='schedule-legend'>
      <span class='legend-item'><span class='legend-dot visitor'></span>ビジター</span>
      <span class='legend-item'><span class='legend-dot home'></span>ホーム</span>
      <span class='legend-item'><span class='legend-dot other'></span>その他</span>
    </p>

    <div class="schedule-container">
      <button class="nav-arrow prev" id="prevMonth" aria-label="前の月"><i class="fas fa-chevron-left"></i><span class="nav-arrow-text"></span></button>
      <div class="schedule-slider" id="scheduleSlider">
        <div class='calendar-wrapper' id='month-3'>
      <h3 class='calendar-month-title'>2026年3月</h3>
      <div class='calendar-grid'>
        <div class='cal-header'>月</div><div class='cal-header'>火</div><div class='cal-header'>水</div><div class='cal-header'>木</div><div class='cal-header'>金</div><div class='cal-header sat'>土</div><div class='cal-header sun'>日</div>
        <div class='cal-day'><span class='day-num out-of-month'>23</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>24</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>25</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>26</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>27</span></div>
        <div class='cal-day'><span class='day-num sat out-of-month'>28</span></div>
        <div class='cal-day'><span class='day-num sun'>1</span></div>
        <div class='cal-day'><span class='day-num'>2</span></div>
        <div class='cal-day'><span class='day-num'>3</span></div>
        <div class='cal-day'><span class='day-num'>4</span></div>
        <div class='cal-day'><span class='day-num'>5</span></div>
        <div class='cal-day'><span class='day-num'>6</span></div>
        <div class='cal-day'><span class='day-num sat'>7</span></div>
        <div class='cal-day'><span class='day-num sun'>8</span></div>
        <div class='cal-day'><span class='day-num'>9</span></div>
        <div class='cal-day'><span class='day-num'>10</span></div>
        <div class='cal-day'><span class='day-num'>11</span></div>
        <div class='cal-day'><span class='day-num'>12</span></div>
        <div class='cal-day'><span class='day-num'>13</span></div>
        <div class='cal-day'><span class='day-num sat'>14</span></div>
        <div class='cal-day'><span class='day-num sun'>15</span></div>
        <div class='cal-day'><span class='day-num'>16</span></div>
        <div class='cal-day'><span class='day-num'>17</span></div>
        <div class='cal-day'><span class='day-num'>18</span></div>
        <div class='cal-day'><span class='day-num'>19</span></div>
        <div class='cal-day'><span class='day-num'>20</span></div>
        <div class='cal-day'><span class='day-num sat'>21</span></div>
        <div class='cal-day'><span class='day-num sun'>22</span></div>
        <div class='cal-day'><span class='day-num'>23</span></div>
        <div class='cal-day'><span class='day-num'>24</span></div>
        <div class='cal-day'><span class='day-num'>25</span></div>
        <div class='cal-day'><span class='day-num'>26</span></div>
        <div class='cal-day home-day'><span class='day-num'>27</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:30</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>28</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:30</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>29</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>30</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>31</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>16:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num out-of-month'>1</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num out-of-month'>2</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num out-of-month'>3</span></div>
        <div class='cal-day'><span class='day-num sat out-of-month'>4</span></div>
        <div class='cal-day'><span class='day-num sun out-of-month'>5</span></div>
      </div>
    </div>
    <div class='calendar-wrapper' id='month-4'>
      <h3 class='calendar-month-title'>2026年4月</h3>
      <div class='calendar-grid'>
        <div class='cal-header'>月</div><div class='cal-header'>火</div><div class='cal-header'>水</div><div class='cal-header'>木</div><div class='cal-header'>金</div><div class='cal-header sat'>土</div><div class='cal-header sun'>日</div>
        <div class='cal-day'><span class='day-num out-of-month'>30</span></div>
        <div class='cal-day visitor-day'><span class='day-num out-of-month'>31</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>16:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>1</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>2</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>3</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>4</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>5</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>6</span></div>
        <div class='cal-day home-day'><span class='day-num'>7</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>8</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>9</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day'><span class='day-num'>10</span></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>11</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>12</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>13</span></div>
        <div class='cal-day home-day'><span class='day-num'>14</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>15</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>16</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>北九州</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>17</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>18</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>19</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>20</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>21</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>22</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>23</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day'><span class='day-num'>24</span></div>
        <div class='cal-day home-day'><span class='day-num sat'>25</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>熊本</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>26</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>鹿児島</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day'><span class='day-num'>27</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>28</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>29</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day'><span class='day-num'>30</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>1</span></div>
        <div class='cal-day'><span class='day-num sat out-of-month'>2</span></div>
        <div class='cal-day'><span class='day-num sun out-of-month'>3</span></div>
      </div>
    </div>
    <div class='calendar-wrapper' id='month-5'>
      <h3 class='calendar-month-title'>2026年5月</h3>
      <div class='calendar-grid'>
        <div class='cal-header'>月</div><div class='cal-header'>火</div><div class='cal-header'>水</div><div class='cal-header'>木</div><div class='cal-header'>金</div><div class='cal-header sat'>土</div><div class='cal-header sun'>日</div>
        <div class='cal-day'><span class='day-num out-of-month'>27</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>28</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>29</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>30</span></div>
        <div class='cal-day home-day'><span class='day-num'>1</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>2</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>3</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>4</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>5</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>6</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>7</span></div>
        <div class='cal-day home-day'><span class='day-num'>8</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>9</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>10</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day'><span class='day-num'>11</span></div>
        <div class='cal-day home-day'><span class='day-num'>12</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>13</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day'><span class='day-num'>14</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>15</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>16</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>17</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>18</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>19</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>20</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day'><span class='day-num'>21</span></div>
        <div class='cal-day home-day'><span class='day-num'>22</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>23</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>24</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day'><span class='day-num'>25</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>26</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_g_s.gif' alt='巨人' class='team-logo-img'> 巨人</span><span class='game-venue'>東京ドーム</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>27</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_g_s.gif' alt='巨人' class='team-logo-img'> 巨人</span><span class='game-venue'>東京ドーム</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>28</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_g_s.gif' alt='巨人' class='team-logo-img'> 巨人</span><span class='game-venue'>東京ドーム</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>29</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_c_s.gif' alt='広島' class='team-logo-img'> 広島</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>30</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_c_s.gif' alt='広島' class='team-logo-img'> 広島</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>31</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_c_s.gif' alt='広島' class='team-logo-img'> 広島</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:00</span></div></div>
      </div>
    </div>
    <div class='calendar-wrapper' id='month-6'>
      <h3 class='calendar-month-title'>2026年6月</h3>
      <div class='calendar-grid'>
        <div class='cal-header'>月</div><div class='cal-header'>火</div><div class='cal-header'>水</div><div class='cal-header'>木</div><div class='cal-header'>金</div><div class='cal-header sat'>土</div><div class='cal-header sun'>日</div>
        <div class='cal-day'><span class='day-num'>1</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>2</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_d_s.gif' alt='中日' class='team-logo-img'> 中日</span><span class='game-venue'>バンテリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>3</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_d_s.gif' alt='中日' class='team-logo-img'> 中日</span><span class='game-venue'>バンテリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>4</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_d_s.gif' alt='中日' class='team-logo-img'> 中日</span><span class='game-venue'>バンテリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>5</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_db_s.gif' alt='DeNA' class='team-logo-img'> DeNA</span><span class='game-venue'>横浜</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>6</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_db_s.gif' alt='DeNA' class='team-logo-img'> DeNA</span><span class='game-venue'>横浜</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>7</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_db_s.gif' alt='DeNA' class='team-logo-img'> DeNA</span><span class='game-venue'>横浜</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>8</span></div>
        <div class='cal-day home-day'><span class='day-num'>9</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_t_s.gif' alt='阪神' class='team-logo-img'> 阪神</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>10</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_t_s.gif' alt='阪神' class='team-logo-img'> 阪神</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>11</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_t_s.gif' alt='阪神' class='team-logo-img'> 阪神</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>12</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_s_s.gif' alt='ヤクルト' class='team-logo-img'> ヤクルト</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>13</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_s_s.gif' alt='ヤクルト' class='team-logo-img'> ヤクルト</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>14</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_s_s.gif' alt='ヤクルト' class='team-logo-img'> ヤクルト</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>15</span></div>
        <div class='cal-day'><span class='day-num'>16</span></div>
        <div class='cal-day'><span class='day-num'>17</span></div>
        <div class='cal-day'><span class='day-num'>18</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>19</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>20</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>21</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>22</span></div>
        <div class='cal-day home-day'><span class='day-num'>23</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>24</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>25</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>26</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>27</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>28</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>17:00</span></div></div>
        <div class='cal-day'><span class='day-num'>29</span></div>
        <div class='cal-day other-day'><span class='day-num'>30</span><div class='game-info other-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>東京ドーム</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day'><span class='day-num out-of-month'>1</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>2</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>3</span></div>
        <div class='cal-day'><span class='day-num sat out-of-month'>4</span></div>
        <div class='cal-day'><span class='day-num sun out-of-month'>5</span></div>
      </div>
    </div>
    <div class='calendar-wrapper' id='month-7'>
      <h3 class='calendar-month-title'>2026年7月</h3>
      <div class='calendar-grid'>
        <div class='cal-header'>月</div><div class='cal-header'>火</div><div class='cal-header'>水</div><div class='cal-header'>木</div><div class='cal-header'>金</div><div class='cal-header sat'>土</div><div class='cal-header sun'>日</div>
        <div class='cal-day'><span class='day-num out-of-month'>29</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>30</span></div>
        <div class='cal-day home-day'><span class='day-num'>1</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>2</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>3</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>4</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>5</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:30</span></div></div>
        <div class='cal-day'><span class='day-num'>6</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>7</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>8</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day'><span class='day-num'>9</span></div>
        <div class='cal-day home-day'><span class='day-num'>10</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>11</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>12</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day'><span class='day-num'>13</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>14</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>15</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>16</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>17</span></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>18</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>19</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>20</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>17:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>21</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>22</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>23</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>24</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>25</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>26</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>17:00</span></div></div>
        <div class='cal-day'><span class='day-num'>27</span></div>
        <div class='cal-day other-day'><span class='day-num'>28</span><div class='game-info other-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_cl_s.gif' alt='セ・リーグ' class='team-logo-img'> <span class='team-name'>セントラル</span></span><span class='game-venue'>東京ドーム</span><span class='game-time'>18:30</span></div></div>
        <div class='cal-day other-day'><span class='day-num'>29</span><div class='game-info other-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_cl_s.gif' alt='セ・リーグ' class='team-logo-img'> <span class='team-name'>セントラル</span></span><span class='game-venue'>富山市民球場</span><span class='game-time'>18:30</span></div></div>
        <div class='cal-day'><span class='day-num'>30</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>31</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sat out-of-month'>1</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun out-of-month'>2</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>16:00</span></div></div>
      </div>
    </div>
    <div class='calendar-wrapper' id='month-8'>
      <h3 class='calendar-month-title'>2026年8月</h3>
      <div class='calendar-grid'>
        <div class='cal-header'>月</div><div class='cal-header'>火</div><div class='cal-header'>水</div><div class='cal-header'>木</div><div class='cal-header'>金</div><div class='cal-header sat'>土</div><div class='cal-header sun'>日</div>
        <div class='cal-day'><span class='day-num out-of-month'>27</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>28</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>29</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>30</span></div>
        <div class='cal-day visitor-day'><span class='day-num out-of-month'>31</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>1</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>2</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>16:00</span></div></div>
        <div class='cal-day'><span class='day-num'>3</span></div>
        <div class='cal-day other-day'><span class='day-num'>4</span><div class='game-info other-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>5</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>6</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>7</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>8</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>9</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>西武球場</span><span class='game-time'>17:00</span></div></div>
        <div class='cal-day'><span class='day-num'>10</span></div>
        <div class='cal-day home-day'><span class='day-num'>11</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>12</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>13</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>14</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>15</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>16</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>17</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>18</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>19</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>20</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day'><span class='day-num'>21</span></div>
        <div class='cal-day home-day'><span class='day-num sat'>22</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>23</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>24</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>25</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>26</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>27</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>ZOZOマリン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>28</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>29</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>30</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day'><span class='day-num'>31</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>1</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>2</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>3</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>4</span></div>
        <div class='cal-day'><span class='day-num sat out-of-month'>5</span></div>
        <div class='cal-day'><span class='day-num sun out-of-month'>6</span></div>
      </div>
    </div>
    <div class='calendar-wrapper' id='month-9'>
      <h3 class='calendar-month-title'>2026年9月</h3>
      <div class='calendar-grid'>
        <div class='cal-header'>月</div><div class='cal-header'>火</div><div class='cal-header'>水</div><div class='cal-header'>木</div><div class='cal-header'>金</div><div class='cal-header sat'>土</div><div class='cal-header sun'>日</div>
        <div class='cal-day'><span class='day-num out-of-month'>31</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>1</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>2</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>エスコン</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day'><span class='day-num'>3</span></div>
        <div class='cal-day home-day'><span class='day-num'>4</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>5</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>6</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day'><span class='day-num'>7</span></div>
        <div class='cal-day home-day'><span class='day-num'>8</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>9</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>10</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_f_s.gif' alt='日本ハム' class='team-logo-img'> 日本ハム</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day'><span class='day-num'>11</span></div>
        <div class='cal-day home-day'><span class='day-num sat'>12</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>13</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_m_s.gif' alt='ロッテ' class='team-logo-img'> ロッテ</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>13:30</span></div></div>
        <div class='cal-day'><span class='day-num'>14</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>15</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>16</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>17</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day'><span class='day-num'>18</span></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>19</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>20</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num'>21</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>楽天モバイル</span><span class='game-time'>13:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>22</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>23</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_l_s.gif' alt='西武' class='team-logo-img'> 西武</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day'><span class='day-num'>24</span></div>
        <div class='cal-day visitor-day'><span class='day-num'>25</span><div class='game-info visitor-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>京セラD大阪</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sat'>26</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_e_s.gif' alt='楽天' class='team-logo-img'> 楽天</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>18:00</span></div></div>
        <div class='cal-day home-day'><span class='day-num sun'>27</span><div class='game-info home-game'><span class='game-opponent'><img src='https://npb.jp/img/common/logo/2026/logo_b_s.gif' alt='オリックス' class='team-logo-img'> オリックス</span><span class='game-venue'>みずほPayPay</span><span class='game-time'>14:00</span></div></div>
        <div class='cal-day'><span class='day-num'>28</span></div>
        <div class='cal-day'><span class='day-num'>29</span></div>
        <div class='cal-day'><span class='day-num'>30</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>1</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>2</span></div>
        <div class='cal-day'><span class='day-num sat out-of-month'>3</span></div>
        <div class='cal-day'><span class='day-num sun out-of-month'>4</span></div>
      </div>
    </div>
    <div class='calendar-wrapper' id='month-10'>
      <h3 class='calendar-month-title'>2026年10月（ポストシーズン）</h3>
      <div class='calendar-grid'>
        <div class='cal-header'>月</div><div class='cal-header'>火</div><div class='cal-header'>水</div><div class='cal-header'>木</div><div class='cal-header'>金</div><div class='cal-header sat'>土</div><div class='cal-header sun'>日</div>
        <div class='cal-day'><span class='day-num out-of-month'>28</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>29</span></div>
        <div class='cal-day'><span class='day-num out-of-month'>30</span></div>
        <div class='cal-day'><span class='day-num'>1</span></div>
        <div class='cal-day'><span class='day-num'>2</span></div>
        <div class='cal-day'><span class='day-num sat'>3</span></div>
        <div class='cal-day'><span class='day-num sun'>4</span></div>
        <div class='cal-day'><span class='day-num'>5</span></div>
        <div class='cal-day'><span class='day-num'>6</span></div>
        <div class='cal-day'><span class='day-num'>7</span></div>
        <div class='cal-day'><span class='day-num'>8</span></div>
        <div class='cal-day'><span class='day-num'>9</span></div>
        <div class='cal-day other-day'><span class='day-num sat'>10</span><div class='game-info other-game'><span class='game-opponent'><span class='txt-desktop'>CS 1st</span><span class='txt-mobile'>CS1st</span></span><span class='game-venue'></span></div></div>
        <div class='cal-day other-day'><span class='day-num sun'>11</span><div class='game-info other-game'><span class='game-opponent'><span class='txt-desktop'>CS 1st</span><span class='txt-mobile'>CS1st</span></span><span class='game-venue'></span></div></div>
        <div class='cal-day other-day'><span class='day-num'>12</span><div class='game-info other-game'><span class='game-opponent'><span class='txt-desktop'>CS 1st</span><span class='txt-mobile'>CS1st</span></span><span class='game-venue'></span></div></div>
        <div class='cal-day'><span class='day-num'>13</span></div>
        <div class='cal-day other-day'><span class='day-num'>14</span><div class='game-info other-game'><span class='game-opponent'><span class='txt-desktop'>CS Final</span><span class='txt-mobile'>CS Fin</span></span><span class='game-venue'></span></div></div>
        <div class='cal-day other-day'><span class='day-num'>15</span><div class='game-info other-game'><span class='game-opponent'><span class='txt-desktop'>CS Final</span><span class='txt-mobile'>CS Fin</span></span><span class='game-venue'></span></div></div>
        <div class='cal-day other-day'><span class='day-num'>16</span><div class='game-info other-game'><span class='game-opponent'><span class='txt-desktop'>CS Final</span><span class='txt-mobile'>CS Fin</span></span><span class='game-venue'></span></div></div>
        <div class='cal-day other-day'><span class='day-num sat'>17</span><div class='game-info other-game'><span class='game-opponent'><span class='txt-desktop'>CS Final</span><span class='txt-mobile'>CS Fin</span></span><span class='game-venue'></span></div></div>
        <div class='cal-day other-day'><span class='day-num sun'>18</span><div class='game-info other-game'><span class='game-opponent'><span class='txt-desktop'>CS Final</span><span class='txt-mobile'>CS Fin</span></span><span class='game-venue'></span></div></div>
        <div class='cal-day other-day'><span class='day-num'>19</span><div class='game-info other-game'><span class='game-opponent'><span class='txt-desktop'>CS Final</span><span class='txt-mobile'>CS Fin</span></span><span class='game-venue'></span></div></div>
        <div class='cal-day'><span class='day-num'>20</span></div>
        <div class='cal-day'><span class='day-num'>21</span></div>
        <div class='cal-day'><span class='day-num'>22</span></div>
        <div class='cal-day'><span class='day-num'>23</span></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>24</span><div class='game-info visitor-game'><span class='game-opponent'><span class='txt-desktop'>日本S 第1戦</span><span class='txt-mobile'>日本S①</span></span><span class='game-venue'>セ本拠地</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>25</span><div class='game-info visitor-game'><span class='game-opponent'><span class='txt-desktop'>日本S 第2戦</span><span class='txt-mobile'>日本S②</span></span><span class='game-venue'>セ本拠地</span></div></div>
        <div class='cal-day'><span class='day-num'>26</span></div>
        <div class='cal-day home-day'><span class='day-num'>27</span><div class='game-info home-game'><span class='game-opponent'><span class='txt-desktop'>日本S 第3戦</span><span class='txt-mobile'>日本S③</span></span><span class='game-venue'>パ本拠地</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>28</span><div class='game-info home-game'><span class='game-opponent'><span class='txt-desktop'>日本S 第4戦</span><span class='txt-mobile'>日本S④</span></span><span class='game-venue'>パ本拠地</span></div></div>
        <div class='cal-day home-day'><span class='day-num'>29</span><div class='game-info home-game'><span class='game-opponent'><span class='txt-desktop'>日本S 第5戦</span><span class='txt-mobile'>日本S⑤</span></span><span class='game-venue'>パ本拠地</span></div></div>
        <div class='cal-day'><span class='day-num'>30</span></div>
        <div class='cal-day visitor-day'><span class='day-num sat'>31</span><div class='game-info visitor-game'><span class='game-opponent'><span class='txt-desktop'>日本S 第6戦</span><span class='txt-mobile'>日本S⑥</span></span><span class='game-venue'>セ本拠地</span></div></div>
        <div class='cal-day visitor-day'><span class='day-num sun'>1</span><div class='game-info visitor-game'><span class='game-opponent'><span class='txt-desktop'>日本S 第7戦</span><span class='txt-mobile'>日本S⑦</span></span><span class='game-venue'>セ本拠地</span></div></div>
      </div> <!-- closes month 10 -->
    </div> <!-- closes scheduleSlider -->
    <button class="nav-arrow next" id="nextMonth" aria-label="次の月"><span class="nav-arrow-text"></span><i class="fas fa-chevron-right"></i></button>
  </div> <!-- closes schedule-container -->
</div> <!-- closes container (line 48) -->
</section>

<script>
(function() {

document.getElementById('hamburger').addEventListener('click', function() {
  this.classList.toggle('active');
  document.getElementById('navLinks').classList.toggle('active');
});
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    document.getElementById('hamburger').classList.remove('active');
    document.getElementById('navLinks').classList.remove('active');
  });
});
window.addEventListener('scroll', () => {
  const nav = document.getElementById('mainNav');
  if (window.scrollY > 50) nav.classList.add('scrolled');
  else nav.classList.remove('scrolled');
});
document.querySelectorAll('.schedule-month-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const month = btn.dataset.month;
    const slider = document.getElementById('scheduleSlider');
    const target = document.getElementById('month-' + month);
    if (target) {
      const scrollPos = target.offsetLeft - slider.offsetLeft;
      slider.scrollTo({ left: scrollPos, behavior: 'smooth' });
      document.querySelectorAll('.schedule-month-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      updateNavArrows(month);
    }
  });
});

const monthNames = {
  '3': '3月', '4': '4月', '5': '5月', '6': '6月', 
  '7': '7月', '8': '8月', '9': '9月', '10': '10月'
};

function updateNavArrows(currentMonth) {
  const months = ['3', '4', '5', '6', '7', '8', '9', '10'];
  const idx = months.indexOf(currentMonth);
  const prevBtn = document.getElementById('prevMonth');
  const nextBtn = document.getElementById('nextMonth');
  
  if (idx > 0) {
    const prevMonth = months[idx - 1];
    prevBtn.querySelector('.nav-arrow-text').textContent = monthNames[prevMonth];
    prevBtn.classList.remove('disabled');
  } else {
    prevBtn.querySelector('.nav-arrow-text').textContent = '';
    prevBtn.classList.add('disabled');
  }
  
  if (idx < months.length - 1) {
    const nextMonth = months[idx + 1];
    nextBtn.querySelector('.nav-arrow-text').textContent = monthNames[nextMonth];
    nextBtn.classList.remove('disabled');
  } else {
    nextBtn.querySelector('.nav-arrow-text').textContent = '';
    nextBtn.classList.add('disabled');
  }
}

// Arrow Navigation
document.getElementById('prevMonth').addEventListener('click', () => {
  const slider = document.getElementById('scheduleSlider');
  slider.scrollBy({ left: -slider.offsetWidth, behavior: 'smooth' });
});
document.getElementById('nextMonth').addEventListener('click', () => {
  const slider = document.getElementById('scheduleSlider');
  slider.scrollBy({ left: slider.offsetWidth, behavior: 'smooth' });
});

// Sync Tab with Scroll
let isScrolling;
document.getElementById('scheduleSlider').addEventListener('scroll', () => {
  window.clearTimeout(isScrolling);
  isScrolling = setTimeout(() => {
    const slider = document.getElementById('scheduleSlider');
    const scrollPos = slider.scrollLeft + (slider.offsetWidth / 2);
    const wrappers = document.querySelectorAll('.calendar-wrapper');
    const btns = document.querySelectorAll('.schedule-month-btn');
    
    wrappers.forEach(wrapper => {
      const start = wrapper.offsetLeft - slider.offsetLeft;
      const end = start + wrapper.offsetWidth;
      if (scrollPos >= start && scrollPos < end) {
        const month = wrapper.id.replace('month-', '');
        btns.forEach(b => {
          b.classList.toggle('active', b.dataset.month === month);
        });
        updateNavArrows(month);
      }
    });
  }, 100);
});

// Initial Scroll (Optional: Current Month)
window.addEventListener('load', () => {
  const activeBtn = document.querySelector('.schedule-month-btn.active');
  if (activeBtn) {
    const slider = document.getElementById('scheduleSlider');
    const target = document.getElementById('month-' + activeBtn.dataset.month);
    if (target) {
      slider.scrollTo({ left: target.offsetLeft - slider.offsetLeft, behavior: 'auto' });
      updateNavArrows(activeBtn.dataset.month);
    }
  }
});

})();
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
    'IMG_1432.JPG', 'IMG_1447.JPG', 'IMG_1448.JPG', 
    'IMG_1450.JPG', 'IMG_1451.JPG', 'IMG_1453.JPG', 
    'IMG_1454.JPG'
]
gallery_cards = ''
for img in gallery_items:
    gallery_cards += f'''
      <div class="gallery-card">
        <div class="gallery-photo"><img src="../public/images/gallery/{img}" alt="東京真隼の活動" loading="lazy"></div>
        <div class="gallery-caption">東京真隼の活動</div>
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
