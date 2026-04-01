import os
import re

def update_index():
    path = r'c:\Users\user\Antigravity\東京真隼\HP\index.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Version and remove Swiper CSS
    content = content.replace('style.css?v=4', 'style.css?v=5')
    content = re.sub(r'<link rel="stylesheet" href="https://cdn\.jsdelivr\.net/npm/swiper@11/swiper-bundle\.min\.css" />\s*', '', content)
    
    # 2. Remove Swiper Style block
    content = re.sub(r'<style>\s*\.articles-swiper.*?</style>\s*', '', content, flags=re.DOTALL)

    # 3. Update Nav text
    content = content.replace('>団員募集</a>', '>団員募集中！</a>')

    # 4. Update Section Title
    content = content.replace('<h2 class="section-title">お知らせ</h2>', '<h2 class="section-title">新着情報</h2>')

    # 5. Replace Swiper HTML with Scroll HTML
    # We target from <div class="swiper articles-swiper"> to the end of that div
    news_items = """
        <div class="news-scroll-item">
          <div style="height: 100%; background: #fff; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); overflow: hidden; border-left: 10px solid #ffcc00; display: flex; flex-direction: column;">
            <div style="padding: 30px; flex-grow: 1;">
              <div style="margin-bottom: 15px;">
                <span style="display: inline-block; background: #ffcc00; color: #111; padding: 4px 12px; border-radius: 4px; font-weight: 800; font-size: 0.85rem; box-shadow: 2px 2px 0 rgba(0,0,0,0.1);">お知らせ</span>
                <span style="color: #666; font-size: 0.9rem; margin-left: 10px;">2026.04.01</span>
              </div>
              <h3 style="font-size: 1.3rem; font-weight: 700; margin: 0 0 15px 0; color: #111; line-height: 1.5;">2026年度 新応援歌完成のお知らせ</h3>
              <p style="color: #555; font-size: 1rem; margin: 0; line-height: 1.6;">
                2026年度の新しい応援歌が完成しました。以下のリンクより詳細をご確認ください。
              </p>
              <div style="margin-top: 15px; display: flex; flex-wrap: wrap; gap: 10px;">
                <a href="https://www.google.com/search?q=../FightSong/ouenka_2026.pdf" target="_blank" style="color: #d4a700; font-weight: bold; text-decoration: none; font-size: 0.9rem; border: 1px solid #d4a700; padding: 4px 10px; border-radius: 4px;">新応援歌（PDF）</a>
                <a href="https://www.google.com/search?q=../FightSong/digital-sheet.html" target="_blank" style="color: #d4a700; font-weight: bold; text-decoration: none; font-size: 0.9rem; border: 1px solid #d4a700; padding: 4px 10px; border-radius: 4px;">デジタル楽譜</a>
                <a href="https://www.google.com/search?q=../FightSong/cheer-guide.html" target="_blank" style="color: #d4a700; font-weight: bold; text-decoration: none; font-size: 0.9rem; border: 1px solid #d4a700; padding: 4px 10px; border-radius: 4px;">応援ガイド</a>
              </div>
            </div>
          </div>
        </div>
        <div class="news-scroll-item">
          <div style="height: 100%; background: #fff; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); overflow: hidden; border-left: 10px solid #ffcc00; display: flex; flex-direction: column;">
            <div style="padding: 30px; flex-grow: 1;">
              <div style="margin-bottom: 15px;">
                <span style="display: inline-block; background: #ffcc00; color: #111; padding: 4px 12px; border-radius: 4px; font-weight: 800; font-size: 0.85rem; box-shadow: 2px 2px 0 rgba(0,0,0,0.1);">お知らせ</span>
              </div>
              <h3 style="font-size: 1.3rem; font-weight: 700; margin: 0 0 15px 0; color: #111; line-height: 1.5;">周東選手の前奏ができました</h3>
              <p style="color: #555; font-size: 1rem; margin: 0; line-height: 1.6;">
                2026年より周東選手の新応援歌（前奏付き）を使用します。<br>
                <a href="./news/20260401-shuto.html" style="color: #d4a700; font-weight: bold; text-decoration: none; display: inline-block; margin-top: 10px;">記事で詳しく見る <i class="fas fa-chevron-right"></i></a>
              </p>
            </div>
          </div>
        </div>
        <div class="news-scroll-item">
          <div style="height: 100%; background: #fff; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); overflow: hidden; border-left: 10px solid #111; display: flex; flex-direction: column;">
            <div style="padding: 30px; flex-grow: 1;">
              <div style="margin-bottom: 15px;">
                <span style="display: inline-block; background: #111; color: #fff; padding: 4px 12px; border-radius: 4px; font-weight: 800; font-size: 0.85rem; box-shadow: 2px 2px 0 rgba(0,0,0,0.1);">応援のお願い</span>
              </div>
              <h3 style="font-size: 1.3rem; font-weight: 700; margin: 0 0 15px 0; color: #111; line-height: 1.5;">ジーター・ダウンズ選手のコール紹介</h3>
              <p style="color: #555; font-size: 1rem; margin: 0; line-height: 1.6;">
                皆様の熱いご声援をよろしくお願いいたします。<br>
                <a href="./news/20260401-downs.html" style="color: #d4a700; font-weight: bold; text-decoration: none; display: inline-block; margin-top: 10px;">記事で詳しく見る <i class="fas fa-chevron-right"></i></a>
              </p>
            </div>
          </div>
        </div>
        <div class="news-scroll-item">
          <div style="height: 100%; background: #fff; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); overflow: hidden; border-left: 10px solid #0055ff; display: flex; flex-direction: column;">
            <div style="padding: 30px; flex-grow: 1;">
              <div style="margin-bottom: 15px;">
                <span style="display: inline-block; background: #0055ff; color: #fff; padding: 4px 12px; border-radius: 4px; font-weight: 800; font-size: 0.85rem; box-shadow: 2px 2px 0 rgba(0,0,0,0.1);">お知らせ</span>
              </div>
              <h3 style="font-size: 1.3rem; font-weight: 700; margin: 0 0 15px 0; color: #111; line-height: 1.5;">2026年 新応援歌が登場！</h3>
              <p style="color: #555; font-size: 1rem; margin: 0; line-height: 1.6;">
                松本晴選手、大山凌選手、谷川原健太選手、緒方理貢選手の新応援歌が追加されました。<br>
                <a href="#new-songs" style="color: #0055ff; font-weight: bold; text-decoration: none; display: inline-block; margin-top: 10px;">下部のセクションで試聴する <i class="fas fa-arrow-down"></i></a>
              </p>
            </div>
          </div>
        </div>
    """
    scroll_html = f'<div class="news-scroll-container"><div class="news-scroll-inner">{news_items}</div></div>'
    content = re.sub(r'<div class="swiper articles-swiper">.*?</div>\s*</div>\s*</div>', scroll_html + '\n  </div>', content, flags=re.DOTALL)

    # 6. Remove Swiper Script
    content = re.sub(r'<script src="https://cdn\.jsdelivr\.net/npm/swiper@11/swiper-bundle\.min\.js"></script>.*?</script>', '', content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html")

def update_others():
    files = ['schedule.html', 'songs.html', 'gallery.html', 'faq.html', 'articles.html']
    for f_name in files:
        path = os.path.join(r'c:\Users\user\Antigravity\東京真隼\HP', f_name)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                c = f.read()
            c = c.replace('>団員募集</a>', '>団員募集中！</a>')
            c = c.replace('style.css?v=4', 'style.css?v=5')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Updated {f_name}")

if __name__ == "__main__":
    update_index()
    update_others()
