from abc import ABC, abstractmethod
from typing import AsyncIterator

class BaseLLM(ABC):
    """
    Base LLM Class for Using inside Herta Agent Framework.
    """
    @abstractmethod
    async def chat(self, *args: any, **kwargs: any) -> str:
        pass

    @abstractmethod
    async def stream(self, *args: any, **kwargs: any) -> AsyncIterator[str]:
        pass

    @abstractmethod
    def _get_tools_schema(self, *args: any, **kwargs):
        pass