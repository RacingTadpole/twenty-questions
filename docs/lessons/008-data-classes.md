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

## Drop the numbers

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

first = Question(
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

Note our "data" list has disappeared, and now we just have a question which contains
all the other questions and answers.

The loop is very straightforward now:

```python
    current = first
    while isinstance(current, Question):
        x = input(current.text + ' ')
        if x == 'y':
            current = current.yes
        if x == 'n':
            current = current.no

    z = input('Is it a ' + current.text + '? ')
    if z == 'y':
        print('Wow, I guessed it!')
    if z == 'n':
        print('You beat me!')
```

Do you think this is an improvement?

## Help!

There are quite a few new things in there
(like the `import`s and the `@dataclass` thing, not to mention `class`) which you might
prefer to understand before you use them. Here's a quick intro to each, which can also ignore.

### import

One nice thing about python is there are a few basic built-in commands (like `print`, `input`, `if` etc),
and _everything else_ you need to "import" to use. I think that's nice because it means if you come
across a command you've never seen before, you can go to the top of the file and see where it was
imported from, and so where it comes from. And then you can search for it.

Some packages (like the ones here, `dataclasses` and `typing`) are built-in to python.
But you can write your own and other people can import your code to use too.

We'll get into that more later.

### class and "@dataclass"

Python's built-in `class`es give you lots of flexibility to define "objects" that make sense for your program.

But there's a trend among programmers these days to restrict these objects to just the bare essentials,
which is what the `@dataclass` line does. It means the object only has the properties you list on it,
and they behave in the obvious way. In fact `@dataclass(frozen=true)` is even better, it means
you cannot change the object once you've created it (it's "frozen") - and that makes it easier to write
code that works.

## Or - drop the numbers but keep the dictionaries

If the `Question` and `Answer` classes seem confusing, don't worry. It's perfectly fine to stick with
dictionaries. You can drop the numbers with them just the same way, and "nest" dictionaries, like this:

```python
first = {
    'text': 'Does your animal fly?',
    'yes': {
        'text': 'Is your flying animal a bird?',
        'yes': {
            'text': 'Is your bird native to Australia?',
            'yes': 'kookaburra',
            'no': 'blue jay',
        },
        'no': 'fruit bat',
    },
    'no': {
        'text': 'Does your animal live underwater?',
        'yes': {
            'text': 'Is your animal a mammal?',
            'yes': 'blue whale',
            'no': 'gold fish',
        },
        'no': 'wombat',
    }
}
```

Here I've chosen to write the questions as dictionaries (with `text`, `yes` and `no` fields),
and the answers just as strings.

The loop could be:

```python
    current = first
    while isinstance(current, dict):
        x = input(current['text'] + ' ')
        if x == 'y':
            current = current['yes']
        if x == 'n':
            current = current['no']

    x = input('Is it a ' + current + '? ')
    if x == 'y':
        print('Wow, I guessed it!')
    if x == 'n':
        print('You beat me!')
```

## Is it a good idea to nest the questions?

Nesting the questions in a big "tree" like this is quite neat, and it reflects the way the game works.

There are some downsides to doing it though, which we'll hit soon.
