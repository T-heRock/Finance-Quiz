from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.entity import Entity


class Topic(Entity):
    __tablename__ = "topics"

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
        index=True,
    )

    parent_topic_id: Mapped[int | None] = mapped_column(
        ForeignKey("topics.id"),
        nullable=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    category = relationship(
        "Category",
        back_populates="topics",
    )

    parent = relationship(
        "Topic",
        remote_side="Topic.id",
        back_populates="children",
    )

    children = relationship(
        "Topic",
        back_populates="parent",
    )