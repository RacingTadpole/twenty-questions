from dataclasses import dataclass
from typing import Union
from dataclasses_serialization.json import JSONSerializer
import json


@dataclass
class Answer:
    name: str

@dataclass
class Question:
    text: str
    yes: Union['Question', Answer]
    no: Union['Question', Answer]

try:
    with open('game.json') as file:
        questions_as_dict = json.load(file)
    q = JSONSerializer.deserialize(Question, questions_as_dict)
except FileNotFoundError:
    q = Answer('wombat')

print()
print()
print('Welcome to Twenty Questions')
print('Please think of an animal or plant, and I will try to guess what it is by asking questions.')
print('Please answer questions with "y" or "n"')
print()

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
    print('Well that was easy! 🥱')
if z == 'n':
    print('You beat me! 😡')
    new_animal=input ('So what was your animal? ')
    new_answer = Answer(new_animal)
    new_question_text=input('What is a question (with answer yes for your animal) that distinguishes a ' + new_animal + ' from a ' + current.name + '? ')
    new_question = Question(text=new_question_text, yes=new_answer, no=current)
    if x == 'y':
        previous.yes = new_question
    if x == 'n':
        previous.no = new_question

    serialized_questions = JSONSerializer.serialize(q)

    with open('game.json', 'w') as file:
        json.dump(serialized_questions, file, indent=2)

    print()
    print('Thank you! Please play again 😃')