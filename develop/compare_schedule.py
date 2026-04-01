import subprocess
import os

def get_content(commit, path):
    try:
        res = subprocess.check_output(['git', 'show', f'{commit}:{path}'], text=True, encoding='utf-8')
        return res
    except Exception as e:
        return str(e)

commit = '976eeba'
path = 'HP/schedule.html'
hist_h = get_content(commit, path)
curr_h = open('c:/Users/user/Antigravity/東京真隼/HP/schedule.html', 'r', encoding='utf-8').read()

with open('diff_schedule.txt', 'w', encoding='utf-8') as f:
    if hist_h == curr_h:
        f.write('The files are identical.')
    else:
        f.write('The files are different.\n')
        # Simple line-by-line diff or just save both
        with open('hist_schedule.html', 'w', encoding='utf-8') as fh:
            fh.write(hist_h)
        with open('curr_schedule.html', 'w', encoding='utf-8') as fc:
            fc.write(curr_h)

print('Compared schedule.html and saved results.')
