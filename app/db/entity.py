from __future__ import annotations

import datetime

from sqlalchemy import DateTime, Integer, func
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from app.db.base import Base


class Entity(Base):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    created_at: Mapped[datetime] = mapped_column( # type: ignore
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column( # type: ignore
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )