from dataclasses import dataclass

@dataclass
class Question:
    number: int
    text: str
    yes_number: int
    no_number: int

@dataclass
class Answer:
    number: int
    text: str

data = [
    Question(0, 'Does your animal fly?', 1, 2),
    Question(1, 'Is your flying animal a bird?', 3, 4),
    Question(2, 'Does your animal live underwater?', 7, 8),
    Question(3, 'Is your bird native to Australia?', 5, 6),
    Answer(4, 'fruit bat'),
    Answer(5, 'kookaburra'),
    Answer(6, 'blue jay'),
    Question(7, 'Is your animal a mammal?', 9, 10),
    Answer(8, 'wombat'),
    Answer(9, 'blue whale'),
    Answer(10, 'goldfish'),
]