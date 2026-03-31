import os

history_dir = r"C:\Users\user\Antigravity\東京真隼\history"
files = [f for f in os.listdir(history_dir) if f.endswith(".html")]

for filename in files:
    filepath = os.path.join(history_dir, filename)
    try:
        # Try reading as UTF-16LE
        with open(filepath, 'rb') as f:
            content_bytes = f.read()
        
        # Check for UTF-16LE BOM or just try decoding
        try:
            content = content_bytes.decode('utf-16le')
            print(f"Converting {filename} (UTF-16LE) to UTF-8")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        except UnicodeDecodeError:
            print(f"Skipping {filename} - already UTF-8 or other encoding")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
