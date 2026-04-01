import subprocess

def get_content(commit, path):
    try:
        res = subprocess.check_output(['git', 'show', f'{commit}:{path}'], text=True, encoding='utf-8')
        return res
    except Exception as e:
        return str(e)

commit = '1aa2119'
path = 'develop/build_pages.py'
res = get_content(commit, path)

with open('hist_build_pages_v2.py', 'w', encoding='utf-8') as f:
    f.write(res)

print('Extracted build_pages.py from 1aa2119')
