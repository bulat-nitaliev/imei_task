from fastapi import APIRouter
from core.config import settings
from .fastapi_users import fastapi_users
from core.schemas.user import UserUpdate, UserRead

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