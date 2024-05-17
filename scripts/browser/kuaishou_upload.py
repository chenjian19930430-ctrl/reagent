"""Kuaishou video auto-upload."""
from playwright.async_api import async_playwright

class KuaishouUploader:
    async def upload(self, video_path: str, title: str):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto("https://cp.kuaishou.com/article/publish/video")
            await page.set_input_files("input[type=file]", video_path)
            await page.fill(".title-input", title)
            await page.click(".publish-btn")
            await browser.close()
            return {"status":"published","platform":"kuaishou","title":title}
