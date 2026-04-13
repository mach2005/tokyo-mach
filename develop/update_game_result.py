import os
import re
import urllib.request
import datetime
from datetime import datetime

# Settings
TEAM_URL = "https://baseball.yahoo.co.jp/npb/teams/12/"
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
    # Extract month from the selected navigation item or title
    # Yahoo uses .bb-scheduleNavi__item--selected for the current month
    month_match = re.search(r'bb-scheduleNavi__item--selected[^>]*>(\d+)月', html)
    if not month_match:
        month_match = re.search(r'bb-calendarTable__title[^>]*>(\d+)年(\d+)月', html)
        month = month_match.group(2) if month_match else str(datetime.now().month)
    else:
        month = month_match.group(1)
    
    days = re.findall(r'<td class="bb-calendarTable__data(.*?)</td>', html, re.DOTALL)
    
    latest_game = None
    latest_day = None
    for day_html in days:
        if "試合終了" in day_html:
            latest_game = day_html
            # Extract day (e.g., class="bb-calendarTable__date">12)
            day_match = re.search(r'class=["\']bb-calendarTable__date["\']>(\d+)', day_html)
            if day_match:
                latest_day = day_match.group(1)
    
    if not latest_game:
        print("No completed game found in current view.")
        return None
    
    is_home = "bb-calendarTable__data--home" in latest_game
    symbol_match = re.search(r'aria-label="([^"]+)"', latest_game)
    symbol_text = symbol_match.group(1) if symbol_match else ""
    
    if "勝利" in symbol_text: symbol = "○"
    elif "敗戦" in symbol_text: symbol = "×"
    else: symbol = "△"
    
    home_score_m = re.search(r'class="bb-calendarTable__home[^>]*">(\d+)</span>', latest_game)
    away_score_m = re.search(r'class="bb-calendarTable__away[^>]*">(\d+)</span>', latest_game)
    
    if not home_score_m or not away_score_m:
        print("Could not parse scores.")
        return None
    
    h_val, a_val = home_score_m.group(1), away_score_m.group(1)
    hawks_score, opp_score = (h_val, a_val) if is_home else (a_val, h_val)
        
    return {
        "text": f"{symbol}{hawks_score}-{opp_score}",
        "month": month,
        "day": latest_day
    }

def update_files(result):
    if not result:
        return
    
    result_text = result["text"]
    month = result["month"]
    day = result["day"]

    # 1. Update Landing Pages (Hero Badge)
    landing_targets = [
        {"path": INDEX_PATH, "label_cls": "result-label", "badge_cls": "result-badge", "indent": "      "},
        {"path": PORTAL_PATH, "label_cls": "result-label-portal", "badge_cls": "result-badge-portal", "indent": "            "}
    ]

    for target in landing_targets:
        path = target["path"]
        if not os.path.exists(path): continue
        with open(path, 'r', encoding='utf-8') as f: content = f.read()
        
        new_badge_html = f'<span class="{target["badge_cls"]}"><span class="{target["label_cls"]}">LATEST RESULT</span>{result_text}</span>'
        pattern = r'<!-- GAME_RESULT_START -->.*?<!-- GAME_RESULT_END -->'
        replacement = f'<!-- GAME_RESULT_START -->\n{target["indent"]}{new_badge_html}\n{target["indent"]}<!-- GAME_RESULT_END -->'
        
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            with open(path, 'w', encoding='utf-8') as f: f.write(new_content)
            print(f"Updated Landing: {path}")

    # 2. Update Schedule Pages (Calendar Days)
    schedule_targets = [SCHEDULE_PATH, BUILD_PAGES_PATH]
    for path in schedule_targets:
        if not os.path.exists(path): continue
        with open(path, 'r', encoding='utf-8') as f: content = f.read()
        
        # Regex to find the specific month and day block
        # We look for the month ID/title first, then the day span, then the game-time
        # In schedule.html: <div class='calendar-wrapper' id='month-4'> ... <span class='day-num...'>12</span> ... <span class='game-time'>13:00</span>
        
        # This is a bit complex. We'll search for the day-num span followed by game-time.
        # Since months are separated, we'll try to find the block for the month if possible.
        month_pattern = rf"id=['\"]month-{month}['\"].*?day-num[^>]*>{day}</span>.*?game-time['\"]>(\d+:\d+|[○×△]\d+-\d+)</span>"
        
        if re.search(month_pattern, content, re.DOTALL):
            # Replace only the time part
            # We use a sub function to only replace the captured group
            def repl(m):
                full_match = m.group(0)
                time_part = m.group(1)
                return full_match.replace(time_part, result_text)
            
            new_content = re.sub(month_pattern, repl, content, flags=re.DOTALL)
            with open(path, 'w', encoding='utf-8') as f: f.write(new_content)
            print(f"Updated Schedule: {path}")
        else:
            print(f"Calendar entry for {month}/{day} not found in {path}")

if __name__ == "__main__":
    print("Starting comprehensive game result update...")
    html_content = fetch_html()
    if html_content:
        result_data = parse_latest_result(html_content)
        if result_data:
            update_files(result_data)
        else:
            print("Failed to parse result.")
    else:
        print("Failed to fetch HTML.")
