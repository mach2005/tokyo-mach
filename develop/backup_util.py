import os
import shutil
import datetime
import glob

# 自身のディレクトリを取得
DIR = os.path.dirname(os.path.abspath(__file__))

# 設定
BACKUP_DIR = r'C:\Users\user\Antigravity\backup'
ARCHIVE_DIR = r'C:\Users\user\Antigravity\archive'
MAX_BACKUPS = 20

def backup_file(file_path):
    """
    指定されたファイルをバックアップし、世代管理を行う。
    file_path: バックアップ対象の完全パス (例: C:\\Users\\user\\Antigravity\\東京真隼\\HP\\index.html)
    """
    if not os.path.exists(file_path):
        print(f"Warning: File not found for backup: {file_path}")
        return

    # フォルダの存在確認
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    # 元のファイル名と拡張子を取得
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)

    # 日時スタンプの生成 (YYMMDDHHMM 形式)
    # ユーザー指定例 index_26042200 に合わせる
    now = datetime.datetime.now()
    timestamp = now.strftime("%y%m%d%H%M")
    
    backup_filename = f"{name}_{timestamp}{ext}"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    # バックアップの実作成
    _, file_ext = os.path.splitext(file_path)
    
    try:
        if file_ext.lower() == ".html":
            # HTMLの場合: CSSのインライン化とパス補正
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 外部CSSの読み込み (style.css)
            css_path = os.path.join(DIR, '../public/style.css')
            css_content = ""
            if os.path.exists(css_path):
                with open(css_path, 'r', encoding='utf-8') as f:
                    css_content = f.read()
                
                # CSS内のパス補正 (url("../images/...") -> url("../東京真隼/images/..."))
                css_content = css_content.replace('url("../', 'url("../東京真隼/')
                
                # <link rel="stylesheet" href="../public/style.css..."> を <style> に置換
                import re
                # <link rel="stylesheet" href="../public/style.css[^"]*"> のようなタグを置換
                link_pattern = r'<link\s+[^>]*rel=["\']stylesheet["\'][^>]*href=["\']\.\./public/style\.css[^"\']*["\'][^>]*>'
                if re.search(link_pattern, content):
                    content = re.sub(link_pattern, f'<style>\n{css_content}\n</style>', content)
                else:
                    # 見つからない場合は head の最後に挿入
                    content = content.replace('</head>', f'<style>\n{css_content}\n</style>\n</head>')

            # 全体的なパス置換 (href="../, src="../)
            content = content.replace('href="../', 'href="../東京真隼/')
            content = content.replace('src="../', 'src="../東京真隼/')
            content = content.replace('url("../', 'url("../東京真隼/')
            
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            # HTML以外はそのままコピー
            shutil.copy2(file_path, backup_path)
            
        print(f"Backup created: {backup_filename}")
    except Exception as e:
        print(f"Error creating backup for {file_path}: {e}")
        return

    # 世代管理 (20個を超えたらアーカイブへ)
    manage_rotation(name, ext)

def manage_rotation(name, ext):
    """
    特定のベース名を持つバックアップファイルの数を制限し、古いものをアーカイブへ移動する。
    """
    # backup フォルダ内の該当ファイルを検索 (名前_*.拡張子)
    pattern = os.path.join(BACKUP_DIR, f"{name}_*{ext}")
    backups = glob.glob(pattern)
    
    # 作成日時順にソート (古い順)
    backups.sort(key=os.path.getmtime)

    if len(backups) > MAX_BACKUPS:
        num_to_move = len(backups) - MAX_BACKUPS
        to_move = backups[:num_to_move]
        
        for old_backup in to_move:
            base_old = os.path.basename(old_backup)
            dest = os.path.join(ARCHIVE_DIR, base_old)
            
            # アーカイブ先での重複回避
            if os.path.exists(dest):
                name_old, ext_old = os.path.splitext(base_old)
                idx = 1
                while os.path.exists(dest):
                    dest = os.path.join(ARCHIVE_DIR, f"{name_old}_{idx}{ext_old}")
                    idx += 1
            
            try:
                shutil.move(old_backup, dest)
                print(f"Archived old backup: {os.path.basename(dest)}")
            except Exception as e:
                print(f"Error archiving {old_backup}: {e}")

if __name__ == "__main__":
    # テスト用
    import sys
    if len(sys.argv) > 1:
        backup_file(sys.argv[1])
