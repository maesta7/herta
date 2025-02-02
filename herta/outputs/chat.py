from pydantic import BaseModel, Field
from typing import Any, Literal

class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    extra_tokens: Any

class OutputLLM(BaseModel):
    type: str = Literal["msg", "tool_calls"]
    content: Any
    usage: Usage