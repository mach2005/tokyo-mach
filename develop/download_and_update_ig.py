import urllib.request
import re
import os
import html

POSTS = [
    {
        "shortcode": "Dbk6thTiRI3",
        "url": "https://www.instagram.com/p/Dbk6thTiRI3/",
        "prefix": "ig_post_1",
        "date": "2026.04.05"
    },
    {
        "shortcode": "DbSyoaNCSib",
        "url": "https://www.instagram.com/p/DbSyoaNCSib/",
        "prefix": "ig_post_2",
        "date": "2026.04.04"
    },
    {
        "shortcode": "DbBFu_6iZ5W",
        "url": "https://www.instagram.com/p/DbBFu_6iZ5W/",
        "prefix": "ig_post_3",
        "date": "2026.04.02"
    }
]

SAVE_DIR = os.path.join(os.path.dirname(__file__), "../public/images")
INDEX_PATH = os.path.join(os.path.dirname(__file__), "../official/index.html")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

def fetch_viewer_images(shortcode):
    url = f"https://imginn.org/p/{shortcode}/"
    print(f"Fetching images from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as res:
            content = res.read().decode('utf-8', errors='ignore')

        imgs = re.findall(r'<img [^>]*src="([^"]+)"', content)
        post_imgs = []
        for img in imgs:
            # Filter out profile pic (t51.82787-19)
            if 't51.82787-15' in img:
                img_url = html.unescape(img)
                if img_url not in post_imgs:
                    post_imgs.append(img_url)
        return post_imgs
    except Exception as e:
        print(f"Error fetching from viewer for {shortcode}: {e}")
        return []

def main():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    for p in POSTS:
        print(f"\n==========================================")
        print(f"Processing Post: {p['shortcode']}")
        print(f"==========================================")
        img_urls = fetch_viewer_images(p['shortcode'])
        print(f" Found {len(img_urls)} post images for {p['shortcode']}")
        
        p['downloaded_files'] = []
        for idx, img_url in enumerate(img_urls, 1):
            filename = f"{p['prefix']}_{idx}.jpg"
            filepath = os.path.join(SAVE_DIR, filename)
            try:
                img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(img_req, timeout=15) as res, open(filepath, 'wb') as f:
                    f.write(res.read())
                file_size = os.path.getsize(filepath)
                print(f"  [SUCCESS] Saved {filename} ({file_size} bytes)")
                p['downloaded_files'].append(f"../public/images/{filename}")
            except Exception as e:
                print(f"  [ERROR] Download failed for {filename}: {e}")

    # Build HTML for official/index.html
    new_html = ""
    for p in POSTS:
        files = p.get('downloaded_files')
        if not files:
            files = [f"../public/images/{p['prefix']}_1.jpg"]

        items_html = ""
        for idx, img_path in enumerate(files, 1):
            items_html += f'                <div class="ig-carousel-item"><img src="{img_path}" alt="{p["date"]}-{idx}" loading="lazy"></div>\n'

        new_html += f"""          <a href="{p['url']}" target="_blank" rel="noopener" class="instagram-card">
            <div class="ig-card-img">
              <button class="ig-nav-btn ig-nav-prev" onclick="moveIgCarousel(event, this, -1)"><i class="fas fa-chevron-left"></i></button>
              <button class="ig-nav-btn ig-nav-next" onclick="moveIgCarousel(event, this, 1)"><i class="fas fa-chevron-right"></i></button>
              <div class="instagram-overlay"><i class="fab fa-instagram"></i></div>
              <div class="ig-carousel-track">
{items_html.rstrip()}
              </div>
            </div>
            <div class="ig-card-footer">
              <span class="ig-post-label">{p['date']}</span>
              <span class="ig-link-text">Instagramで表示</span>
            </div>
          </a>\n"""

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        html_content = f.read()

    pattern = r'<!-- IG_FEED_START -->.*?<!-- IG_FEED_END -->'
    replacement = f'<!-- IG_FEED_START -->\n{new_html}        <!-- IG_FEED_END -->'
    updated_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print(f"\n[COMPLETE SUCCESS] Updated {INDEX_PATH} with newly downloaded Instagram post images!")

if __name__ == "__main__":
    main()
