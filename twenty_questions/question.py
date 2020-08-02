from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Question:
    text: str
    yes_question: Optional['Question'] = None
    yes_answer: Optional[str] = None
    no_question: Optional['Question'] = None
    no_answer: Optional[str] = None
