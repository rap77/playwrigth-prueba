from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.facebook.com/")

    # Fill out a login form
    page.fill("#email", "rafael.padron773@proton.me")
    page.fill("#pass", "@Rp230594.Facebook@")
    page.click("button[type=submit]")

    # Wait for navigation after login
    page.wait_for_event("timeout",3000)
    print("Logged in and navigated to:", page.url())

    browser.close()

with sync_playwright() as playwright:
    run(playwright)