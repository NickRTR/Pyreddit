import json
from playwright.sync_api import sync_playwright, ViewportSize

def createImages(assignments):
    print("Downloading screenshots of reddit posts...")

    with sync_playwright() as p:
        print("Launching Headless Browser...")
        browser = p.chromium.launch()
        context = browser.new_context()

        # cookie_file = open("./cookies/cookie-dark-mode.json", encoding="utf-8") # dark mode
        cookie_file = open("./cookies/cookie-light-mode.json", encoding="utf-8") # light mode
        cookies = json.load(cookie_file)
        context.add_cookies(cookies)  # load preference cookies
        page = context.new_page()

        for assignment in assignments:
            page.goto(assignment["url"], timeout=0)
            page.set_viewport_size(ViewportSize(width=1920, height=1080))

            if page.locator('[data-testid="content-gate"]').is_visible():
                # This means the post is NSFW and requires to click the proceed button.
                page.locator('[data-testid="content-gate"] button').click()
                page.locator(
                    '[data-click-id="text"] button'
                ).click()  # Remove "Click to see nsfw" Button in Screenshot

            # if assignment is a comment, select comment instead of post / question
            if (assignment["title"] == "question"):
                page.locator('[data-test-id="post-content"]').screenshot(path=f"./images/{assignment['title']}.png")
            else:
                page.locator(f'#t1_{assignment["commentId"]}').screenshot(path=f"./images/{assignment['title']}.png")

            print("Successfully created screenshot!")