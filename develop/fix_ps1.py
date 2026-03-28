import os
import re

path = 'build_songs.ps1'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Ensure all closing here-string delimiters are at the start of the line and have no trailing whitespace
    # Matches any whitespace at the start of a line followed by "@, and then any trailing whitespace
    content = re.sub(r'(?m)^[ \t]*\"@\s*$', '\"@', content)
    
    # 2. Also check the opening delimiters. @" must be at the end of the line.
    content = re.sub(r'(?m)^(\$[a-zA-Z0-9_]+\s*=\s*@\")\s*$', r'\1', content)
    
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print("Cleaned build_songs.ps1")
else:
    print("File not found")
