from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func
from datetime import datetime
from .mixins.int_pk import IdIntPkMixins

class WhiteList(Base, IdIntPkMixins):
    name: Mapped[str]
    tg_id:Mapped[str] = mapped_column(index=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.now, server_default=func.now())


       