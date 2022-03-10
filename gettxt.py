from bs4 import BeautifulSoup
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://twitter.com/aichan_nel")
    time.sleep(10)
    page.screenshot(path="twitter.png")
    print(page.content())
    browser.close()

# r = requests.get("https://twitter.com/aichan_nel", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})

# print(r.text)
