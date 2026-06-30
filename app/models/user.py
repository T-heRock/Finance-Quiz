from __future__ import annotations

from sqlalchemy import Enum as SqlEnum
from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.enums import Platform
from app.db.entity import Entity


class User(Entity):
    __tablename__ = "users"
    __table_args__ = (
    UniqueConstraint(
        "platform",
        "platform_user_id",
        name="uq_platform_user",
    ),
)

    platform: Mapped[Platform] = mapped_column(
        SqlEnum(
            Platform,
            name="platform_enum",
            native_enum=False,
        ),
        nullable=False,
    )

    platform_user_id: Mapped[str] = mapped_column(
        String(100),
        index=True,
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )