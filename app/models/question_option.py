from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.entity import Entity

if TYPE_CHECKING:
    from app.models.question import Question


class QuestionOption(Entity):
    __tablename__ = "question_options"

    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id"),
        nullable=False,
        index=True,
    )

    option_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    option_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    is_correct: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    question: Mapped[Question] = relationship(
        "Question",
        back_populates="options",
    )