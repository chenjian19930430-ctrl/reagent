from ai.agents.base import BaseAgent

class SummaryAgent(BaseAgent):
    async def process(self, input_data: dict) -> dict:
        text = input_data.get("text",""); max_length = input_data.get("max_length",200)
        return {"summary":text[:max_length]+("..." if len(text)>max_length else ""),"original_length":len(text),"summary_length":min(len(text),max_length)}
    async def validate(self, output: dict) -> bool:
        return bool(output.get("summary"))
