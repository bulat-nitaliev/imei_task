from fastapi import APIRouter, Depends
from core.config import settings
from .fastapi_users import fastapi_users
from core.schemas.user import UserUpdate, UserRead


from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from api_v1.fastapi_users import current_user
from typing import Annotated


router = APIRouter(
    prefix=settings.users,
    tags=["Users",]
)


router.include_router(
    fastapi_users.get_users_router(
        UserRead, 
        UserUpdate
        ),
        
)


