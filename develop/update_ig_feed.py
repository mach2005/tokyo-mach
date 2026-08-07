import os
import re
import sys
import urllib.request
import json
from datetime import datetime

# UTF-8 stdout configuration for Windows environment
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# 設定
IG_ACCOUNT = "tokyo_mach"
# Instagramビューアーの候補（スクレイピング用）
IG_VIEWERS = [
    "https://imginn.org",
    "https://dumpoir.com/v",
    "https://imginn.com"
]
INDEX_PATH = os.path.join(os.path.dirname(__file__), "../official/index.html")
SAVE_DIR = os.path.join(os.path.dirname(__file__), "../public/images")

def fetch_ig_data():
    for viewer in IG_VIEWERS:
        url = f"{viewer}/{IG_ACCOUNT}/"
        try:
            print(f"Fetching Instagram data from {url}...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})
            with urllib.request.urlopen(req, timeout=15) as response:
                html = response.read().decode('utf-8')
                
                # 最新3件までのリンクと画像を取得
                matches = re.findall(r'<a href="(/p/[^"]+)"[^>]*>.*?<img [^>]*src="([^"]+)"', html, re.DOTALL)
                if matches:
                    results = []
                    for i in range(min(3, len(matches))):
                        link, img_url = matches[i]
                        results.append({
                            'link': f"https://www.instagram.com{link}",
                            'img_url': img_url
                        })
                    return results
        except Exception as e:
            print(f"Failed to fetch from {viewer}: {e}")
    return []

def download_image(url, index):
    try:
        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)
        
        local_filename = f"ig_post_{index}.jpg"
        local_path = os.path.join(SAVE_DIR, local_filename)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response, open(local_path, 'wb') as f:
            f.write(response.read())
        return f"public/images/{local_filename}"
    except Exception as e:
        print(f"Failed to download image {index}: {e}")
        return None

def update_index(posts):
    if not posts:
        print("Required data missing for IG update.")
        return

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 3つの投稿HTMLを生成
    new_html = ""
    for i, post in enumerate(posts):
        images = post.get('images', [])
        if not images:
            img_src = post.get('local_path') or post.get('img_url')
            if img_src and not img_src.startswith('http') and not img_src.startswith('..'):
                img_src = f"../{img_src}"
            images = [img_src]

        date_label = post.get('date', f'2026.04.0{5-i}')
        
        items_html = ""
        for idx, img_path in enumerate(images, 1):
            items_html += f'                <div class="ig-carousel-item"><img src="{img_path}" alt="{date_label}-{idx}" loading="lazy"></div>\n'

        new_html += f"""          <a href="{post['link']}" target="_blank" rel="noopener" class="instagram-card">
            <div class="ig-card-img">
              <button class="ig-nav-btn ig-nav-prev" onclick="moveIgCarousel(event, this, -1)"><i class="fas fa-chevron-left"></i></button>
              <button class="ig-nav-btn ig-nav-next" onclick="moveIgCarousel(event, this, 1)"><i class="fas fa-chevron-right"></i></button>
              <div class="instagram-overlay"><i class="fab fa-instagram"></i></div>
              <div class="ig-carousel-track">
{items_html.rstrip()}
              </div>
            </div>
            <div class="ig-card-footer">
              <span class="ig-post-label">{date_label}</span>
              <span class="ig-link-text">Instagramで表示</span>
            </div>
          </a>\n"""

    pattern = r'<!-- IG_FEED_START -->.*?<!-- IG_FEED_END -->'
    replacement = f'<!-- IG_FEED_START -->\n{new_html}        <!-- IG_FEED_END -->'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully updated Instagram feed with {len(posts)} posts in {INDEX_PATH}")

if __name__ == "__main__":
    # ユーザー指定の3つのカルーセル投稿（画像送り・複数画像対応）を固定で使用
    manual_data = [
        {
            "link": "https://www.instagram.com/tokyo_mach/p/Dbk6thTiRI3/?img_index=1",
            "date": "2026.04.05",
            "images": [
                "../public/images/ig_post_1_1.jpg",
                "../public/images/ig_post_1_2.jpg",
                "../public/images/ig_post_1_3.jpg",
                "../public/images/ig_post_1_4.jpg",
                "../public/images/ig_post_1_5.jpg",
                "../public/images/ig_post_1_6.jpg"
            ]
        },
        {
            "link": "https://www.instagram.com/tokyo_mach/p/DbSyoaNCSib/",
            "date": "2026.04.04",
            "images": [
                "../public/images/ig_post_2_1.jpg",
                "../public/images/ig_post_2_2.jpg",
                "../public/images/ig_post_2_3.jpg",
                "../public/images/ig_post_2_4.jpg",
                "../public/images/ig_post_2_6.jpg",
                "../public/images/ig_post_2_7.jpg",
                "../public/images/ig_post_2_8.jpg",
                "../public/images/ig_post_2_9.jpg"
            ]
        },
        {
            "link": "https://www.instagram.com/tokyo_mach/p/DbBFu_6iZ5W/",
            "date": "2026.04.02",
            "images": [
                "../public/images/ig_post_3_1.jpg",
                "../public/images/ig_post_3_2.jpg",
                "../public/images/ig_post_3_3.jpg",
                "../public/images/ig_post_3_5.jpg",
                "../public/images/ig_post_3_6.jpg"
            ]
        }
    ]
    update_index(manual_data)
