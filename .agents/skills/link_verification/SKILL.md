---
name: link_verification
description: 東京真隼ウェブサイトの全リンク（内部リンク・外部リンク）を検証し、壊れたリンクを修正する手順。
---

# リンク検証＆修正スキル

ポータルサイト・HP・FightSong 間のリンク整合性を確認・修正するスキルです。

## ディレクトリ構造とパス関係

```
東京真隼/
├── index.html          ← ./portal/index.html へリダイレクト
├── portal/
│   └── index.html      ← ../HP/index.html, ../FightSong/xxx を参照
├── HP/
│   ├── index.html       ← ../public/style.css を参照
│   ├── schedule.html    ← ../public/style.css を参照
│   ├── songs.html       ← ../public/style.css を参照
│   ├── faq.html         ← ../public/style.css を参照
│   └── gallery.html     ← ../public/style.css を参照
├── FightSong/
│   ├── cheer-guide.html ← ../public/audio/xxx を参照
│   └── ...
└── public/
    ├── style.css
    ├── favicon.svg
    └── audio/
```

## リンクのルール

### portal/index.html から

| リンク先 | パス形式 |
|----------|---------|
| HP 公式サイト | `../HP/index.html` (相対パス) |
| デジタルシート | `../FightSong/digital-sheet.html` (相対パス) |
| 応援歌PDF | `../FightSong/ouenka_2026.pdf` (相対パス) |
| モバイル応援ガイド | `https://mach2005.github.io/tokyo-mach/FightSong/cheer-guide.html` (絶対URL) |
| 印刷用PDF | `https://mach2005.github.io/tokyo-mach/FightSong/print_ouenka_2026.pdf` (絶対URL) |

### HP 配下のページから

| リンク先 | パス形式 |
|----------|---------|
| 共通CSS | `../public/style.css` |
| favicon | `../public/favicon.svg` |
| 同階層のページ | `schedule.html`, `songs.html` 等 |
| ポータルへ戻る | `../portal/index.html` |

### FightSong 配下のファイルから

| リンク先 | パス形式 |
|----------|---------|
| 音声ファイル | `../public/audio/xxx.aac` |
| ポータルへ戻る | `../portal/index.html` |

## 自動検証スクリプト

以下のPythonスクリプトで全リンクを検証します:

```powershell
python -c "
import os, re
# ... (中略)
"
```

## 外部URL検証

```powershell
python -c "
import urllib.request, urllib.error
# ... (中略)
"
```

## よくあるリンク修正

### portal/index.html のリンクが相対パスで壊れている場合

```powershell
python -c "
with open('portal/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
# 壊れがちなパターンを修正
content = content.replace('href=\"HP/', 'href=\"../HP/')
content = content.replace('href=\"FightSong/', 'href=\"../FightSong/')
with open('portal/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed portal links')
"
```
