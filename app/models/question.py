from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import Difficulty, QuestionType
from app.db.entity import Entity
from app.models.question_option import QuestionOption

if TYPE_CHECKING:
    from app.models.topic import Topic


class Question(Entity):
    __tablename__ = "questions"

    topic_id: Mapped[int] = mapped_column(
        ForeignKey("topics.id"),
        nullable=False,
        index=True,
    )

    question_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    question_type: Mapped[QuestionType] = mapped_column(
        SqlEnum(
            QuestionType,
            name="question_type_enum",
            native_enum=False,
        ),
        nullable=False,
        default=QuestionType.MCQ_SINGLE,
    )

    difficulty: Mapped[Difficulty] = mapped_column(
        SqlEnum(
            Difficulty,
            name="difficulty_enum",
            native_enum=False,
        ),
        nullable=False,
        default=Difficulty.MEDIUM,
    )

    explanation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    source: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    topic: Mapped[Topic] = relationship(
        "Topic",
        back_populates="questions",
    )

    options: Mapped[list[QuestionOption]] = relationship(
    "QuestionOption",
    back_populates="question",
    cascade="all, delete-orphan",
    order_by="QuestionOption.option_order",
    )