import os
import re
import sys
import urllib.request
import time
from datetime import datetime

# UTF-8 stdout configuration for Windows environment
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Settings
TEAM_URL = "https://baseball.yahoo.co.jp/npb/teams/12/"
WEEKDAYS_JP = ['月', '火', '水', '木', '金', '土', '日']
INDEX_PATH = os.path.join(os.path.dirname(__file__), "../official/index.html")
PORTAL_PATH = os.path.join(os.path.dirname(__file__), "../members/index.html")
SCHEDULE_PATH = os.path.join(os.path.dirname(__file__), "../official/schedule.html")
BUILD_PAGES_PATH = os.path.join(os.path.dirname(__file__), "build_pages.py")

def fetch_html(url=None):
    target = url or TEAM_URL
    try:
        req = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Failed to fetch {target}: {e}")
        return None

def parse_month_results(html, force_year="2026", force_month=None):
    """Parse all finished games from a Yahoo calendar page."""
    # Try to find year/month in the selected nav item
    month_match = re.search(r'bb-scheduleNavi__item--selected[^>]*>(\d+)月', html)
    curr_year = force_year
    curr_month = force_month or (month_match.group(1) if month_match else str(datetime.now().month))

    days = re.findall(r'<td class="bb-calendarTable__data(.*?)</td>', html, re.DOTALL)
    
    all_finished = []
    for day_html in days:
        if "試合終了" in day_html or "中止" in day_html:
            is_cancelled = "中止" in day_html
            
            day_m = re.search(r'class=["\']bb-calendarTable__date["\']>(\d+)', day_html)
            dow_m = re.search(r'class=["\']bb-calendarTable__date["\']>.*?<span[^>]*>\((.*?)\)</span>', day_html, re.DOTALL)
            day = day_m.group(1) if day_m else ""
            dow = dow_m.group(1) if dow_m else ""
            
            is_home = "bb-calendarTable__data--home" in day_html
            
            if is_cancelled:
                symbol = ""
                hawks_s = "中止"
                opp_s = ""
            else:
                symbol_m = re.search(r'aria-label="([^"]+)"', day_html)
                symbol_text = symbol_m.group(1) if symbol_m else ""
                symbol = "○" if "勝利" in symbol_text else "●" if "敗戦" in symbol_text else "△"
                
                h_score_m = re.search(r'class="bb-calendarTable__home[^>]*">(\d+)</span>', day_html)
                a_score_m = re.search(r'class="bb-calendarTable__away[^>]*">(\d+)</span>', day_html)
                h_score = h_score_m.group(1) if h_score_m else "0"
                a_score = a_score_m.group(1) if a_score_m else "0"
                hawks_s, opp_s = (h_score, a_score) if is_home else (a_score, h_score)
            
            opp_name_m = re.search(r'class="bb-calendarTable__teamName">.*?>(.*?)</a>', day_html, re.DOTALL)
            opp_name = opp_name_m.group(1) if opp_name_m else "不明"
            
            opp_logo_m = re.search(r'class="bb-calendarTable__versusLogo.*?--npbTeam(\d+)', day_html)
            opp_id = opp_logo_m.group(1) if opp_logo_m else ""
            
            venue_m = re.search(r'class="bb-calendarTable__venue">(.*?)</p>', day_html)
            venue = venue_m.group(1) if venue_m else ""
            if "ベルーナ" in venue:
                venue = "西武球場"
            
            # Fallback: calculate day-of-week from date if scraping didn't get it
            if not dow:
                try:
                    d = datetime(int(curr_year), int(curr_month), int(day))
                    dow = WEEKDAYS_JP[d.weekday()]
                except Exception:
                    dow = ""
            
            all_finished.append({
                "date_str": f"{curr_year}.{curr_month.zfill(2)}.{day.zfill(2)} ({dow})",
                "short_date": f"{curr_month}/{day} ({dow})",
                "month": curr_month,
                "day": day,
                "venue": venue,
                "hawks_score": hawks_s,
                "opp_score": opp_s,
                "opp_name": opp_name,
                "opp_logo": f"https://npb.jp/img/common/logo/2026/logo_{get_team_code(opp_id, opp_name)}_s.gif",
                "opp_id": opp_id,
                "symbol": symbol,
                "is_visitor": not is_home,
                "is_cancelled": is_cancelled
            })
            
    return all_finished, curr_month

def fetch_all_results():
    """Fetch results for all months that have games (March to current month)."""
    now = datetime.now()
    current_month = now.month
    all_results = []
    
    # Fetch each month from March to current month
    for month in range(3, current_month + 1):
        if month == current_month:
            # Current month uses the base schedule URL
            url = "https://baseball.yahoo.co.jp/npb/teams/12/schedule"
        else:
            # Past months use ?month=YYYY-MM format
            url = f"https://baseball.yahoo.co.jp/npb/teams/12/schedule?month=2026-{month:02d}"
        print(f"Fetching month {month}...")
        html = fetch_html(url)
        if html:
            month_results, _ = parse_month_results(html, force_year="2026", force_month=str(month))
            all_results.extend(month_results)
            print(f"  Found {len(month_results)} finished games in month {month}")
        time.sleep(1)  # Be polite to the server
    
    return all_results

def get_team_code(tid, tname=""):
    name_to_code = {
        "巨人": "g", "DeNA": "db", "阪神": "t", "広島": "c", "中日": "d", "ヤクルト": "s",
        "西武": "l", "ロッテ": "m", "ソフトバンク": "h", "オリックス": "b", "楽天": "e", "日本ハム": "f"
    }
    if tname in name_to_code:
        return name_to_code[tname]
    codes = {"1":"g", "2":"db", "3":"t", "4":"c", "5":"d", "6":"s", "7":"l", "8":"m", "9":"h", "11":"b", "12":"e", "376":"f"}
    return codes.get(tid, "h")

def fetch_hawks_standings():
    """Fetch Hawks rank, record, and games-behind info from Yahoo standings."""
    url = "https://baseball.yahoo.co.jp/npb/standings/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
        rows = re.findall(r'<tr class="bb-rankTable__row">(.*?)</tr>', html, re.DOTALL)
        standings = []
        for r in rows:
            team = re.search(r'bb-rankTable__team[^>]*>(.*?)</a>', r)
            if team:
                t_name = team.group(1).strip()
                if any(t in t_name for t in ['ソフトバンク', '西武', '日本ハム', 'オリックス', 'ロッテ', '楽天']):
                    rank_m = re.search(r'bb-rankTable__data--rank">(\d+)', r)
                    tds = re.findall(r'<td class="bb-rankTable__data[^"]*">(.*?)</td>', r, re.DOTALL)
                    clean_tds = [re.sub(r'<.*?>', '', c).strip() for c in tds]
                    magic_str = ""
                    for td in clean_tds:
                        m_m = re.search(r'M\d+', td)
                        if m_m:
                            magic_str = m_m.group(0)
                            break

                    if rank_m and len(clean_tds) >= 8:
                        standings.append({
                            'rank': int(rank_m.group(1)),
                            'team': t_name,
                            'games': clean_tds[2],
                            'wins': clean_tds[3],
                            'losses': clean_tds[4],
                            'draws': clean_tds[5],
                            'pct': clean_tds[6],
                            'gb': clean_tds[7],
                            'magic': magic_str
                        })
        
        pac_standings = standings[:6]
        hawks_data = next((s for s in pac_standings if 'ソフトバンク' in s['team']), None)
        
        if hawks_data:
            rank = hawks_data['rank']
            wins = hawks_data['wins']
            losses = hawks_data['losses']
            draws = hawks_data['draws']
            record_str = f"{wins}勝 {losses}敗 {draws}分"
            
            if rank == 1:
                second_place = next((s for s in pac_standings if s['rank'] == 2), None)
                gb_val = second_place['gb'] if second_place else "0"
                gb_str = f"ゲーム差 {gb_val}"
            else:
                gb_val = hawks_data['gb']
                gb_str = f"ゲーム差 {gb_val}"
                
            magic_str = hawks_data.get('magic', '')

            return {
                'rank': f"{rank}位",
                'record': record_str,
                'gb': gb_str,
                'magic': magic_str
            }
    except Exception as e:
        print(f"Failed to fetch standings: {e}")
        
    return {
        'rank': "1位",
        'record': "63勝 35敗 1分",
        'gb': "ゲーム差 7.5",
        'magic': "M35"
    }

def update_schedule_all(all_results):
    """Update schedule.html and build_pages.py with ALL game results."""
    for path in [SCHEDULE_PATH, BUILD_PAGES_PATH]:
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            sc_content = f.read()
        
        updated_count = 0
        for game in all_results:
            month = int(game['month'])
            day = int(game['day'])
            if game.get('is_cancelled'):
                res_text = "中止"
            else:
                res_text = f"{game['symbol']} {game['hawks_score']}-{game['opp_score']}"
            
            # Check the current month block, the previous month block, and the next month block
            for t_month in [month - 1, month, month + 1]:
                t_month_str = str(t_month)
                month_start_idx = sc_content.find(f"id='month-{t_month_str}'")
                if month_start_idx == -1:
                    month_start_idx = sc_content.find(f'id="month-{t_month_str}"')
                if month_start_idx == -1:
                    continue
                    
                month_end_idx = sc_content.find("id='month-", month_start_idx + 10)
                if month_end_idx == -1:
                    month_end_idx = sc_content.find('id="month-', month_start_idx + 10)
                if month_end_idx == -1:
                    month_end_idx = len(sc_content)
                    
                month_html = sc_content[month_start_idx:month_end_idx]
                
                cal_days = re.finditer(r"<div class='cal-day([^']*)'>(.*?)</div>", month_html, re.DOTALL)
                
                new_month_html = month_html
                for match_cal in cal_days:
                    day_attrs = match_cal.group(1)
                    day_content = match_cal.group(2)
                    
                    day_num_match = re.search(r"<span class='day-num([^']*)'>(.*?)</span>", day_content)
                    if not day_num_match:
                        continue
                        
                    classes = day_num_match.group(1)
                    day_text = day_num_match.group(2)
                    
                    try:
                        d_val = int(day_text)
                    except ValueError:
                        continue
                    
                    is_match = False
                    if t_month == month and d_val == day and "out-of-month" not in classes:
                        is_match = True
                    elif t_month == month - 1 and d_val == day and "out-of-month" in classes and d_val < 15:
                        is_match = True
                    elif t_month == month + 1 and d_val == day and "out-of-month" in classes and d_val > 15:
                        is_match = True
                    
                    if is_match:
                        if "game-info" in day_content:
                            new_day_content = re.sub(
                                r"(<span class='game-time'>).*?(</span>)", 
                                rf"\g<1>{res_text}\g<2>", 
                                day_content
                            )
                            if new_day_content != day_content:
                                new_month_html = new_month_html.replace(match_cal.group(0), f"<div class='cal-day{day_attrs}'>{new_day_content}</div>")
                                updated_count += 1
                        break # Found the cell for this month block, move to next t_month
                        
                sc_content = sc_content[:month_start_idx] + new_month_html + sc_content[month_end_idx:]
                
        if updated_count > 0:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(sc_content)
            print(f"Updated {updated_count} game results in: {os.path.basename(path)}")
        else:
            print(f"No new updates needed for: {os.path.basename(path)}")

def update_top_page(latest, visitor):
    """Update index.html hero card and portal badge."""
    res_text = f"{latest['hawks_score']}-{latest['opp_score']}"
    standings = fetch_hawks_standings()
    
    # 1. Update Index (Rich Card)
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, 'r', encoding='utf-8') as f: content = f.read()
        
        h_logo = "https://p.npb.jp/img/common/logo/2026/logo_h_l.png"
        
        # Get team code for opp_logo
        opp_logo = f"https://p.npb.jp/img/common/logo/2026/logo_{get_team_code(latest['opp_id'], latest['opp_name'])}_l.png"

        import re
        latest['month'] = latest['month']
        visitor['month'] = visitor['month']
        
        venue_map = {
            '楽天モバイル': '楽天モバイルパーク宮城',
            'ベルーナドーム': '西武球場',
            'ベルーナ': '西武球場',
            '西武球場': '西武球場',
            'ZOZOマリン': 'ZOZOマリンスタジアム',
            '京セラD大阪': '京セラドーム大阪',
            'エスコンF': 'エスコンフィールドHOKKAIDO',
            'みずほPayPay': 'みずほPayPayドーム福岡',
            '東京ドーム': '東京ドーム'
        }
        latest['venue_full'] = venue_map.get(latest['venue'], latest['venue'])
        visitor['venue_full'] = venue_map.get(visitor['venue'], visitor['venue'])
        
        new_card_html = f'''        <div class="latest-result-card" style="position: relative;">
          <div class="result-card-header">
            <a href="./schedule.html#month-{latest['month']}" class="result-date" style="color: inherit; text-decoration: underline; text-decoration-color: rgba(255,255,255,0.4); text-underline-offset: 4px; transition: opacity 0.2s;" onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1"><i class="far fa-calendar-alt"></i> {latest["date_str"]}</a>
            <a href="https://www.google.com/maps/search/?api=1&query={latest['venue_full']}" target="_blank" rel="noopener" class="result-venue" style="color: inherit; text-decoration: none; transition: opacity 0.2s;" onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1"><i class="fas fa-map-marker-alt"></i> {latest["venue"]}</a>
          </div>
          <div class="score-main">
            <div class="team-box">
              <img src="https://p.npb.jp/img/common/logo/2026/logo_h_l.png" alt="ソフトバンク" class="team-logo-large">
              <span class="team-name-short">ソフトバンク</span>
            </div>
            <div class="score-numbers-large">
              <div>{latest["hawks_score"]}</div>
              <span class="score-dash">-</span>
              <div>{latest["opp_score"]}</div>
            </div>
            <div class="team-box">
              <img src="{opp_logo}" alt="{latest["opp_name"]}" class="team-logo-large">
              <span class="team-name-short">{latest["opp_name"]}</span>
            </div>
          </div>
          <div class="result-card-footer-stats">
            <span class="stat-badge stat-badge-rank">{standings['rank']}</span>
            <span class="stat-badge stat-badge-record">{standings['record']}</span>
            <span class="stat-badge stat-badge-gb">{standings['gb']}</span>
            {f'<span class="stat-badge stat-badge-magic">{standings["magic"]}</span>' if standings.get('magic') else ''}
          </div>
        </div>
        <!-- Next Visitor Game Highlight -->
        <div class="visitor-result-mini" onclick="window.location.href='./schedule.html#month-{visitor['month']}'" style="cursor: pointer;">
          <span class="visitor-label">NEXT VISITOR</span>
          <span class="visitor-info-group">
            <span class="visitor-date"><i class="far fa-calendar-alt"></i> {visitor["short_date"]}</span>
            <span class="visitor-opponent">vs {visitor["opp_name"]}</span>
          </span>
          <a href="https://www.google.com/maps/search/?api=1&query={visitor['venue_full']}" target="_blank" rel="noopener" class="visitor-venue" onclick="event.stopPropagation()"><i class="fas fa-map-marker-alt"></i> {visitor["venue"]}</a>
        </div>'''
        
        pattern = r'<!-- GAME_RESULT_START -->.*?<!-- GAME_RESULT_END -->'
        replacement = f'<!-- GAME_RESULT_START -->\n        {new_card_html}\n        <!-- GAME_RESULT_END -->'
        
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(INDEX_PATH, 'w', encoding='utf-8') as f: f.write(content)
        print("Updated Index with Rich Card")

    # 1b. Update Portal (Simple Badge)
    if os.path.exists(PORTAL_PATH):
        with open(PORTAL_PATH, 'r', encoding='utf-8') as f: p_content = f.read()
        p_badge_html = f'<span class="result-badge-portal"><span class="result-label-portal">LATEST RESULT</span>{res_text}</span>'
        p_pattern = r'<!-- GAME_RESULT_START -->.*?<!-- GAME_RESULT_END -->'
        p_replacement = f'<!-- GAME_RESULT_START -->\n            {p_badge_html}\n            <!-- GAME_RESULT_END -->'
        new_p_content = re.sub(p_pattern, p_replacement, p_content, flags=re.DOTALL)
        with open(PORTAL_PATH, 'w', encoding='utf-8') as f: f.write(new_p_content)
        print("Updated Portal with Simple Badge")

def auto_deploy():
    """Git add, commit, push to deploy the updated game result."""
    import subprocess
    if os.environ.get("GITHUB_ACTIONS"):
        print("Running inside GitHub Actions workflow. Skipping internal git push.")
        return

    repo_dir = os.path.join(os.path.dirname(__file__), "..")
    try:
        subprocess.run(["git", "add", "-A"], cwd=repo_dir, check=True, timeout=30)
        result = subprocess.run(["git", "status", "--porcelain"], cwd=repo_dir, capture_output=True, text=True, timeout=30)
        if not result.stdout.strip():
            print("No changes to deploy.")
            return
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.run(["git", "commit", "-m", f"試合結果自動更新 {now}"], cwd=repo_dir, check=True, timeout=30)
        subprocess.run(["git", "push", "origin", "main"], cwd=repo_dir, check=True, timeout=60)
        print("Auto-deploy completed successfully.")
    except Exception as e:
        print(f"Auto-deploy notice (non-fatal): {e}")

if __name__ == "__main__":
    print("Starting full game result update...")
    
    # Fetch ALL months' results
    all_results = fetch_all_results()
    
    if all_results:
        # Update schedule with ALL results
        update_schedule_all(all_results)
        
        # Update top page with latest result and NEXT visitor game from data.txt
        finished_games = [g for g in all_results if not g.get('is_cancelled')]
        if finished_games:
            latest = finished_games[-1]
            
            # Extract latest finished game date to ensure NEXT VISITOR is strictly AFTER latest game
            latest_date = None
            if latest and latest.get('date_str'):
                lm = re.search(r'(\d{4})\.(\d{2})\.(\d{2})', latest['date_str'])
                if lm:
                    latest_date = datetime(int(lm.group(1)), int(lm.group(2)), int(lm.group(3))).date()
            
            # Find next upcoming visitor game from data.txt
            next_visitor = None
            data_txt_path = os.path.join(os.path.dirname(__file__), "data.txt")
            if os.path.exists(data_txt_path):
                today_now = datetime.now()
                # Ensure game is after latest finished game, but allow today's upcoming game
                visitor_venues = ["ZOZOマリン", "エスコン", "楽天モバイル", "西武球場", "京セラD大阪", "甲子園", "バンテリン", "横浜", "マツダスタジアム", "東京ドーム", "ベルーナドーム"]
                with open(data_txt_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        parts = line.strip().split('\t')
                        if len(parts) >= 4:
                            d_str, dow, opp, v_name = parts[:4]
                            m_match = re.match(r'(\d+)月(\d+)日', d_str)
                            if m_match:
                                m_val, d_val = int(m_match.group(1)), int(m_match.group(2))
                                try:
                                    g_date = datetime(2026, m_val, d_val)
                                    # Always auto-calculate correct day-of-week to prevent human error
                                    correct_dow = WEEKDAYS_JP[g_date.weekday()]
                                    if "祝" in dow:
                                        correct_dow += "・祝"
                                        
                                    if (latest_date is None or g_date.date() > latest_date) and any(vv in v_name for vv in visitor_venues):
                                        next_visitor = {
                                            "short_date": f"{m_val}/{d_val} ({correct_dow})",
                                            "month": str(m_val),
                                            "opp_name": opp,
                                            "venue": v_name,
                                            "venue_full": v_name
                                        }
                                        break
                                except Exception:
                                    pass
            
            if not next_visitor:
                # Dynamic fallback with guaranteed correct weekday calculation
                today_dt = datetime.now()
                correct_dow = WEEKDAYS_JP[today_dt.weekday()]
                next_visitor = {
                    "short_date": f"{today_dt.month}/{today_dt.day} ({correct_dow})",
                    "month": str(today_dt.month),
                    "opp_name": "西武",
                    "venue": "西武球場",
                    "venue_full": "西武球場"
                }
                
            update_top_page(latest, next_visitor)
        
        # Auto deploy
        auto_deploy()
        
        print(f"Done! Updated {len(all_results)} total game results.")
    else:
        print("No game results found.")
