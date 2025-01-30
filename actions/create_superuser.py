import asyncio
import contextlib
from os import getenv

from core.models import db_helper, User
from api_v1.dependencies.users import get_users_db
from core.schemas.user import UserCreate
from api_v1.dependencies.user_manager import get_user_manager
from fastapi_users.exceptions import UserAlreadyExists
from core.authenticate.user_manager import UserManager

# get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


tg_id = getenv('email', '944444444')
email = getenv('email', 'admin@admin.com')
password = getenv('password', 'abc')
is_active = True
is_superuser = True
is_verified = True

async def create_user(
        user_manager:UserManager,
        user_create:UserCreate
):
    user = await user_manager.create(
        user_create=user_create,
        safe=False
    )
    return user


async def create_superuser(
        tg_id: str = tg_id,
        email:str = email,
        password:str = password,
        is_active:bool = is_active,
        is_superuser:bool = is_superuser,
        is_verified:bool = is_verified,
):
    user_create = UserCreate(
        tg_id = tg_id,
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified
    )
    async with db_helper.session_factory() as session:
        async with get_user_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                await create_user(
                    user_manager=user_manager,
                    user_create=user_create
                )






# if __name__ == '__main__':
#     asyncio.run(create_superuser())
