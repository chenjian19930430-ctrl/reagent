"""Douyin video auto-upload using Playwright."""
from playwright.async_api import async_playwright

class DouyinUploader:
    def __init__(self, cookie_path: str = "cookies/douyin.json"):
        self.cookie_path = cookie_path
    async def upload(self, video_path: str, title: str, description: str = ""):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto("https://creator.douyin.com/creator-micro/content/upload")
            await page.wait_for_selector("input[type=file]").set_input_files(video_path)
            await page.fill(".title-input", title)
            await page.fill(".desc-textarea", description)
            await page.click(".publish-btn")
            await browser.close()
            return {"status":"published","platform":"douyin","title":title}
