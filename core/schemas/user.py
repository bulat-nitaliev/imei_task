
from pydantic import BaseModel, EmailStr
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    tg_id:str


class UserCreate(schemas.BaseUserCreate):
    tg_id:str


class UserUpdate(schemas.BaseUserUpdate):
    tg_id:str


class BaseUser(BaseModel):
    tg_id: str
    id: int
    email: EmailStr
    is_active: bool
    is_superuser: bool
    is_verified: bool

class UserShema(BaseUser):...
