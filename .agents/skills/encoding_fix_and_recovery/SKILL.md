---
name: encoding_fix_and_recovery
description: UTF-8文字化け（Mojibake）の修復とGit履歴からのファイル復元手順。PowerShellによるファイル破損を安全に回復する方法。
---

# 文字化け修復＆ファイル復元スキル

## 背景

PowerShell の `Set-Content` や `Get-Content` は、デフォルトで UTF-16LE エンコーディングを使用します。
UTF-8 で書かれた HTML ファイルをこれらのコマンドで処理すると、文字化け（Mojibake）が発生します。

過去にこの問題が発生し、以下の手順で完全復旧を行いました。

## 安全なコミット（復元ポイント）

| コミットハッシュ | 説明 |
|-----------------|------|
| `d84f3e9` | 全ファイルが正常な状態。FightSong のフラット化済み。HP配下は元の構造。 |
| `325c796` | 最新安定版。ルートリダイレクト追加済み、ポータルリンク修正済み。 |

## 修復手順

### パターン1: 単一ファイルの復元

Python を使用して Git 履歴から安全にファイルを取り出します:

```powershell
python -c "
import subprocess
data = subprocess.run(['git', 'show', 'd84f3e9:HP/index.html'], capture_output=True).stdout
with open('HP/index.html', 'wb') as f:
    f.write(data)
print('Restored HP/index.html')
"
```

### パターン2: 全HPファイルの一括復元

```powershell
python -c "
import subprocess
files = ['HP/index.html', 'HP/schedule.html', 'HP/songs.html', 'HP/faq.html', 'HP/gallery.html']
for f in files:
    data = subprocess.run(['git', 'show', f'd84f3e9:{f}'], capture_output=True).stdout
    with open(f, 'wb') as out:
        out.write(data)
    print(f'Restored {f}')
print('All files restored!')
"
```

### パターン3: 最新安定コミットへの完全ロールバック

```powershell
git checkout 325c796 -- .
git commit -m "Rollback: Restore to stable state"
git push origin main
```

## パス補正（復元後に必要）

`d84f3e9` から復元した場合、HP配下のファイルのCSSパスが `./public/` になっているため、`../public/` に修正する必要があります:

```powershell
python -c "
import os, re
for fname in ['HP/schedule.html', 'HP/songs.html', 'HP/faq.html', 'HP/gallery.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('./public/', '../public/')
    content = content.replace('href=\"index.html\"', 'href=\"index.html\"')
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed paths in {fname}')
"
```

## 予防策

### やってはいけないこと

```powershell
# ❌ これは文字化けを引き起こします
Get-Content HP/index.html | Set-Content HP/index_copy.html
(Get-Content HP/index.html) -replace "old", "new" | Set-Content HP/index.html
```

### 安全な代替手段

```powershell
# ✅ Python を使う
python -c "
with open('HP/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('old', 'new')
with open('HP/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
"
```

```powershell
# ✅ PowerShell 7+ なら Encoding 指定で安全
Get-Content HP/index.html -Encoding UTF8 | Set-Content HP/index_copy.html -Encoding UTF8
```

## 文字化けの検出

ファイルが文字化けしているかどうかを確認するには:

```powershell
python -c "
for fname in ['HP/index.html', 'HP/schedule.html', 'HP/songs.html', 'HP/faq.html', 'HP/gallery.html']:
    with open(fname, 'rb') as f:
        data = f.read(100)
    # BOM (FF FE) があれば UTF-16LE = 文字化けの可能性大
    if data[:2] == b'\xff\xfe':
        print(f'⚠️  {fname}: UTF-16LE detected (likely mojibake)')
    elif data[:3] == b'\xef\xbb\xbf':
        print(f'✅ {fname}: UTF-8 with BOM')
    else:
        print(f'✅ {fname}: UTF-8 (no BOM)')
"
```
