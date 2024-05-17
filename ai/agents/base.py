from abc import ABC, abstractmethod
from typing import Any

class BaseAgent(ABC):
    @abstractmethod
    async def process(self, input_data: Any) -> Any: ...
    @abstractmethod
    async def validate(self, output: Any) -> bool: ...
