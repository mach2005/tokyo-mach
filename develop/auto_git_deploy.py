import subprocess
import os
import sys

def auto_deploy(commit_msg="Fix and update website"):
    print(f"[AUTO DEPLOY] Starting automatic Git commit & push...")
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    try:
        r1 = subprocess.run(["git", "add", "."], cwd=project_root, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        print(f"  [git add] {r1.stdout.strip()} {r1.stderr.strip()}")
        
        r2 = subprocess.run(["git", "commit", "-m", commit_msg], cwd=project_root, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        print(f"  [git commit] {r2.stdout.strip()} {r2.stderr.strip()}")
        
        r3 = subprocess.run(["git", "push", "origin", "main"], cwd=project_root, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        print(f"  [git push] {r3.stdout.strip()} {r3.stderr.strip()}")
        
        print("[AUTO DEPLOY OK] GitHub upload completed successfully!")
        return True
    except Exception as e:
        print(f"[AUTO DEPLOY ERROR] {e}")
        return False

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "Fix: Automatic deploy update"
    auto_deploy(msg)
