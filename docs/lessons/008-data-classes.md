# Lesson 8: Data classes

## First pass

Dictionaries are great, but it's still easy to make errors with them,
eg. what if you accidentally mistyped a key like this:

```python
    {'number': 0, 'question': 'Does your animal fly?', 'yes': 1, 'no': 2},
    {'number': 1, 'qustion': 'Is your flying animal a bird?', 'yes': 3, 'no': 4},
```

You wouldn't know until the user hits that question, and then it would go wrong.

Data classes are a solution to this. We'll define one for questions and another one for answers. Here's how:

```python
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
```

You can write this too, which makes things clearer:

```python
    Question(number=0, text='Does your animal fly?', yes_number=1, no_number=2),
```

To use data classes, do stuff like this:

```python
q = Question(0, 'Does your animal fly?', 1, 2)
print(q.number)
print(q.text)
print(q)
print(isinstance(q, Question))
```

## Second pass

Why are we using numbers to refer to questions and answers?
Let's just point to them directly, and write our questions out in a tree, like this:

```python
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
```

The loop is very straightforward now:

```python
    current = q
    while isinstance(current, Question):
        x = input(current.text + ' ')
        if x == 'y':
            current = current.yes
        if x == 'n':
            current = current.no

    x = input('Is it a ' + answer + '? ')
    if x == 'y':
        print('Wow, I guessed it!')
    if x == 'n':
        print('You beat me!')
```

Do you think this is an improvement?
