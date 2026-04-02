import os

build_script_path = r'C:\Users\user\Antigravity\東京真隼\develop\build_pages.py'
clean_content_path = r'C:\Users\user\Antigravity\東京真隼\develop\clean_schedule.txt'

with open(clean_content_path, 'r', encoding='utf-8') as f:
    new_schedule_html_js = f.read()

with open(build_script_path, 'r', encoding='utf-8') as f:
    script_lines = f.readlines()

new_lines = []
skip = False
for line in script_lines:
    if '# ===== SCHEDULE PAGE' in line:
        new_lines.append(line)
        new_lines.append("schedule_content = r'''\n")
        new_lines.append(new_schedule_html_js + "\n")
        new_lines.append("'''\n")
        new_lines.append("make_page('schedule.html', '試合日程', schedule_content)\n")
        skip = True
        continue
    
    if skip:
        # 次のセクションか末尾までスキップ
        if '# =====' in line and 'SCHEDULE PAGE' not in line:
            skip = False
            new_lines.append("\n")
            new_lines.append(line)
        continue
    
    new_lines.append(line)

with open(build_script_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Updated {build_script_path} with clean content and fixed Mojibake.")
