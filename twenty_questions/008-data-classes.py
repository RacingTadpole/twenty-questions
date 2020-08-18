from dataclasses import dataclass
from typing import Union

@dataclass
class Answer:
    text: str

@dataclass
class Question:
    text: str
    yes: Union['Question', Answer]
    no: Union['Question', Answer]

q = Question(
    'Does your animal fly?',
    yes=Question(
        'Is your flying animal a bird?',
        yes=Question(
            'Is your bird native to Australia?',
            yes=Answer('kookaburra'),
            no=Answer('blue jay'),
        ),
        no=Answer('fruit bat'),
    ),
    no=Question(
        'Does your animal live underwater?',
        yes=Question('Is your animal a mammal?',
            yes=Answer('blue whale'),
            no=Answer('gold fish'),
        ),
        no=Answer('wombat'),
    )
)

current = q
while isinstance(current, Question):
    x = input(current.text + ' ')
    if x == 'y':
        current = current.yes
    if x == 'n':
        current = current.no

x = input('Is it a ' + current.text + '? ')
if x == 'y':
    print('Wow, I guessed it!')
if x == 'n':
    print('You beat me!')
