from ai.agents.base import BaseAgent

class IntentClassifier(BaseAgent):
    INTENTS = {"pricing":"价格咨询","product":"产品咨询","tech":"技术支持","complaint":"投诉","other":"其他"}
    async def process(self, input_data: dict) -> dict:
        message = input_data.get("message","").lower()
        if any(k in message for k in ["price","pricing","cost","多少钱","价格"]): intent="pricing"
        elif any(k in message for k in ["how","what","功能","怎么用"]): intent="product"
        else: intent="other"
        return {"intent":intent,"intent_label":self.INTENTS[intent],"confidence":0.85}
    async def validate(self, output: dict) -> bool:
        return output.get("intent") in self.INTENTS
