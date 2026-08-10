import os
import shutil
from playwright.sync_api import sync_playwright

DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(DIR, ".."))

def generate_pdf(html_path, pdf_path, format_size='A3', landscape=True):
    abs_html = os.path.abspath(html_path)
    abs_pdf = os.path.abspath(pdf_path)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f'file:///{abs_html.replace("\\", "/")}')
        page.pdf(
            path=abs_pdf,
            format=format_size,
            landscape=landscape,
            print_background=True,
            margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'}
        )
        browser.close()
    print(f"Generated PDF: {pdf_path}")

if __name__ == '__main__':
    digital_html = os.path.join(PROJECT_ROOT, 'FightSong', 'digital-sheet.html')
    print_html = os.path.join(PROJECT_ROOT, 'FightSong', 'print_ouenka_2026.html')
    nankai_html = os.path.join(PROJECT_ROOT, 'FightSong', 'print_nankai_sheet.html')
    
    pdf_v2 = os.path.join(PROJECT_ROOT, 'FightSong', 'ouenka_2026_v2.pdf')
    pdf_v1 = os.path.join(PROJECT_ROOT, 'FightSong', 'ouenka_2026.pdf')
    pdf_print = os.path.join(PROJECT_ROOT, 'FightSong', 'print_ouenka_2026.pdf')
    pdf_nankai = os.path.join(PROJECT_ROOT, 'FightSong', 'nankai_ouenka_2026.pdf')

    generate_pdf(digital_html, pdf_v2, format_size='A3', landscape=True)
    if os.path.exists(pdf_v2):
        shutil.copy2(pdf_v2, pdf_v1)
        
    generate_pdf(print_html, pdf_print, format_size='A3', landscape=True)
    # if os.path.exists(nankai_html):
    #     generate_pdf(nankai_html, pdf_nankai, format_size='A4', landscape=False)
        
    print("All PDFs successfully re-generated!")
