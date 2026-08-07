import os
import sys
import subprocess

# UTF-8 stdout configuration for Windows environment
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

script_dir = os.path.dirname(os.path.abspath(__file__))
target_script = os.path.join(script_dir, "download_and_update_ig.py")

if __name__ == "__main__":
    print("Running Instagram downloader & updater...")
    subprocess.run([sys.executable, target_script], check=True)
