"""Multi-platform scheduled publishing scheduler."""
import asyncio
from datetime import datetime

class PublishScheduler:
    def __init__(self):
        self.tasks = []
    def add_task(self, platform:str, video_path:str, title:str, publish_time:str):
        self.tasks.append({"platform":platform,"video_path":video_path,"title":title,"publish_time":publish_time})
    async def run_scheduled(self):
        while True:
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            pending = [t for t in self.tasks if t["publish_time"] == now]
            for task in pending:
                if task["platform"] == "douyin":
                    from scripts.browser.douyin_upload import DouyinUploader
                    await DouyinUploader().upload(task["video_path"], task["title"])
                elif task["platform"] == "kuaishou":
                    from scripts.browser.kuaishou_upload import KuaishouUploader
                    await KuaishouUploader().upload(task["video_path"], task["title"])
                self.tasks.remove(task)
            await asyncio.sleep(60)
