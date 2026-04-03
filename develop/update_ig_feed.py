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
                
                # Imginn等の構造から最新1件を抽出（正規表現は各サイトに合わせる必要があるが、一般解を試行）
                # 例: <a href="/p/xxx/"><img src="yyy">
                # ここでは最新1件のイメージとリンクを取得
                matches = re.findall(r'<a href="(/p/[^"]+)"[^>]*>.*?<img [^>]*src="([^"]+)"', html, re.DOTALL)
                if matches:
                    link, img_url = matches[0]
                    # 相対パスを絶対パスに
                    full_link = f"https://www.instagram.com{link}"
                    return full_link, img_url
        except Exception as e:
            print(f"Failed to fetch from {viewer}: {e}")
    return None, None

def download_image(url):
    try:
        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)
        
        local_path = os.path.join(SAVE_DIR, "latest_ig.jpg")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response, open(local_path, 'wb') as f:
            f.write(response.read())
        return "public/images/latest_ig.jpg"
    except Exception as e:
        print(f"Failed to download image: {e}")
        return None

def update_index(post_link, img_local_path):
    if not post_link or not img_local_path:
        print("Required data missing for IG update.")
        return

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # マーカー間の置換
    new_html = f"""          <a href="{post_link}" target="_blank" rel="noopener" class="instagram-card">
            <div class="ig-card-img">
              <img src="../{img_local_path}" alt="Latest Instagram Post">
              <div class="instagram-overlay"><i class="fab fa-instagram"></i></div>
            </div>
            <div class="ig-card-footer">
              <span class="ig-post-label">Latest Post</span>
              <span class="ig-link-text">Instagramで表示</span>
            </div>
          </a>"""

    pattern = r'<!-- IG_FEED_START -->.*?<!-- IG_FEED_END -->'
    replacement = f'<!-- IG_FEED_START -->\n{new_html}\n          <!-- IG_FEED_END -->'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully updated Instagram feed in {INDEX_PATH}")

if __name__ == "__main__":
    link, img = fetch_ig_data()
    if link and img:
        local_img = download_image(img)
        if local_img:
            update_index(link, local_img)
        else:
            print("Image download failed, using remote URL.")
            update_index(link, img) # フォールバックとしてリモートURLを使用 
    else:
        # フォールバック: スクレイピングが失敗した場合、手動でセットされた最新のデータ（今回のブラウザ取得分）を使うロジック
        # 固定値での更新（初回用またはエラー時の維持）
        print("Automatic fetching failed. Using recent manual values (fallback).")
        manual_link = "https://www.instagram.com/tokyo_mach/p/DWOpajwiYNO/"
        manual_img = "https://scontent-nrt1-1.cdninstagram.com/v/t51.82787-15/656063955_18105975256848405_3022366776073415298_n.jpg"
        # 実際にはダウンロードを試みる
        local_img = download_image(manual_img) or manual_img
        update_index(manual_link, local_img)
