from abc import ABC, abstractmethod

class BaseEmbedding(ABC):
    @abstractmethod
    async def embed_docs(self, *args: any, **kwargs: any) -> list[list[float]]:
        pass

    @abstractmethod
    async def embed_querys(self, *args: any, **kwargs: any) -> list[list[float]]:
        pass