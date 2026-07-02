from enum import Enum, StrEnum


class Platform(StrEnum):
    TELEGRAM = "telegram"
    WEBSITE = "website"

class Difficulty(str, Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class QuestionType(str, Enum):
    MCQ_SINGLE = "MCQ_SINGLE"