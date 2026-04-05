import os
import re

files_to_update = [
    'HP/index.html',
    'FightSong/digital-sheet.html',
    'HP/news/20260401-downs.html',
    'HP/songs.html',
    'HP/articles.html',
    'FightSong/cheer-guide.html',
    'FightSong/print-sheet.html',
    'FightSong/print_ouenka_2026.html'
]

# Style for narrow containers
styled_name = '<span style="display:inline-block; transform:scaleX(0.7); transform-origin:left; white-space:nowrap;">ジーター ダウンズ</span>'
plain_name = 'ジーター ダウンズ'

def update_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Special handling for specific files
    if 'digital-sheet' in file_path or 'print-sheet' in file_path or 'print_ouenka_2026' in file_path:
        # In these files, we likely want the styled version for player names in headers
        # We look for "ジーター" that is not already "ジーター ダウンズ"
        # And we target the song-name or similar classes if possible, but a regex for the name alone might work if we are careful.
        
        # Replace occurrences in common player name containers
        content = re.sub(r'(class="[^"]*song-name[^"]*">)ジーター(?=</div>|</span>)', r'\1' + styled_name, content)
        # Also handle standard occurrences in these sheets
        content = content.replace('>ジーター<', f'>{styled_name}<')
        content = content.replace('　ジーター', f'　{plain_name}') # Lyrics usually don't need scaling
    else:
        # Plain replacement for news and index
        content = content.replace('ジーター ダウンズ', 'TEMP_DOWNS') # Save existing
        content = content.replace('ジーター', plain_name)
        content = content.replace('TEMP_DOWNS', plain_name)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {file_path}")

for f in files_to_update:
    update_file(f)
