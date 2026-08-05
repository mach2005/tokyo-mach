---
description: 東京真隼サイトのフルビルド＆デプロイ（ページ生成→Git push→URL検証）
---

# フルビルド＆デプロイ ワークフロー

全ページを再生成してGitHub Pagesにデプロイする。
**テキスト微修正だけなら `/quick-fix-deploy` を使うこと（こちらより速い）。**

## 手順

### 1. HP配下サブページ生成（schedule, songs, faq, gallery）

```powershell
python develop/build_pages.py
```

### 2. 応援歌ページ生成（HP/songs.html）

```powershell
python develop/gen_songs.py
```

### 3. ローカルリンク整合性検証

```powershell
$root = "."
$broken = @()
Get-ChildItem -Path $root -Filter "*.html" -Recurse | Where-Object { $_.FullName -notmatch '\\history\\|\\\.git\\' } | ForEach-Object {
  $file = $_
  $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
  $matches = [regex]::Matches($content, '(?:href|src)=[\"'']([^\"''#]+)[\"'']')
  foreach ($m in $matches) {
    $link = $m.Groups[1].Value
    if ($link -match '^(http|//|data:|mailto:|#)') { continue }
    $resolved = [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($file.DirectoryName, $link))
    if (-not (Test-Path $resolved)) {
      $broken += "$($file.Name) -> $link"
    }
  }
}
if ($broken.Count -eq 0) { Write-Host "✅ All links OK" }
else { Write-Host "⚠️ Broken links:"; $broken | ForEach-Object { Write-Host "  $_" } }
```

### 4. Git push デプロイ

```powershell
git add .
git status
git commit -m "Update: Rebuild all pages"
git push origin main
Write-Host "✅ Deployed!"
```

### 5. デプロイ後URL検証（push後1〜2分待ってから実行）

```powershell
Start-Sleep -Seconds 10
$urls = @(
  "https://mach2005.github.io/tokyo-mach/portal/index.html",
  "https://mach2005.github.io/tokyo-mach/HP/index.html",
  "https://mach2005.github.io/tokyo-mach/HP/songs.html",
  "https://mach2005.github.io/tokyo-mach/FightSong/cheer-guide.html"
)
foreach ($url in $urls) {
  try {
    $req = [System.Net.WebRequest]::Create($url)
    $req.Method = "HEAD"
    $res = $req.GetResponse()
    Write-Host "✅ $($res.StatusCode) $url"
    $res.Close()
  } catch {
    Write-Host "❌ FAILED: $url"
  }
}
```

### 6. クリーンアップ

```powershell
Get-ChildItem -Path "." -Filter "__pycache__" -Recurse | Remove-Item -Force -Recurse
Write-Host "✅ Cleanup completed."
Write-Host "Shift+F5でブラウザをリロードしてください。"
```
