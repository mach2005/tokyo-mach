import os
import shutil
import glob
from datetime import datetime

DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(DIR, ".."))
BACKUP_DIR = os.path.join(PROJECT_ROOT, "archive", "backup")

TARGET_FILES = [
    "official/index.html",
    "official/schedule.html",
    "official/songs.html",
    "official/faq.html",
    "official/gallery.html",
    "members/index.html",
    "FightSong/cheer-guide.html",
    "FightSong/digital-sheet.html",
    "FightSong/print_ouenka_2026.html"
]

def create_backup():
    """修正前の全HPファイルをバックアップフォルダへ即座に保存"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    saved_count = 0
    for rel_path in TARGET_FILES:
        src = os.path.join(PROJECT_ROOT, rel_path)
        if os.path.exists(src):
            # 1. 最新の直前バックアップ (latest)
            safe_name = rel_path.replace("/", "_").replace("\\", "_")
            latest_dst = os.path.join(BACKUP_DIR, f"latest_{safe_name}")
            shutil.copy2(src, latest_dst)
            
            # 2. タイムスタンプ付き履歴バックアップ
            history_dst = os.path.join(BACKUP_DIR, f"{timestamp}_{safe_name}")
            shutil.copy2(src, history_dst)
            saved_count += 1
            
    print(f"[BACKUP OK] {saved_count} files backed up successfully. (Timestamp: {timestamp})")
    
    # 対話・指示ログも同時にバックアップ抽出
    try:
        import save_chat_history
        save_chat_history.extract_chat_log()
    except Exception as e:
        print(f"[WARN] Failed to auto-backup chat log: {e}")
        
    return timestamp

def restore_latest():
    """直前のバックアップ状態へ即座に全復元"""
    if not os.path.exists(BACKUP_DIR):
        print("[RESTORE ERROR] Backup directory not found.")
        return False

    restored_count = 0
    for rel_path in TARGET_FILES:
        safe_name = rel_path.replace("/", "_").replace("\\", "_")
        latest_src = os.path.join(BACKUP_DIR, f"latest_{safe_name}")
        dst = os.path.join(PROJECT_ROOT, rel_path)
        
        if os.path.exists(latest_src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(latest_src, dst)
            print(f"  Restored: {rel_path}")
            restored_count += 1
            
    if restored_count > 0:
        print(f"[RESTORE OK] {restored_count} files restored to previous state successfully.")
        return True
    else:
        print("[RESTORE ERROR] No backup files available for restoration.")
        return False

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "backup"
    if cmd == "restore":
        restore_latest()
    else:
        create_backup()
