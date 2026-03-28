$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$data = Get-Content "$PSScriptRoot\data.txt" -Encoding UTF8
$top = Get-Content "$PSScriptRoot\layout_top.html" -Raw -Encoding UTF8
$bot = Get-Content "$PSScriptRoot\layout_bottom.html" -Raw -Encoding UTF8

$games = @{}
foreach ($line in $data) {
    if ($line -eq $null) { continue }
    $line = $line.Trim()
    if ($line -eq "" -or $line -match "^---") { continue }
    $cols = $line -split "`t"
    if ($cols.Length -ge 3) {
        $m = [regex]::match($cols[0], '(\d+)月(\d+)日')
        if ($m.Success) {
            $month = [int]$m.Groups[1].Value
            $day = [int]$m.Groups[2].Value
            $dateKey = "2026-{0:D2}-{1:D2}" -f $month, $day
            $opp = $cols[2] -replace '（交流戦）',''
            $venue = if ($cols.Length -ge 4 -and $cols[3] -ne "-") { $cols[3] } else { "" }
            $time = if ($cols.Length -ge 5 -and $cols[4] -ne "-") { $cols[4] } else { "" }
            
            $isHome = $false
            if ($venue -in @("みずほPayPay", "北九州", "熊本", "鹿児島")) { $isHome = $true }
            if ($venue -eq "東京ドーム" -and $opp -match "西武") { $isHome = $true }
            
            $type = "visitor"
            if ($isHome) { $type = "home" }
            if ($opp -match "CS") { $type = "cs" }
            if ($opp -match "日本シリーズ") { $type = "ns" }
            
            $games[$dateKey] = @{
                Opponent = $opp
                Venue = $venue
                Time = $time
                Type = $type
            }
        }
    }
}

$mid = ""
$months = 3..10

$mid += "    <div class='schedule-nav'>`n"
foreach ($m in $months) {
    $active = if ($m -eq 4) { " active" } else { "" }
    $label = if ($m -eq 10) { "10-11月" } else { "${m}月" }
    $mid += "      <button class='schedule-month-btn$active' data-month='$m'>$label</button>`n"
}
$mid += "    </div>`n"
$mid += "    <p class='schedule-legend'>`n"
$mid += "      <span class='legend-item'><span class='legend-dot visitor'></span>ビジター</span>`n"
$mid += "      <span class='legend-item'><span class='legend-dot home'></span>ホーム</span>`n"
$mid += "    </p>`n"

foreach ($m in $months) {
    $display = if ($m -eq 4) { "block" } else { "none" }
    $title = if ($m -eq 10) { "2026年10月-11月（ポストシーズン）" } else { "2026年${m}月" }
    
    $mid += "    <div class='calendar-wrapper' id='month-$m' style='display:$display;'>`n"
    $mid += "      <h3 class='calendar-month-title'>$title</h3>`n"
    $mid += "      <div class='calendar-grid'>`n"
    $mid += "        <div class='cal-header'>月</div><div class='cal-header'>火</div><div class='cal-header'>水</div><div class='cal-header'>木</div><div class='cal-header'>金</div><div class='cal-header sat'>土</div><div class='cal-header sun'>日</div>`n"
    
    $firstDay = Get-Date -Year 2026 -Month $m -Day 1
    $dayOfWeek = $firstDay.DayOfWeek.value__
    $offset = ($dayOfWeek + 6) % 7
    
    $daysInMonth = [DateTime]::DaysInMonth(2026, $m)
    if ($m -eq 10) { $daysInMonth = 31 + 1 }
    
    $totalDays = $offset + $daysInMonth
    $weeks = [math]::Ceiling($totalDays / 7)
    $cells = $weeks * 7
    
    for ($i = 0; $i -lt $cells; $i++) {
        $cellDate = $firstDay.AddDays($i - $offset)
        $dateKey = $cellDate.ToString("yyyy-MM-dd")
        $dayNum = $cellDate.Day.ToString()
        $isCurrentMonth = ($cellDate.Month -eq $m)
        if ($m -eq 10 -and $cellDate.Month -eq 11) { $isCurrentMonth = $true }
        
        $dayClass = "cal-day"
        $numClass = "day-num"
        
        if (($i % 7) -eq 5) { $numClass += " sat" }
        if (($i % 7) -eq 6) { $numClass += " sun" }
        if (-not $isCurrentMonth) { $numClass += " out-of-month" }
        
        $gameHtml = ""
        $hasGame = $games.ContainsKey($dateKey)
        $isVisibleGame = $false
        
        if ($hasGame) {
            $g = $games[$dateKey]
            
            if ($isCurrentMonth) {
                $isVisibleGame = $true
            } else {
                # Only show if it matches a game in current month (same opponent & venue) within 4 days
                foreach ($dOff in -4..4) {
                    if ($dOff -eq 0) { continue }
                    $checkDate = $cellDate.AddDays($dOff)
                    $cm = ($checkDate.Month -eq $m)
                    if ($m -eq 10 -and $checkDate.Month -eq 11) { $cm = $true }
                    
                    if ($cm) {
                        $checkKey = $checkDate.ToString("yyyy-MM-dd")
                        if ($games.ContainsKey($checkKey)) {
                            $checkGame = $games[$checkKey]
                            if ($checkGame.Opponent -eq $g.Opponent -and $checkGame.Venue -eq $g.Venue) {
                                $isVisibleGame = $true
                                break
                            }
                        }
                    }
                }
            }
            
            if ($isVisibleGame) {
                $type = $g.Type
                $teamAbbr = ""
                switch -Regex ($g.Opponent) {
                    "日本ハム" { $teamAbbr = "f" }
                    "楽天" { $teamAbbr = "e" }
                    "ロッテ" { $teamAbbr = "m" }
                    "西武" { $teamAbbr = "l" }
                    "オリックス" { $teamAbbr = "b" }
                    "巨人" { $teamAbbr = "g" }
                    "広島" { $teamAbbr = "c" }
                    "中日" { $teamAbbr = "d" }
                    "DeNA" { $teamAbbr = "db" }
                    "阪神" { $teamAbbr = "t" }
                    "ヤクルト" { $teamAbbr = "s" }
                }
                
                $oppHtml = ""
                if ($teamAbbr -ne "") {
                    $logoUrl = "https://npb.jp/img/common/logo/2026/logo_${teamAbbr}_s.gif"
                    $oppHtml = "<span class='game-opponent'><img src='$logoUrl' alt='$($g.Opponent)' class='team-logo-img'> $($g.Opponent)</span>"
                } else {
                    $oppHtml = "<span class='game-opponent'>$($g.Opponent)</span>"
                }
                
                if ($type -eq "home") { 
                    $dayClass += " home-day"
                    $gameHtml = "<div class='game-info home-game'>$oppHtml<span class='game-venue'>$($g.Venue)</span><span class='game-time'>$($g.Time)</span></div>" 
                } elseif ($type -eq "visitor") { 
                    $dayClass += " visitor-day"
                    $gameHtml = "<div class='game-info visitor-game'>$oppHtml<span class='game-venue'>$($g.Venue)</span><span class='game-time'>$($g.Time)</span></div>" 
                } elseif ($type -eq "cs") { 
                    $dayClass += " cs-day"
                    $gameHtml = "<div class='game-info cs-info'>$oppHtml<span class='game-venue'>$($g.Venue)</span></div>" 
                } elseif ($type -eq "ns") { 
                    $dayClass += " ns-day"
                    $gameHtml = "<div class='game-info ns-info'>$oppHtml<span class='game-venue'>$($g.Venue)</span></div>" 
                }
            }
        }
        
        if (-not $isVisibleGame) {
            $gameHtml = "" 
        }
        
        $mid += "        <div class='$dayClass'><span class='$numClass'>$dayNum</span>$gameHtml</div>`n"
    }
    $mid += "      </div>`n"
    $mid += "    </div>`n"
}

$finalHtml = $top + $mid + $bot
[System.IO.File]::WriteAllText("$PSScriptRoot\schedule.html", $finalHtml, [System.Text.Encoding]::UTF8)
Write-Output "Done"
