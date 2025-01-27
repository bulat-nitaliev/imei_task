from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func
from datetime import datetime

class WhiteList(Base):
    name: Mapped[str] = mapped_column(index=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.now, server_default=func.now())


       