import os

favicon_snippet = """    <link rel="icon" type="image/png" href="../public/favicon.png?v=2">
    <link rel="shortcut icon" href="../public/favicon.png?v=2">
    <link rel="apple-touch-icon" href="../public/apple-touch-icon.png?v=2">"""

history_dir = r"C:\Users\user\Antigravity\東京真隼\history"
target_files = ["live_index.html", "main_index.html", "v1.html", "v3.html"]

for filename in target_files:
    filepath = os.path.join(history_dir, filename)
    print(f"Processing {filename}...")
    
    # Read as bytes and try to find <head>
    with open(filepath, 'rb') as f:
        raw = f.read()
    
    # Try different decodings to find <head>
    content = None
    for enc in ['utf-16', 'utf-8-sig', 'utf-8', 'shift-jis']:
        try:
            temp = raw.decode(enc)
            if '<head>' in temp.lower():
                content = temp
                print(f"  Matched using {enc}")
                break
        except:
            continue
            
    if content is None:
        print(f"  Could not decode {filename}")
        continue

    if 'favicon.png?v=2' in content:
        print(f"  Already updated.")
        continue

    # Insert after <head> case-insensitively
    head_pos = content.lower().find('<head>')
    if head_pos != -1:
        insert_pos = head_pos + len('<head>')
        new_content = content[:insert_pos] + "\n" + favicon_snippet + content[insert_pos:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Successfully updated.")
    else:
        print(f"  Final backup: no <head> found.")
