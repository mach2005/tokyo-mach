import os
import re
import urllib.request
from datetime import datetime

# Settings
TEAM_URL = "https://baseball.yahoo.co.jp/npb/teams/12/"
INDEX_PATH = os.path.join(os.path.dirname(__file__), "../HP/index.html")

def fetch_html():
    try:
        # User-Agent is required to avoid 403/block
        req = urllib.request.Request(TEAM_URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Failed to fetch: {e}")
        return None

def parse_latest_result(html):
    # Search for calendar cells
    # Selector logic: .bb-calendarTable td
    days = re.findall(r'<td class="bb-calendarTable__data(.*?)</td>', html, re.DOTALL)
    
    latest_game = None
    # We want the LAST game that is "試合終了" (Finished)
    for day in days:
        if "試合終了" in day:
            latest_game = day
    
    if not latest_game:
        print("No completed game found in current view.")
        return None
    
    # Hawks Home/Away detection
    # bb-calendarTable__data--home class means Hawks is Home
    is_home = "bb-calendarTable__data--home" in latest_game
    
    # Result Symbol (aria-label="勝利" etc.)
    symbol_match = re.search(r'aria-label="([^"]+)"', latest_game)
    symbol_text = symbol_match.group(1) if symbol_match else ""
    
    if "勝利" in symbol_text:
        symbol = "○"
    elif "敗戦" in symbol_text:
        symbol = "×"
    else:
        symbol = "△"
    
    # Scores
    # <span class="bb-calendarTable__home ...">7</span>
    # <span class="bb-calendarTable__away ...">11</span>
    home_score_m = re.search(r'class="bb-calendarTable__home[^>]*">(\d+)</span>', latest_game)
    away_score_m = re.search(r'class="bb-calendarTable__away[^>]*">(\d+)</span>', latest_game)
    
    if not home_score_m or not away_score_m:
        print("Could not parse scores.")
        return None
    
    h_val = home_score_m.group(1)
    a_val = away_score_m.group(1)
    
    # Hawks is always on the left
    if is_home:
        hawks_score = h_val
        opp_score = a_val
    else:
        hawks_score = a_val
        opp_score = h_val
        
    return f"{symbol}{hawks_score}-{opp_score}"

def update_index(result_text):
    if not result_text:
        return

    if not os.path.exists(INDEX_PATH):
        print(f"File not found: {INDEX_PATH}")
        return

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate the HTML snippet
    new_badge_html = f'<span class="result-badge"><span class="result-label">LATEST RESULT</span>{result_text}</span>'
    
    pattern = r'<!-- GAME_RESULT_START -->.*?<!-- GAME_RESULT_END -->'
    replacement = f'<!-- GAME_RESULT_START -->\n      {new_badge_html}\n      <!-- GAME_RESULT_END -->'
    
    if not re.search(pattern, content, re.DOTALL):
        print("Marker <!-- GAME_RESULT_START --> not found in index.html")
        return
        
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully updated {INDEX_PATH} with {result_text}")

if __name__ == "__main__":
    print("Starting game result update...")
    html_content = fetch_html()
    if html_content:
        result = parse_latest_result(html_content)
        if result:
            update_index(result)
        else:
            print("Failed to parse result.")
    else:
        print("Failed to fetch HTML.")
