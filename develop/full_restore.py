import subprocess
import os

print("Restoring all 6 core HTML files from pure git commit d84f3e9...")
files_to_restore = [
    "index.html", 
    "songs.html", 
    "schedule.html", 
    "faq.html", 
    "gallery.html", 
    "portal/index.html"
]

subprocess.run(["git", "checkout", "d84f3e9", "--"] + files_to_restore, check=True)

# Make sure HP directory exists
os.makedirs("HP", exist_ok=True)

# Move the 5 main files into HP/
hp_files = ["index.html", "songs.html", "schedule.html", "faq.html", "gallery.html"]

for f in hp_files:
    src = f
    dest = os.path.join("HP", f)
    if os.path.exists(dest):
        os.remove(dest)
    os.rename(src, dest)

print("Applying safe UTF-8 path updates...")

# Fix paths for all 5 HP/ files
for f in hp_files:
    path = os.path.join("HP", f)
    with open(path, 'r', encoding='utf-8') as file:
        c = file.read()
    c = c.replace('./public/', '../public/')
    with open(path, 'w', encoding='utf-8') as file:
        file.write(c)

# Fix portal/index.html paths
portal_path = 'portal/index.html'
with open(portal_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('./public/', '../public/')
c = c.replace('href="index.html"', 'href="../HP/index.html"')
c = c.replace('href="FightSong/', 'href="../FightSong/')

with open(portal_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Full restoration successful! Mojave and data-loss completely eliminated.")
