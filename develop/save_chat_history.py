import os
import json
from datetime import datetime

DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(DIR, ".."))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "archive", "chat_history")
APPDATA_DIR = r"C:\Users\user\.gemini\antigravity-ide"
CONVERSATION_ID = "ead8f342-49f7-42e8-9087-f6a2f4bc46e5"

TRANSCRIPT_PATH = os.path.join(APPDATA_DIR, "brain", CONVERSATION_ID, ".system_generated", "logs", "transcript.jsonl")

def extract_chat_log():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    if not os.path.exists(TRANSCRIPT_PATH):
        print(f"[ERROR] Transcript log file not found: {TRANSCRIPT_PATH}")
        return False
        
    messages = []
    with open(TRANSCRIPT_PATH, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                step_type = data.get("type", "")
                if step_type == "USER_INPUT":
                    content = data.get("content", "")
                    if content and "<USER_REQUEST>" in content:
                        import re
                        m = re.search(r'<USER_REQUEST>(.*?)</USER_REQUEST>', content, re.DOTALL)
                        req_text = m.group(1).strip() if m else content.strip()
                        messages.append(f"### 👤 USER:\n{req_text}\n")
                    elif content:
                        messages.append(f"### 👤 USER:\n{content.strip()}\n")
                elif step_type == "PLANNER_RESPONSE":
                    content = data.get("content", "")
                    if content and not content.startswith("<thought>"):
                        messages.append(f"### 🤖 AI:\n{content.strip()}\n")
            except Exception:
                pass
                
    now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    latest_file = os.path.join(OUTPUT_DIR, "chat_history_latest.md")
    timestamp_file = os.path.join(OUTPUT_DIR, f"chat_history_{now_str}.md")
    
    header = f"# 東京真隼（TOKYO MACH）対話・指示バックアップログ\n保存日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n"
    full_text = header + "\n---\n\n".join(messages)
    
    with open(latest_file, 'w', encoding='utf-8') as f:
        f.write(full_text)
    with open(timestamp_file, 'w', encoding='utf-8') as f:
        f.write(full_text)
        
    print(f"[OK] Chat history saved successfully ({len(messages)} turns extracted)")
    print(f"  Saved to: {latest_file}")
    return True

if __name__ == "__main__":
    extract_chat_log()
