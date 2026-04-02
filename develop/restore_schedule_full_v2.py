import os

build_script_path = r'C:\Users\user\Antigravity\東京真隼\develop\build_pages.py'
clean_content_path = r'C:\Users\user\Antigravity\東京真隼\develop\clean_schedule.txt'

with open(clean_content_path, 'r', encoding='utf-8') as f:
    raw_content = f.read()

# スクリプトのカプセル化：
# <script> の中身を (function() { ... })(); で囲む
start_script_idx = raw_content.find('<script>')
end_script_idx = raw_content.rfind('</script>')

if start_script_idx != -1 and end_script_idx != -1:
    html_part = raw_content[:start_script_idx + 8]
    js_part = raw_content[start_script_idx + 8 : end_script_idx]
    footer_part = raw_content[end_script_idx:]
    
    # スコープを分離
    new_schedule_html_js = html_part + "\n(function() {\n" + js_part + "\n})();\n" + footer_part
else:
    new_schedule_html_js = raw_content

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
    
    # 既存のスケジュールセクションを全削除（次のセクションまで）
    if skip:
        if ('# =====' in line and 'SCHEDULE PAGE' not in line) or 'make_page(' in line:
             if 'schedule.html' not in line: # schedule.html の make_page は既に書いた
                skip = False
                new_lines.append("\n")
                new_lines.append(line)
        continue
    
    new_lines.append(line)

with open(build_script_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Updated {build_script_path} with SCOPED script and fixed Mojibake.")
