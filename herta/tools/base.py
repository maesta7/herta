from typing import Optional, Literal, Union
from pydantic import BaseModel
        
class Tool_parameter(BaseModel):
    name: str
    description: str
    type: str = Literal["string", "number", "boolean"]
    enum: Optional[list] = None

class Array_parameter(Tool_parameter):
    type: str = Literal["array"]
    items: list[Tool_parameter]

class Object_parameter(Tool_parameter):
    type: str = Literal["object"]
    properties: list[Tool_parameter]

class BaseTool(BaseModel):
    name: str
    description: str
    parameters: Optional[list[Union[Tool_parameter, Array_parameter, Object_parameter]]] = None
    require: list[str] = None
    endpoint: str
    method: str = Literal["GET", "POST"]