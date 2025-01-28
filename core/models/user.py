
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from core.models import Base
from sqlalchemy.orm import mapped_column, Mapped
from typing import TYPE_CHECKING
from .mixins.int_pk import IdIntPkMixins

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base,IdIntPkMixins, SQLAlchemyBaseUserTable[int]):
    tg_id: Mapped[str] = mapped_column(unique=True)

    @classmethod
    def get_user_db(cls,session: "AsyncSession") :
        return SQLAlchemyUserDatabase(session, cls)