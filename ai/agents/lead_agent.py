from ai.agents.base import BaseAgent

class LeadScoringAgent(BaseAgent):
    async def process(self, input_data: dict) -> dict:
        industry_match = input_data.get("industry_match",0.5)
        engagement = input_data.get("engagement_score",0.5)
        budget = input_data.get("budget_level",0.5)
        score = (industry_match*0.3 + engagement*0.3 + budget*0.2)*100
        return {"score":round(score,1),"dimensions":{"industry_match":industry_match*100,"engagement":engagement*100,"budget":budget*100},"recommendation":"优先跟进" if score>=70 else "持续培育"}
    async def validate(self, output: dict) -> bool:
        return 0 <= output.get("score",0) <= 100
