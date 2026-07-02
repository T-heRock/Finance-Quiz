from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.entity import Entity

if TYPE_CHECKING:
    from app.models.category import Category

if TYPE_CHECKING:
    from app.models.question import Question


class Topic(Entity):

    __tablename__ = "topics"

    __table_args__ = (
        UniqueConstraint(
            "category_id",
            "name",
            name="uq_category_topic",
        ),
    )
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

    category: Mapped[Category] = relationship(
        "Category",
        back_populates="topics",
    )

    parent: Mapped[Topic | None] = relationship(
        "Topic",
        remote_side="Topic.id",
        back_populates="children",
    )

    children: Mapped[list[Topic]] = relationship(
        "Topic",
        back_populates="parent",
    )

    questions: Mapped[list[Question]] = relationship(
    "Question",
    back_populates="topic",
)
    
is_verified: Mapped[bool] = mapped_column(
    Boolean,
    nullable=False,
    default=True,
)