import hashlib, json
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

class LLMClient:
    def __init__(self, api_key: str = "", base_url: str = "https://api.deepseek.com/v1", model: str = "deepseek-chat"):
        self.api_key = api_key; self.base_url = base_url; self.model = model
        self.cache = {}
    def _cache_key(self, messages: list) -> str:
        return hashlib.md5(json.dumps(messages, sort_keys=True).encode()).hexdigest()
    @retry(stop=stop_after_attempt(3),wait=wait_exponential(multiplier=1,min=2,max=10))
    async def chat(self, messages: list, temperature: float = 0.7) -> str:
        key = self._cache_key(messages)
        if key in self.cache: return self.cache[key]
        headers = {"Authorization":f"Bearer {self.api_key}","Content-Type":"application/json"}
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(f"{self.base_url}/chat/completions",json={"model":self.model,"messages":messages,"temperature":temperature},headers=headers)
            resp.raise_for_status()
            result = resp.json()["choices"][0]["message"]["content"]
            self.cache[key] = result
            return result
