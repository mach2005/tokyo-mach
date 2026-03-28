import os
DIR = os.path.dirname(os.path.abspath(__file__))

# Template reading
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

# Note: The schedule logic in build_pages.py was originally static or simplified. 
# For a full dynamic calendar, build_schedule.ps1 is often used, 
# but I provide the static structure with the navigation here.

schedule_content += '''
    <div class="calendar-wrapper" id="month-3">
      <h3 class="calendar-month-title">2026年3月 - 4月</h3>
      <p style="text-align:center; padding: 40px; color: #666;">（詳細は順次更新いたします。最新情報はSNSをご確認ください。）</p>
    </div>
  </div>
</section>
<script>
document.querySelectorAll('.schedule-month-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.schedule-month-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  });
});
</script>
'''

make_page('schedule.html', '試合日程', schedule_content)

# ===== GALLERY PAGE =====
gallery_content = '''
<section class="page-hero">
  <div class="page-hero-content">
    <span class="page-hero-label">GALLERY</span>
    <h1>ギャラリー</h1>
    <p>東京真隼の活動の様子をお届けします</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="gallery-grid">
      <div class="gallery-card">
        <div class="gallery-placeholder"><i class="fas fa-bullhorn"></i></div>
        <div class="gallery-caption">応援風景</div>
      </div>
      <div class="gallery-card">
        <div class="gallery-placeholder"><i class="fas fa-train"></i></div>
        <div class="gallery-caption">遠征の様子</div>
      </div>
      <div class="gallery-card">
        <div class="gallery-placeholder"><i class="fas fa-users"></i></div>
        <div class="gallery-caption">集合写真</div>
      </div>
    </div>
  </div>
</section>
'''
make_page('gallery.html', 'ギャラリー', gallery_content)

# ===== FAQ PAGE =====
faqs = [
    ('東京真隼とはどんな団体ですか？','東京真隼（TOKYO MACH）は、福岡ソフトバンクホークスの私設応援団です。主にビジター球場（関東圏を中心に、北海道から広島まで）でホークスを応援しています。'),
    ('誰でも入団できますか？','はい！年齢・性別・経験を問わず、ホークスが好きな方なら誰でも入団できます。'),
    ('入団にかかる費用はありますか？','団費などはいただいておりません。交通費等は自己負担となります。'),
    ('球団公式の応援団ですか？','いいえ、東京真隼は「私設」応援団です。'),
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
    <h1>Q&A</h1>
    <p>よくあるご質問をまとめました</p>
  </div>
</section>
<section class="section">
  <div class="container container-narrow">
    <div class="faq-list">{faq_items}</div>
  </div>
</section>
<script>
document.querySelectorAll('.faq-question').forEach(btn => {{
  btn.addEventListener('click', () => {{
    btn.closest('.faq-item').classList.toggle('open');
  }});
}});
</script>
'''
make_page('faq.html', 'Q&A', faq_content)

print('Updated HP pages.')
