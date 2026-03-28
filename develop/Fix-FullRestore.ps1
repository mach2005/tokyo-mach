# Fix-FullRestore.ps1
Write-Host "Restoring files from git commit d84f3e9..."
git checkout d84f3e9 -- index.html portal/index.html songs.html schedule.html faq.html gallery.html

Write-Host "Moving files to HP folder..."
if (!(Test-Path HP)) { New-Item -ItemType Directory -Path HP | Out-Null }
$files = @("index.html", "songs.html", "schedule.html", "faq.html", "gallery.html")
foreach ($f in $files) {
    if (Test-Path "HP\$f") { Remove-Item -Force "HP\$f" }
    Move-Item -Path $f -Destination "HP\$f" -Force
}

Write-Host "Applying path updates with UTF-8 No-BOM..."
$utf8NoBom = New-Object System.Text.UTF8Encoding $False

$hpFiles = @("HP\index.html", "HP\songs.html", "HP\schedule.html", "HP\faq.html", "HP\gallery.html")
foreach ($file in $hpFiles) {
    $content = [System.IO.File]::ReadAllText((Resolve-Path $file).Path)
    $content = $content.Replace('./public/', '../public/')
    [System.IO.File]::WriteAllText((Resolve-Path $file).Path, $content, $utf8NoBom)
}

$portalFile = "portal\index.html"
$content = [System.IO.File]::ReadAllText((Resolve-Path $portalFile).Path)
$content = $content.Replace('./public/', '../public/')
$content = $content.Replace('href="index.html"', 'href="../HP/index.html"')
$content = $content.Replace('href="FightSong/', 'href="../FightSong/')
[System.IO.File]::WriteAllText((Resolve-Path $portalFile).Path, $content, $utf8NoBom)

Write-Host "Full restoration completed successfully!"
