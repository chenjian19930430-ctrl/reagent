import asyncio
from typing import List, Dict, Any
from tenacity import retry, stop_after_attempt, wait_exponential

class AgentOrchestrator:
    def __init__(self):
        self.agents = {}
    def register(self, name: str, agent: Any):
        self.agents[name] = agent
    @retry(stop=stop_after_attempt(3),wait=wait_exponential(multiplier=1,min=2,max=10))
    async def execute(self, agent_name: str, input_data: dict) -> dict:
        agent = self.agents.get(agent_name)
        if not agent: raise ValueError(f"Agent {agent_name} not found")
        result = await agent.process(input_data)
        valid = await agent.validate(result)
        if not valid: raise ValueError(f"Agent {agent_name} produced invalid output")
        return result
    async def pipeline(self, steps: List[Dict]) -> List[Dict]:
        return [await self.execute(step["agent"], step["input"]) for step in steps]
