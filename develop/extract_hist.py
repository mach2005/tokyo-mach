import subprocess
import os

def get_content(commit, path):
    try:
        res = subprocess.check_output(['git', 'show', f'{commit}:{path}'], text=True, encoding='utf-8')
        return res
    except Exception as e:
        return str(e)

commit = '976eeba'
build_pages = get_content(commit, 'develop/build_pages.py')
data_txt = get_content(commit, 'develop/data.txt')

with open('hist_build_pages.py', 'w', encoding='utf-8') as f:
    f.write(build_pages)
with open('hist_data.txt', 'w', encoding='utf-8') as f:
    f.write(data_txt)

print('Extracted historical files to hist_build_pages.py and hist_data.txt')
