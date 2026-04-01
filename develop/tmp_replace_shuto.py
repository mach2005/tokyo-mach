import codecs
import re

html_path = r'c:\Users\user\Antigravity\東京真隼\HP\index.html'

with codecs.open(html_path, 'r', 'utf-8') as f:
    html = f.read()

# Original string pattern (handle flexible whitespace)
pattern = re.compile(
    r'【前奏】光のその先\s+切り拓け\s+鷹の勇者（ヒーロー）<br>\s*【本編】たゆまぬ努力で\s+さぁ時代を築け\s+志ひとつに\s+行けスピードソルジャー',
    re.MULTILINE
)

replacement = """<strong style="color: #d4a700;">【前奏】<br>
          光のその先 切り拓け 鷹の勇者（ヒーロー）</strong><br>
          【本編】<br>
          たゆまぬ努力で さぁ時代を築け 志ひとつに 行けスピードソルジャー"""

new_html = pattern.sub(replacement, html)

if html != new_html:
    with codecs.open(html_path, 'w', 'utf-8') as f:
        f.write(new_html)
    print("Replaced successfully")
else:
    print("Pattern not found!")
