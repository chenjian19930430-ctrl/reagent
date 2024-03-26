from ai.agents.base import BaseAgent

class VideoScriptAgent(BaseAgent):
    async def process(self, input_data: dict) -> dict:
        title = input_data.get("title",""); platform = input_data.get("platform","douyin")
        return {"title":title,"script":f"AI生成脚本: {title} - 适配{platform}平台","duration":60}
    async def validate(self, output: dict) -> bool:
        return bool(output.get("script"))
