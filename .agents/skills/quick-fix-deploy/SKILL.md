---
name: quick-fix-deploy
description: >-
  東京真隼サイトの微小なテキスト修正やCSS修正をPythonビルドを介さずに直接UTF-8で編集し、
  最速でGitコミット＆GitHub Pagesへプッシュするスキル。
  ユーザーが「少し文言を変えて」「 typoを直して」「色を少し変更して」など、軽微な修正を求めた際に使用する。
---

# クイック修正＆デプロイ スキル

HTML/CSS/テキストの微修正を、Pythonによる再生成を介さずに直接ファイル編集し、最速でGitHub Pagesへデプロイします。

## 重要原則（文字コード保護）

> [!CAUTION]
> **PowerShellの `Set-Content`, `Get-Content`, `>`, `>>` は絶対に使わないこと（UTF-16LE文字化けの原因）。**
> 必ずAI編集ツール（`replace_file_content` 等）または Python / `[System.IO.File]` の UTF-8 指定で編集してください。

## ファイル編集方法

### 1. AI編集ツールを使用する場合（最優先・推奨）
`edit_file` / `replace_file_content` などの標準ツールを使用して直接UTF-8で置換します。

### 2. PowerShell を使用する場合（System.IO.File UTF-8厳守）
```powershell
$p = "{対象ファイルの相対パス}"
$c = [System.IO.File]::ReadAllText($p, [System.Text.Encoding]::UTF8)
$c = $c.Replace("置換前テキスト", "置換後テキスト")
[System.IO.File]::WriteAllText($p, $c, [System.Text.Encoding]::UTF8)
```

## 自動デプロイ手順（完全自律実行）

修正完了後、ユーザーに確認を求めることなく直ちに以下を実行します:

```powershell
git add .
git status
git commit -m "Fix: {修正内容の要約}"
git push origin main

# Pythonキャッシュのクリーンアップ
Get-ChildItem -Path "." -Filter "__pycache__" -Recurse | Remove-Item -Force -Recurse
```

## 主な対象ファイルパス早見表

| 修正対象 | ファイルパス |
| :--- | :--- |
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
