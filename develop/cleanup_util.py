import os
import shutil
import glob

DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(DIR, ".."))
TMP_DIR = os.path.join(PROJECT_ROOT, "tmp")

def cleanup_workspace():
    """ルート直下のデバッグ・一時ファイルを tmp/ へ移動・整理"""
    os.makedirs(TMP_DIR, exist_ok=True)
    
    patterns = ["tmp_*", "debug*.txt", "*.tmp", "diff_*.txt"]
    cleaned_count = 0
    
    for pat in patterns:
        for fpath in glob.glob(os.path.join(PROJECT_ROOT, pat)):
            if os.path.isfile(fpath):
                fname = os.path.basename(fpath)
                dst = os.path.join(TMP_DIR, fname)
                try:
                    shutil.move(fpath, dst)
                    cleaned_count += 1
                except Exception:
                    pass
                    
    print(f"[CLEANUP OK] {cleaned_count} temporary files moved to tmp/")
    return cleaned_count

if __name__ == "__main__":
    cleanup_workspace()
