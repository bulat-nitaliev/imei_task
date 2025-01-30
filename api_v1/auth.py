from fastapi import APIRouter
from core.config import settings
from .fastapi_users import fastapi_users
from .dependencies.backend import auth_backend
from core.schemas.user import UserCreate, UserRead

router = APIRouter(
    prefix=settings.v1,
    tags=["Auth",]
)

#/login
#/logout
router.include_router(
    router=fastapi_users.get_auth_router(auth_backend)
)


router.include_router(
    fastapi_users.get_register_router(
        UserRead, 
        UserCreate
        ),
 
)

#/request-verify-token 
#/verify

router.include_router(
    router=fastapi_users.get_verify_router(UserRead)
)

#/forgot-password
#/reset-password

router.include_router(
    router=fastapi_users.get_reset_password_router()
)