from pydantic import BaseModel


class TaskParams(BaseModel):
    param1: str = "default"
    param2: int = 0