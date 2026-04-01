import os
import re

def update_files():
    # Targets: HP/*.html and HP/news/*.html
    hp_dir = r'c:\Users\user\Antigravity\東京真隼\HP'
    news_dir = os.path.join(hp_dir, 'news')
    
    targets = []
    for d in [hp_dir, news_dir]:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.endswith('.html'):
                    targets.append(os.path.join(d, f))
    
    # 1. Catchphrase Replacement (Rich version with <br>)
    # <p class="hero-desc">北海道から広島まで、<br class="sp-only">ビジターの地で<br>ホークスの勝利を叫ぶ。</p>
    p1_rich = r'北海道から広島まで、<br class="sp-only">ビジターの地で<br>ホークスの勝利を叫ぶ。'
    p1_plain = r'北海道から広島まで、ビジターの地でホークスの勝利を叫ぶ。'
    p1_new = r'CTS～HIJ'
    
    # 2. Introduction Replacement
    p2_old = r'世界最強のホークス私設応援団'
    p2_new = r'ビジター応援の専門集団。関門海峡を飛び越え台湾まで'
    
    for path in targets:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig = content
        # Replace rich phrase
        content = content.replace(p1_rich, p1_new)
        # Replace plain phrase (meta tags)
        content = content.replace(p1_plain, p1_new)
        # Replace introduction
        content = content.replace(p2_old, p2_new)
        
        if content != orig:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated: {os.path.basename(path)}')

if __name__ == "__main__":
    update_files()
