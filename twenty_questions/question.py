from dataclasses import dataclass
from typing import Optional, Union

@dataclass(frozen=True)
class Answer:
    text: str

@dataclass(frozen=True)
class Question:
    text: str
    yes: Union['Question', Answer]
    no: Union['Question', Answer]
