import subprocess
import os

print("Restoring files from git...")
# Restore files from commit d84f3e9 (where they were clean UTF-8)
subprocess.run(["git", "checkout", "d84f3e9", "--", "index.html", "portal/index.html"], check=True)

# Move index.html to HP/index.html
if os.path.exists('index.html'):
    if os.path.exists('HP/index.html'):
        os.remove('HP/index.html')
    os.rename('index.html', 'HP/index.html')

print("Applying path updates in UTF-8...")

# Fix HP/index.html paths
with open('HP/index.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('./public/', '../public/')
with open('HP/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Fix portal/index.html paths
with open('portal/index.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('./public/', '../public/')
c = c.replace('href="index.html"', 'href="../HP/index.html"')
c = c.replace('href="FightSong/', 'href="../FightSong/')
with open('portal/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Files successfully restored and path-corrected!")
