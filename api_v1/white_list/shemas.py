from pydantic import BaseModel,ConfigDict
from datetime import datetime


class WhiteListBase(BaseModel):
    name: str
    tg_id:str
    created_at: datetime


class CreateWhiteList(WhiteListBase):...

class WhiteList(WhiteListBase):
    model_config = ConfigDict(from_attributes=True)
    id: int