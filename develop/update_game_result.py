import os
import re
import urllib.request
from datetime import datetime

# Settings
TEAM_URL = "https://baseball.yahoo.co.jp/npb/teams/12/"
WEEKDAYS_JP = ['月', '火', '水', '木', '金', '土', '日']
INDEX_PATH = os.path.join(os.path.dirname(__file__), "../HP/index.html")
PORTAL_PATH = os.path.join(os.path.dirname(__file__), "../portal/index.html")
SCHEDULE_PATH = os.path.join(os.path.dirname(__file__), "../HP/schedule.html")
BUILD_PAGES_PATH = os.path.join(os.path.dirname(__file__), "build_pages.py")

def fetch_html():
    try:
        req = urllib.request.Request(TEAM_URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Failed to fetch: {e}")
        return None

def parse_latest_result(html):
    # Focus on the main calendar area to avoid legacy support messages
    cal_area = re.search(r'class=["\']bb-calendarTable["\'].*?</table>', html, re.DOTALL)
    cal_html = cal_area.group(0) if cal_area else html
    
    # Try to find year/month in the selected nav item
    month_match = re.search(r'bb-scheduleNavi__item--selected[^>]*>(\d+)月', html)
    
    # For 2026 season, we can safely default or search specifically
    curr_year = "2026" 
    curr_month = month_match.group(1) if month_match else str(datetime.now().month)

    days = re.findall(r'<td class="bb-calendarTable__data(.*?)</td>', html, re.DOTALL)
    
    all_finished = []
    for day_html in days:
        if "試合終了" in day_html:
            day_m = re.search(r'class=["\']bb-calendarTable__date["\']>(\d+)', day_html)
            dow_m = re.search(r'class=["\']bb-calendarTable__date["\']>.*?<span[^>]*>\((.*?)\)</span>', day_html, re.DOTALL)
            day = day_m.group(1) if day_m else ""
            dow = dow_m.group(1) if dow_m else ""
            
            is_home = "bb-calendarTable__data--home" in day_html
            
            symbol_m = re.search(r'aria-label="([^"]+)"', day_html)
            symbol_text = symbol_m.group(1) if symbol_m else ""
            symbol = "○" if "勝利" in symbol_text else "×" if "敗戦" in symbol_text else "△"
            
            h_score_m = re.search(r'class="bb-calendarTable__home[^>]*">(\d+)</span>', day_html)
            a_score_m = re.search(r'class="bb-calendarTable__away[^>]*">(\d+)</span>', day_html)
            h_score = h_score_m.group(1) if h_score_m else "0"
            a_score = a_score_m.group(1) if a_score_m else "0"
            
            opp_name_m = re.search(r'class="bb-calendarTable__teamName">.*?>(.*?)</a>', day_html, re.DOTALL)
            opp_name = opp_name_m.group(1) if opp_name_m else "不明"
            
            opp_logo_m = re.search(r'class="bb-calendarTable__versusLogo.*?--npbTeam(\d+)', day_html)
            opp_id = opp_logo_m.group(1) if opp_logo_m else ""
            opp_logo = f"https://npb.jp/img/common/logo/2026/logo_{get_team_code(opp_id)}_s.gif"
            
            venue_m = re.search(r'class="bb-calendarTable__venue">(.*?)</p>', day_html)
            venue = venue_m.group(1) if venue_m else ""
            
            hawks_s, opp_s = (h_score, a_score) if is_home else (a_score, h_score)
            
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
                "opp_logo": opp_logo,
                "opp_id": opp_id,
                "symbol": symbol,
                "is_visitor": not is_home
            })
            
    if not all_finished:
        return None
        
    latest = all_finished[-1]
    latest_visitor = next((g for g in reversed(all_finished) if g["is_visitor"]), None)
    
    return {
        "latest": latest,
        "visitor": latest_visitor
    }

def get_team_code(tid):
    # Mapping for p.npb.jp/img/common/logo/2026/logo_{code}_l.png
    codes = {"1":"g", "2":"db", "3":"t", "4":"c", "5":"d", "6":"s", "7":"l", "8":"m", "9":"h", "11":"b", "12":"e", "376":"f"}
    return codes.get(tid, "h")

def update_files(data):
    if not data: return
    latest = data["latest"]
    visitor = data["visitor"]
    res_text = f"{latest['symbol']}{latest['hawks_score']}-{latest['opp_score']}"
    
    # 1. Update Index (Rich Card)
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, 'r', encoding='utf-8') as f: content = f.read()
        
        # High-Res Logos
        h_logo = "https://p.npb.jp/img/common/logo/2026/logo_h_l.png"
        opp_logo = f"https://p.npb.jp/img/common/logo/2026/logo_{get_team_code(latest['opp_id'])}_l.png"

        new_card_html = f'''<div class="latest-result-card" style="position: relative;">
          <div class="result-card-header">
            <span class="result-date">{latest["date_str"]}</span>
            <span class="result-venue">{latest["venue"]}</span>
          </div>
          <div class="score-main">
            <div class="team-box">
              <img src="{h_logo}" alt="ソフトバンク" class="team-logo-large">
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
        </div>
        <!-- Latest Visitor Result Highlight -->
        <div class="visitor-result-mini">
          <span class="visitor-label">LATEST VISITOR</span>
          <span class="visitor-date">{visitor["short_date"]}</span>
          <span class="visitor-score">{visitor["hawks_score"]}-{visitor["opp_score"]} vs {visitor["opp_name"]}</span>
          <span class="visitor-venue">@{visitor["venue"]}</span>
        </div>'''
        
        pattern = r'<!-- GAME_RESULT_START -->.*?<!-- GAME_RESULT_END -->'
        replacement = f'<!-- GAME_RESULT_START -->\n        {new_card_html}\n        <!-- GAME_RESULT_END -->'
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(INDEX_PATH, 'w', encoding='utf-8') as f: f.write(new_content)
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

    # 2. Update Schedule & Build Script (same as before)
    res_text = f"{latest['symbol']}{latest['hawks_score']}-{latest['opp_score']}"
    for path in [SCHEDULE_PATH, BUILD_PAGES_PATH]:
        if not os.path.exists(path): continue
        with open(path, 'r', encoding='utf-8') as f: sc_content = f.read()
        month_pattern = rf"id=['\"]month-{latest['month']}['\"].*?day-num[^>]*>{latest['day']}</span>.*?game-time['\"]>(\d+:\d+|[○×△]\s*\d+-\d+)</span>"
        if re.search(month_pattern, sc_content, re.DOTALL):
            def repl(m): return m.group(0).replace(m.group(1), res_text)
            new_sc = re.sub(month_pattern, repl, sc_content, flags=re.DOTALL)
            with open(path, 'w', encoding='utf-8') as f: f.write(new_sc)
            print(f"Updated Schedule: {path}")

def auto_deploy():
    """Git add, commit, push to deploy the updated game result."""
    import subprocess
    repo_dir = os.path.join(os.path.dirname(__file__), "..")
    try:
        subprocess.run(["git", "add", "-A"], cwd=repo_dir, check=True)
        result = subprocess.run(["git", "status", "--porcelain"], cwd=repo_dir, capture_output=True, text=True)
        if not result.stdout.strip():
            print("No changes to deploy.")
            return
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.run(["git", "commit", "-m", f"試合結果自動更新 {now}"], cwd=repo_dir, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=repo_dir, check=True)
        print("Auto-deploy completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Auto-deploy failed: {e}")

if __name__ == "__main__":
    print("Starting rich game result update...")
    html_content = fetch_html()
    if html_content:
        result_data = parse_latest_result(html_content)
        if result_data:
            update_files(result_data)
            auto_deploy()
        else:
            print("Failed to parse result.")
    else:
        print("Failed to fetch HTML.")
