import os
import re
import sys
import urllib.request
from datetime import datetime, timezone, timedelta

# UTF-8 stdout configuration for Windows environment
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# 設定
X_ACCOUNT = "tokyo_mach"
# 複数のNitterインスタンスをフォールバックとして用意
NITTER_INSTANCES = [
    "https://nitter.net",
    "https://nitter.poast.org",
    "https://nitter.privacydev.net",
    "https://nitter.cz",
    "https://nitter.lucabased.xyz",
    "https://nitter.soopy.moe",
    "https://nitter.pericles.host"
]
INDEX_PATH = os.path.join(os.path.dirname(__file__), "../official/index.html")
PROFILE_IMG = "https://pbs.twimg.com/profile_images/1907352748280221696/7BPbU0fT_400x400.jpg"

def fetch_rss():
    for instance in NITTER_INSTANCES:
        url = f"{instance}/{X_ACCOUNT}/rss"
        try:
            print(f"Fetching from {url}...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=10) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            print(f"Failed to fetch from {instance}: {e}")
    return None

def parse_rss(xml_content):
    items = re.findall(r'<item>(.*?)</item>', xml_content, re.DOTALL)
    parsed_items = []
    JST = timezone(timedelta(hours=9))
    
    for item in items:
        title = re.search(r'<title>(.*?)</title>', item, re.DOTALL)
        link = re.search(r'<link>(.*?)</link>', item, re.DOTALL)
        pub_date = re.search(r'<pubDate>(.*?)</pubDate>', item, re.DOTALL)
        description = re.search(r'<description>(.*?)</description>', item, re.DOTALL)
        
        if title and link and pub_date:
            raw_link = link.group(1).strip()
            x_link = re.sub(r'^https?://[^/]+', 'https://x.com', raw_link)
            
            raw_date = pub_date.group(1).strip()
            try:
                date_obj = datetime.strptime(raw_date, '%a, %d %b %Y %H:%M:%S %Z')
                date_obj = date_obj.replace(tzinfo=timezone.utc).astimezone(JST)
                formatted_date = date_obj.strftime('%Y/%m/%d %H:%M')
            except Exception:
                date_obj = datetime.min.replace(tzinfo=JST)
                formatted_date = raw_date
            
            content = description.group(1) if description else title.group(1)
            content = content.replace('<![CDATA[', '').replace(']]>', '')
            content = re.sub(r'<.*?>', '', content)
            content = content.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
            content = re.sub(r'\n\s*\n', '\n', content).strip()
            
            parsed_items.append({
                'link': x_link,
                'content': content[:200] + ("..." if len(content) > 200 else ""),
                'date': formatted_date,
                'datetime_obj': date_obj
            })
            
    # Sort strictly by real datetime descending to eliminate pinned-tweet ordering issues
    parsed_items.sort(key=lambda x: x['datetime_obj'], reverse=True)
    return parsed_items[:1]

def update_index(posts):
    if not posts:
        print("No posts found to update.")
        return

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    new_feed_html = ""
    for i, post in enumerate(posts):
        new_feed_html += f"""          <!-- Post {i+1} -->
          <a href="{post['link']}" target="_blank" rel="noopener" class="x-post-card">
            <div class="x-post-header">
              <div class="x-user-icon"><img src="{PROFILE_IMG}" alt="東京真隼"></div>
              <div class="x-user-info">
                <span class="x-user-name">東京真隼【公式】</span>
                <span class="x-user-id">@{X_ACCOUNT}</span>
              </div>
              <i class="fab fa-x-twitter x-logo"></i>
            </div>
            <div class="x-post-content">{post['content']}</div>
            <div class="x-post-footer">
              <span class="x-post-date">{post['date']}</span>
              <span class="x-link-text">Xで表示</span>
            </div>
          </a>
"""

    # マーカー間の置換
    pattern = r'<!-- X_FEED_START -->.*?<!-- X_FEED_END -->'
    replacement = f'<!-- X_FEED_START -->\n{new_feed_html}          <!-- X_FEED_END -->'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully updated {INDEX_PATH}")

if __name__ == "__main__":
    try:
        xml = fetch_rss()
        if xml:
            posts = parse_rss(xml)
            if posts:
                update_index(posts)
            else:
                print("No X posts parsed.")
        else:
            print("Could not fetch X feed from any instance. Keeping existing feed intact.")
    except Exception as e:
        print(f"Notice: X feed update skipped due to error: {e}")
