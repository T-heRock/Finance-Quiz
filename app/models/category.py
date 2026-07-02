from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.entity import Entity

if TYPE_CHECKING:
    from app.models.topic import Topic

class Category(Entity):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    topics: Mapped[list[Topic]] = relationship(
        "Topic",
        back_populates="category",
)