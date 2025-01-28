

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    tg_id:str


class UserCreate(schemas.BaseUserCreate):
    tg_id:str


class UserUpdate(schemas.BaseUserUpdate):
    tg_id:str