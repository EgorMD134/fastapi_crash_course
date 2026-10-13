from pydantic import BaseModel,ConfigDict

from typing import Optional,Annotated

class STaskAdd(BaseModel):
    name : str 
    description : Optional[str] = None


class STask(STaskAdd):
    model_config = ConfigDict(from_attributes=True)
    id:int
   

class STaskId(BaseModel):
    ok:bool = True
    task_id : int 