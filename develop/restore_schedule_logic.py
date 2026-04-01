import os

# PATHS
DIR = r'c:\Users\user\Antigravity\東京真隼\develop'
HIST_HTML = os.path.join(DIR, 'hist_schedule.html')
BUILD_PY = os.path.join(DIR, 'build_pages.py')

with open(HIST_HTML, 'r', encoding='utf-8') as f:
    hist_h = f.read()

# Extract the content between <section class="page-hero"> and </body> (excluding footer which is in build_pages.py already)
# Actually, build_pages.py constructs full = header + content + footer.
# So we need to extract ONLY the "content" part from hist_schedule.html.
# In hist_schedule.html:
# content starts at line 88: <section class="page-hero">
# content ends before <footer class="site-footer"> (line 463)

start_mark = '<section class="page-hero">'
end_mark = '<footer class="site-footer">'

start_idx = hist_h.find(start_mark)
end_idx = hist_h.find(end_mark)

if start_idx == -1 or end_idx == -1:
    print(f"Error finding marks: start={start_idx}, end={end_idx}")
    exit(1)

new_schedule_content_html = hist_h[start_idx:end_idx].strip()

# Now we need to escape the content for a Python string (triple quotes)
# Since the HTML contains both single and double quotes, we might need to be careful.
# But triple single quotes ''' usually work if we don't have ''' in the HTML.
# The HTML doesn't seem to have '''.

with open(BUILD_PY, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We want to replace everything from "# ===== SCHEDULE PAGE =====" (line 21)
# to "make_page('schedule.html', '試合日程', schedule_content)" (line 394)
# with a single block that sets schedule_content to the extracted HTML.

start_line = -1
end_line = -1

for i, line in enumerate(lines):
    if "# ===== SCHEDULE PAGE =====" in line:
        start_line = i
    if "make_page('schedule.html', '試合日程', schedule_content)" in line:
        end_line = i
        break

if start_line == -1 or end_line == -1:
    print(f"Error finding lines: start={start_line}, end={end_line}")
    exit(1)

new_block = [
    "# ===== SCHEDULE PAGE (Restored from Build #113) =====\n",
    "schedule_content = r'''\n",
    new_schedule_content_html + "\n",
    "'''\n",
    "make_page('schedule.html', '試合日程', schedule_content)\n\n"
]

new_lines = lines[:start_line] + new_block + lines[end_line+1:]

with open(BUILD_PY, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Updated build_pages.py with restored schedule content from Build #113.")
