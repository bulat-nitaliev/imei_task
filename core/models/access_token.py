
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy.ext.asyncio import AsyncSession
from .base import Base
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):  
    user_id:Mapped[int] = mapped_column(
                Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False
            )
    
    @classmethod
    def get_db(cls,session: "AsyncSession") :
        return SQLAlchemyAccessTokenDatabase(session, cls)