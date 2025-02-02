from pydantic import BaseModel
from typing import Literal, Union, Optional

# =================================================================
# Base class for Message objects
# =================================================================

class BaseContent(BaseModel):
    content: Union[str, list[dict]]

class BaseMsg(BaseModel):
    role: str
    name: Optional[str] = None
    content: BaseContent

# =================================================================
# Tool Calling Class
# =================================================================

class ToolCall(BaseModel):
    id: str
    type: str

class Function(BaseModel):
    name: str
    arguments: str

class FunctionCall(ToolCall):
    type: str = Literal["function"]
    function: Function

# =================================================================
# Message
# =================================================================

class System_msg(BaseMsg):
    role: str = Literal["system"]

class AI_msg(BaseMsg):
    role: str = Literal["assistant"]
    tool_calls: Optional[list[FunctionCall]] = None

class Human_msg(BaseMsg):
    role: str = Literal["user"]

class Tool_msg(BaseMsg):
    role: str = Literal["tool"]
    tool_call_id: str