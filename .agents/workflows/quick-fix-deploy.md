---
description: 東京真隼サイトの微修正を最速でデプロイする（HTMLの直接編集→Git push）。Pythonは使わない。
---

# クイック修正＆デプロイ ワークフロー

HTML/CSS/テキストの微修正を、Pythonを使わずに直接ファイル編集して最速でデプロイする。

## 重要原則

> [!CAUTION]
> **PowerShellの `Set-Content`, `Get-Content`, `>`, `>>` は絶対に使わない（UTF-16LE文字化けの原因）。**
> 代わりに `[System.IO.File]::ReadAllText` / `::WriteAllText` を UTF-8 指定で使う。

## ファイル編集のゴールデンテンプレート

### テキスト置換（最も多用する）

```powershell
$p = "{対象ファイルの相対パス}"
$c = [System.IO.File]::ReadAllText($p, [System.Text.Encoding]::UTF8)
$c = $c.Replace("置換前テキスト", "置換後テキスト")
[System.IO.File]::WriteAllText($p, $c, [System.Text.Encoding]::UTF8)
Write-Host "✅ Updated: $p"
```

### 複数箇所を一括置換

```powershell
$p = "{対象ファイルの相対パス}"
$c = [System.IO.File]::ReadAllText($p, [System.Text.Encoding]::UTF8)
$c = $c.Replace("A", "B").Replace("C", "D").Replace("E", "F")
[System.IO.File]::WriteAllText($p, $c, [System.Text.Encoding]::UTF8)
Write-Host "✅ Updated: $p"
```

### 複数ファイルを同時更新（選手データ変更時など）

```powershell
$files = @(
  "FightSong/cheer-guide.html",
  "FightSong/digital-sheet.html",
  "FightSong/print_ouenka_2026.html",
  "develop/gen_songs.py"
)
foreach ($p in $files) {
  $c = [System.IO.File]::ReadAllText($p, [System.Text.Encoding]::UTF8)
  $c = $c.Replace("旧テキスト", "新テキスト")
  [System.IO.File]::WriteAllText($p, $c, [System.Text.Encoding]::UTF8)
  Write-Host "✅ Updated: $p"
}
```

## デプロイ（必ず実行）

```powershell
git add .
git status
git commit -m "Fix: {修正内容の一行説明}"
git push origin main

# Pythonキャッシュのクリーンアップ
Get-ChildItem -Path "." -Filter "__pycache__" -Recurse | Remove-Item -Force -Recurse
Write-Host "✅ Deployed and Cleanup completed!"
```

## 対象ファイルの早見表（パス）

| 修正対象 | ファイルパス |
|----------|-------------|
| ポータル | `portal/index.html` |
| 公式HPトップ | `HP/index.html` |
| 試合日程 | `HP/schedule.html` |
| 応援歌(簡易版) | `HP/songs.html` |
| Q&A | `HP/faq.html` |
| ギャラリー | `HP/gallery.html` |
| 共通CSS | `public/style.css` |
| モバイル応援ガイド | `FightSong/cheer-guide.html` |
| デジタルシート | `FightSong/digital-sheet.html` |
| 印刷用HTML | `FightSong/print_ouenka_2026.html` |
| チアガイド | `FightSong/print-sheet.html` |

## 注意事項

- `HP/schedule.html`, `HP/songs.html` を全面再生成したい場合は `/full-build-deploy` ワークフローを使う（Pythonが必要）
- ただし「テキスト1箇所修正」レベルならこのワークフローで十分（Pythonビルド不要）
- デプロイ後はブラウザで **Shift+F5（スーパーリロード）** を実行すること
