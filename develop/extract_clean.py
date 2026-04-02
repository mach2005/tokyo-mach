import os

p = r'C:\Users\user\Antigravity\東京真隼\develop\hist_schedule.html'
out_path = r'C:\Users\user\Antigravity\東京真隼\develop\clean_schedule.txt'

with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

# エキスパート・ビルド：
# 1. <section class="page-hero"> から開始
# 2. </body> の手前にある最後の </script> までを抽出
start = content.find('<section class="page-hero">')
# フッター直後のスクリプトも含めるため、</body> か </html> の手前まで探す
end = content.find('<footer class="site-footer">')
if end == -1:
    end = content.rindex('</script>') + 9
else:
    # フッターの後ろにスクリプトがあるケース：
    script_start = content.find('<script>', end)
    if script_start != -1:
        script_end = content.rfind('</script>') + 9
        # コンテンツ + スクリプト
        body = content[start:end]
        script = content[script_start:script_end]
        final_content = body + script
    else:
        final_content = content[start:end]

with open(out_path, 'w', encoding='utf-8') as out:
    out.write(final_content)

print(f"Extracted to {out_path}")
