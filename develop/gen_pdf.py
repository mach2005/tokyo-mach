from playwright.sync_api import sync_playwright

def generate_pdf(html_path, pdf_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f'file:///{html_path}')
        page.pdf(
            path=pdf_path,
            format='A3',
            landscape=True,
            print_background=True,
            margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'}
        )
        browser.close()

if __name__ == '__main__':
    generate_pdf('c:/Users/user/Antigravity/東京真隼/FightSong/digital-sheet.html', 'c:/Users/user/Antigravity/東京真隼/FightSong/ouenka_2026_v2.pdf')
    generate_pdf('c:/Users/user/Antigravity/東京真隼/FightSong/print_ouenka_2026.html', 'c:/Users/user/Antigravity/東京真隼/FightSong/print_ouenka_2026.pdf')
    generate_pdf('c:/Users/user/Antigravity/東京真隼/FightSong/print_nankai_sheet.html', 'c:/Users/user/Antigravity/東京真隼/FightSong/nankai_ouenka_2026.pdf')
    print("Done")
