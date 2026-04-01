import codecs
import re

def update_index():
    index_path = r'c:\Users\user\Antigravity\東京真隼\HP\index.html'
    with codecs.open(index_path, 'r', 'utf-8') as f:
        html = f.read()

    # Find the bounds for replacement
    start_str = '<div class="news-scroll-container">'
    
    start_idx = html.find(start_str)
    
    # We want to replace everything up to the first </section> after start_idx
    # actually, up to `  </div>\n</section>`
    end_idx = html.find('</section>', start_idx)
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find the block in index.html")
        return

    # Extract the new songs section for later use in new-songs.html
    songs_start_str = '<!-- New Songs Section -->'
    songs_start_idx = html.find(songs_start_str)
    songs_end_idx = html.find('</section>', songs_start_idx)
    
    if songs_start_idx != -1 and songs_end_idx != -1:
        new_songs_html_original = html[songs_start_idx : songs_end_idx + len('</section>')]
    else:
        new_songs_html_original = ""

    new_news_block = """<div class="news-slider-wrapper" style="position: relative; max-width: 1000px; margin: 0 auto;">
      <button class="news-scroll-prev" id="newsPrev" style="position: absolute; left:-20px; top:50%; transform:translateY(-50%); z-index:10; background:rgba(255,255,255,0.95); width:44px; height:44px; border-radius:50%; border:1px solid #ddd; cursor:pointer; box-shadow:0 4px 10px rgba(0,0,0,0.1); display:flex; align-items:center; justify-content:center; color:#333; transition:0.3s;" onmouseover="this.style.background='#ffcc00'; this.style.borderColor='#111'; this.style.color='#111'" onmouseout="this.style.background='rgba(255,255,255,0.95)'; this.style.borderColor='#ddd';"><i class="fas fa-chevron-left" style="font-weight:900;"></i></button>
      
      <div class="news-scroll-container" id="newsScroll" style="overflow-x: hidden; scroll-behavior: smooth; padding: 20px 0;">
        <div class="news-scroll-inner" id="newsInner" style="display: flex; gap: 20px; width: max-content;">
          
          <!-- Unified Article 1: New Songs -->
          <a href="./news/20260401-new-songs.html" class="news-scroll-item news-card" style="text-decoration:none; display:block; width: 320px; flex-shrink: 0; outline:none;">
            <div style="height: 100%; background: #fff; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); overflow: hidden; border-left: 10px solid #ffcc00; display: flex; flex-direction: column; transition: 0.3s; padding: 30px;">
              <div style="margin-bottom: 15px;">
                <span style="display: inline-block; background: #ffcc00; color: #111; padding: 4px 12px; border-radius: 4px; font-weight: 800; font-size: 0.85rem; box-shadow: 2px 2px 0 rgba(0,0,0,0.1);">お知らせ</span>
                <span style="color: #666; font-size: 0.9rem; margin-left: 10px;">2026.04.01</span>
              </div>
              <h3 style="font-size: 1.3rem; font-weight: 700; margin: 0 0 15px 0; color: #111; line-height: 1.5;">2026年度 新応援歌完成のお知らせ</h3>
              <p style="color: #555; font-size: 1rem; margin: 0; line-height: 1.6;">
                松本晴選手、大山凌選手、谷川原健太選手、緒方理貢選手の新応援歌、周東佑京選手の前奏が追加されました。以下のリンクより詳細をご確認ください。
              </p>
              <div style="margin-top: 15px; font-weight: bold; color: #d4a700;">記事で詳しく見る <i class="fas fa-chevron-right"></i></div>
            </div>
          </a>
          
          <!-- Article 2: Downs -->
          <a href="./news/20260401-downs.html" class="news-scroll-item news-card" style="text-decoration:none; display:block; width: 320px; flex-shrink: 0; outline:none;">
            <div style="height: 100%; background: #fff; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); overflow: hidden; border-left: 10px solid #111; display: flex; flex-direction: column; transition: 0.3s; padding: 30px;">
              <div style="margin-bottom: 15px;">
                <span style="display: inline-block; background: #111; color: #fff; padding: 4px 12px; border-radius: 4px; font-weight: 800; font-size: 0.85rem; box-shadow: 2px 2px 0 rgba(0,0,0,0.1);">応援のお願い</span>
                <span style="color: #666; font-size: 0.9rem; margin-left: 10px;">2026.04.01</span>
              </div>
              <h3 style="font-size: 1.3rem; font-weight: 700; margin: 0 0 15px 0; color: #111; line-height: 1.5;">ジーター・ダウンズ選手のコール紹介</h3>
              <p style="color: #555; font-size: 1rem; margin: 0; line-height: 1.6;">
                皆様の熱いご声援をよろしくお願いいたします。
              </p>
              <div style="margin-top: auto; padding-top: 15px; font-weight: bold; color: #d4a700;">記事で詳しく見る <i class="fas fa-chevron-right"></i></div>
            </div>
          </a>

        </div>
      </div>
      
      <button class="news-scroll-next" id="newsNext" style="position: absolute; right:-20px; top:50%; transform:translateY(-50%); z-index:10; background:rgba(255,255,255,0.95); width:44px; height:44px; border-radius:50%; border:1px solid #ddd; cursor:pointer; box-shadow:0 4px 10px rgba(0,0,0,0.1); display:flex; align-items:center; justify-content:center; color:#333; transition:0.3s;" onmouseover="this.style.background='#ffcc00'; this.style.borderColor='#111'; this.style.color='#111'" onmouseout="this.style.background='rgba(255,255,255,0.95)'; this.style.borderColor='#ddd';"><i class="fas fa-chevron-right" style="font-weight:900;"></i></button>
    </div>
  </div>
"""
    
    # We replace from start_idx to end_idx but we have to be careful not to delete the </div></div> before </section>
    # The structure originally was:
    # <div class="news-scroll-container">
    #   <div class="news-scroll-inner"> ... </div>
    # </div>
    # </div>
    # </section>
    # But `<div class="container">` wraps the whole section content. 
    # Let's just find `<div class="news-scroll-container">` and replace up to its closing tag by regex.
    pattern = r'<div class="news-scroll-container">.*?(?=</div>\s*</section>)'
    
    html = re.sub(pattern, new_news_block, html, flags=re.DOTALL)

    js_code = """
<script>
  window.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.news-card > div').forEach(card => {
      card.addEventListener('mouseover', () => card.style.transform = 'translateY(-5px)');
      card.addEventListener('mouseout', () => card.style.transform = 'none');
    });

    const inner = document.getElementById('newsInner');
    const scroll = document.getElementById('newsScroll');
    const prevBtn = document.getElementById('newsPrev');
    const nextBtn = document.getElementById('newsNext');
    
    if(!inner) return;

    // Clone elements for loop
    const itemsList = Array.from(inner.children);
    itemsList.forEach(item => inner.appendChild(item.cloneNode(true)));
    itemsList.forEach(item => inner.appendChild(item.cloneNode(true)));
    itemsList.forEach(item => inner.appendChild(item.cloneNode(true)));
    itemsList.forEach(item => inner.appendChild(item.cloneNode(true)));

    const getScrollAmount = () => itemsList.length > 0 ? itemsList[0].offsetWidth + 20 : 340;

    let isScrolling = false;
    const handleLoop = () => {
      const itemW = getScrollAmount();
      const maxScroll = scroll.scrollWidth - scroll.clientWidth;
      
      if (scroll.scrollLeft >= maxScroll - itemW / 2) {
        scroll.style.scrollBehavior = 'auto';
        scroll.scrollLeft = (itemsList.length * itemW);
        // Force reflow
        void scroll.offsetWidth;
      } else if (scroll.scrollLeft <= itemW / 2) {
        scroll.style.scrollBehavior = 'auto';
        scroll.scrollLeft = maxScroll - ((itemsList.length+1) * itemW);
        void scroll.offsetWidth;
      }
      isScrolling = false;
    };

    nextBtn.addEventListener('click', () => {
      if(isScrolling) return;
      isScrolling = true;
      scroll.style.scrollBehavior = 'smooth';
      scroll.scrollLeft += getScrollAmount();
      setTimeout(handleLoop, 400);
    });

    prevBtn.addEventListener('click', () => {
      if(isScrolling) return;
      isScrolling = true;
      scroll.style.scrollBehavior = 'smooth';
      scroll.scrollLeft -= getScrollAmount();
      setTimeout(handleLoop, 400);
    });

    // Initial position
    setTimeout(() => {
      if(itemsList.length > 0) {
          scroll.style.scrollBehavior = 'auto';
          scroll.scrollLeft = (itemsList.length * getScrollAmount());
      }
    }, 100);
  });
</script>
</body>"""

    if "id=\"newsInner\"" not in html and '<script>' not in html[-2000:]: # simple checking to avoid double insert
        pass
    
    # insert JS before body
    html = html.replace('</body>', js_code)

    with codecs.open(index_path, 'w', 'utf-8') as f:
        f.write(html)
    print("Updated index.html")
    
    return new_songs_html_original

def update_article(new_songs_html_original):
    if not new_songs_html_original: return
    
    article_path = r'c:\Users\user\Antigravity\東京真隼\HP\news\20260401-new-songs.html'
    with codecs.open(article_path, 'r', 'utf-8') as f:
        article_html = f.read()

    # The new 4 links
    links_html = """
    <div style="margin: 40px 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
      <a href="https://mach2005.github.io/tokyo-mach/FightSong/cheer-guide.html" target="_blank" style="background: #fff; padding: 25px; border-radius: 12px; border: 1px solid #ddd; text-align: center; text-decoration: none; transition: 0.3s; box-shadow: 0 4px 10px rgba(0,0,0,0.05);" onmouseover="this.style.borderColor='#0056b3'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='#ddd'; this.style.transform='none'">
        <i class="fas fa-mobile-alt" style="font-size: 2.5rem; color: #0056b3; margin-bottom: 15px;"></i>
        <h3 style="margin-bottom: 10px; color: #111; font-size: 1.1rem; font-weight:bold;">スマホ応援ガイド</h3>
      </a>
      <a href="https://mach2005.github.io/tokyo-mach/FightSong/digital-sheet.html" target="_blank" style="background: #fff; padding: 25px; border-radius: 12px; border: 1px solid #ddd; text-align: center; text-decoration: none; transition: 0.3s; box-shadow: 0 4px 10px rgba(0,0,0,0.05);" onmouseover="this.style.borderColor='#ffcc00'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='#ddd'; this.style.transform='none'">
        <i class="fas fa-music" style="font-size: 2.5rem; color: #ffcc00; margin-bottom: 15px;"></i>
        <h3 style="margin-bottom: 10px; color: #111; font-size: 1.1rem; font-weight:bold;">歌詞カード</h3>
      </a>
      <a href="https://mach2005.github.io/tokyo-mach/FightSong/ouenka_2026.pdf" target="_blank" style="background: #fff; padding: 25px; border-radius: 12px; border: 1px solid #ddd; text-align: center; text-decoration: none; transition: 0.3s; box-shadow: 0 4px 10px rgba(0,0,0,0.05);" onmouseover="this.style.borderColor='#ff3b30'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='#ddd'; this.style.transform='none'">
        <i class="fas fa-file-pdf" style="font-size: 2.5rem; color: #ff3b30; margin-bottom: 15px;"></i>
        <h3 style="margin-bottom: 10px; color: #111; font-size: 1.1rem; font-weight:bold;">歌詞カード(PDF版)</h3>
      </a>
      <a href="https://mach2005.github.io/tokyo-mach/FightSong/print_ouenka_2026.pdf" target="_blank" style="background: #fff; padding: 25px; border-radius: 12px; border: 1px solid #ddd; text-align: center; text-decoration: none; transition: 0.3s; box-shadow: 0 4px 10px rgba(0,0,0,0.05);" onmouseover="this.style.borderColor='#333'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='#ddd'; this.style.transform='none'">
        <i class="fas fa-print" style="font-size: 2.5rem; color: #333; margin-bottom: 15px;"></i>
        <h3 style="margin-bottom: 10px; color: #111; font-size: 1.1rem; font-weight:bold;">印刷はこちら</h3>
      </a>
    </div>
"""

    import re
    article_html = re.sub(r'<div style="margin: 40px 0; display: grid;.*?</div>\s*<p>', links_html + '\n    <p>', article_html, flags=re.DOTALL)

    # Adjust paths in the new songs block: ../public/ -> ../../public/
    adjusted_new_songs = new_songs_html_original.replace('../public/', '../../public/')
    
    article_html = article_html.replace('<footer class="article-footer">', adjusted_new_songs + '\n\n  <footer class="article-footer">')

    with codecs.open(article_path, 'w', 'utf-8') as f:
        f.write(article_html)
    print("Updated 20260401-new-songs.html")

if __name__ == "__main__":
    songs_html = update_index()
    update_article(songs_html)
