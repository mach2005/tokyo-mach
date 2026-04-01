import codecs
with codecs.open(r'c:\Users\user\Antigravity\東京真隼\HP\index.html', 'r', 'utf-8') as f:
    text = f.read()

target = '''    </div>
  </div>
</div>
</section>'''
new_target = '''    </div>
  </div>
</section>'''

text = text.replace(target, new_target)

with codecs.open(r'c:\Users\user\Antigravity\東京真隼\HP\index.html', 'w', 'utf-8') as f:
    f.write(text)
print("done")
