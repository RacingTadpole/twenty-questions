from dataclasses import dataclass
from typing import Union

@dataclass
class Answer:
    name: str

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

while True:
    current = q
    while isinstance(current, Question):
        x = input(current.text + ' ')
        previous = current
        if x == 'y':
            current = current.yes
        if x == 'n':
            current = current.no

    z = input('Is it a ' + current.name + '? ')
    if z == 'y':
        print('Wow, I guessed it!')
    if z == 'n':
        print('You beat me! 😡')
        new_animal = input('So what was your animal? ')
        new_answer = Answer(new_animal)
        new_question_text = input('What is a question (with answer yes for your animal) that distinguishes a ' + new_animal + ' from a ' + current.name + '? ')
        new_question = Question(text=new_question_text, yes=new_answer, no=current)
        if x == 'y':
            previous.yes = new_question
        if x == 'n':
            previous.no = new_question
    print()
    print("Let's play again!")
    print()
