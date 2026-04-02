import os
import sys

# 自身のディレクトリを取得
DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(DIR)

import backup_util

def main():
    """
    主要な全HTMLファイルをスキャンし、一括で最新版をバックアップする。
    """
    print("Starting session-based batch backup...")
    
    # バックアップ対象のリスト
    targets = [
        os.path.join(DIR, '../HP/index.html'),
        os.path.join(DIR, '../HP/schedule.html'),
        os.path.join(DIR, '../HP/songs.html'),
        os.path.join(DIR, '../HP/gallery.html'),
        os.path.join(DIR, '../HP/faq.html'),
        os.path.join(DIR, '../portal/index.html'),
    ]
    
    for target in targets:
        # パスを正規化
        full_path = os.path.abspath(target)
        if os.path.exists(full_path):
            backup_util.backup_file(full_path)
        else:
            print(f"Warning: File not found, skipping: {full_path}")
            
    print("\nSession backup completed.")

if __name__ == "__main__":
    main()
