from typing import Optional, Literal, Union
from pydantic import BaseModel, Field
        
class Tool_parameter(BaseModel):
    name: str = Field(description="ชื่อของ params")
    description: str = Field(description="รายละเอียดของ params")
    type: str = Literal["string", "number", "boolean"]
    enum: Optional[list] = None

class Array_parameter(Tool_parameter):
    type: str = Literal["array"]
    items: list[Tool_parameter]

class Object_parameter(Tool_parameter):
    type: str = Literal["object"]
    properties: list[Tool_parameter]

class BaseTool(BaseModel):

    name: str = Field(description="ชื่อของ Tools ที่ LLM จะเห็นในระบบ")
    description: str = Field(description="รายละเอียดของ Tools ที่ต้องการจะใช้")
    parameters: Optional[list[Union[Tool_parameter, Array_parameter, Object_parameter]]] = None
    require: list[str] = None
    endpoint: str = Field(description="endpoint ที่จะทำการเรียกใช้ Tools")
    method: str = Literal["GET", "POST"]