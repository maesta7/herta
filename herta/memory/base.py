from abc import ABC, abstractmethod
from typing_extensions import Literal
from herta.inputs import System_msg, Human_msg, AI_msg
from typing import Literal, Union

class BaseChatMemory(ABC):

    @abstractmethod
    async def add_msg(self, user_id: str, msg: Union[System_msg, Human_msg, AI_msg]) -> None:
        pass

    @abstractmethod
    async def get_msg(self, user_id: str, max_memory_turn: int) -> object:
        pass

    @abstractmethod
    async def clr_msg(self, user_id: str) -> None:
        pass