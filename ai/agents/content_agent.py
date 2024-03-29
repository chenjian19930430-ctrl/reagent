from ai.agents.base import BaseAgent

class ContentGenerationAgent(BaseAgent):
    async def process(self, input_data: dict) -> dict:
        content_type = input_data.get("type","social_post")
        product = input_data.get("product_name","ReAgent")
        templates = {"social_post":f"【新品推荐】{product} - AI驱动营销新体验！","email":f"主题: {product} 助力您的业务增长"}
        return {"content":templates.get(content_type,templates["social_post"]),"type":content_type}
    async def validate(self, output: dict) -> bool:
        return bool(output.get("content"))
