---
name: full-build-deploy
description: >-
  東京真隼サイトの全ページ（試合日程・応援歌・FAQ・ギャラリー）をPythonスクリプトで再生成し、
  ローカルリンクの整合性検証を行ってからGitHub Pagesへデプロイ・公開URLの疎通確認までを完全自動実行するスキル。
  ユーザーが「全体を再ビルドして」「日程と応援歌を更新してデプロイして」「全ページ再生成して」と指示した際に使用する。
---

# フルビルド＆デプロイ スキル

全ページをPythonスクリプトから再生成し、リンク検証を行ってからGitHub Pagesにデプロイします。
※文言の1箇所修正など軽微な修正の場合は、より高速な `quick-fix-deploy` スキルを使用してください。

## 実行手順（完全自律実行）

### 1. HP配下サブページの生成（schedule, songs, faq, gallery）
```powershell
python develop/build_pages.py
```

### 2. 応援歌ページの生成（HP/songs.html）
```powershell
python develop/gen_songs.py
```

### 3. ローカルリンク整合性の検証
```powershell
$root = "."
$broken = @()
Get-ChildItem -Path $root -Filter "*.html" -Recurse | Where-Object { $_.FullName -notmatch '\\history\\|\\\.git\\|\\archive\\' } | ForEach-Object {
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

### 4. Git ステージング・コミット・プッシュ
```powershell
git add .
git status
git commit -m "Update: Rebuild all pages and deploy"
git push origin main
Write-Host "✅ Deployed to GitHub Pages!"
```

### 5. デプロイ後URL疎通確認
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

### 6. キャッシュクリーンアップ
```powershell
Get-ChildItem -Path "." -Filter "__pycache__" -Recurse | Remove-Item -Force -Recurse
Write-Host "✅ Build and deployment pipeline finished."
```
