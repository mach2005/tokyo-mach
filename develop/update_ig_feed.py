import os
import re
import urllib.request
import json
from datetime import datetime

# 設定
IG_ACCOUNT = "tokyo_mach"
# Instagramビューアーの候補（スクレイピング用）
IG_VIEWERS = [
    "https://imginn.org",
    "https://dumpoir.com/v",
    "https://imginn.com"
]
INDEX_PATH = os.path.join(os.path.dirname(__file__), "../HP/index.html")
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
        img_src = post.get('local_path') or post.get('img_url')
        if img_src and not img_src.startswith('http'):
            img_src = f"../{img_src}"
            
        new_html += f"""          <a href="{post['link']}" target="_blank" rel="noopener" class="instagram-card">
            <div class="ig-card-img">
              <img src="{img_src}" alt="Instagram Post {i+1}">
              <div class="instagram-overlay"><i class="fab fa-instagram"></i></div>
            </div>
            <div class="ig-card-footer">
              <span class="ig-post-label">Latest {i+1}</span>
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
    ig_posts = fetch_ig_data()
    if ig_posts:
        for i, post in enumerate(ig_posts):
            post['local_path'] = download_image(post['img_url'], i+1)
        update_index(ig_posts)
    else:
        # フォールバック
        print("Automatic fetching failed. Using recent manual values (fallback).")
        manual_data = [
            {"link": "https://www.instagram.com/tokyo_mach/p/DWOpajwiYNO/", "img_url": "https://scontent-nrt1-1.cdninstagram.com/v/t51.82787-15/656063955_18105975256848405_3022366776073415298_n.jpg"},
            {"link": "https://www.instagram.com/tokyo_mach/p/DWoX0PICR-v/", "img_url": "https://scontent-nrt1-1.cdninstagram.com/v/t51.82787-15/658175740_18106957390848405_4542364041086217553_n.jpg"},
            {"link": "https://www.instagram.com/tokyo_mach/p/DWOJZyfibsR/", "img_url": "https://scontent-nrt1-1.cdninstagram.com/v/t51.82787-15/658555795_18105951826848405_4020037548141739809_n.jpg"}
        ]
        for i, post in enumerate(manual_data):
            post['local_path'] = download_image(post['img_url'], i+1)
        update_index(manual_data)
