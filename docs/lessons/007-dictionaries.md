# Lesson 7: Dictionaries

That worked but lines like this are hard to read, don't you think?

```python
    question = info[1]
    yes_number = info[2]
    no_number = info[3]
```

Wouldn't something like this be nicer and less error-prone?

```python
    question = info['question']
    yes_number = info['yes']
    no_number = info['no']
```

Python lets us do this. Instead of putting our question info into a list like this:

```python
    [0, 'Does your animal fly?', 1, 2]
```

you can name each part like this:

```python
    {'number': 0, 'question': 'Does your animal fly?', 'yes': 1, 'no': 2}
```

This is called a dictionary. It uses `{}` instead of `[]`. 

You can think of it as a bunch of "keys" (like `question`)
and "values" (like `'Does your animal fly?`).

While we're at it, why don't we change the way we write the answers too?

```python
    {'number': 4, 'answer': 'fruit bat'},
```

Try rewriting your code from the last lesson to use this structure.

If you want to test if a particular key is in the dictionary, you can use `in`, eg.

```python
info = {'number': 4, 'answer': 'fruit bat'}
print('question' in info)  # False
print('answer' in info)  # True
```

Here's the same list we had before, in the new format:

```python
data = [
    {'number': 0, 'question': 'Does your animal fly?', 'yes': 1, 'no': 2},
    {'number': 1, 'question': 'Is your flying animal a bird?', 'yes': 3, 'no': 4},
    {'number': 2, 'question': 'Does your animal live underwater?', 'yes': 7, 'no': 8},
    {'number': 3, 'question': 'Is your bird native to Australia?', 'yes': 5, 'no': 6},
    {'number': 4, 'answer': 'fruit bat'},
    {'number': 5, 'answer': 'kookaburra'},
    {'number': 6, 'answer': 'blue jay'},
    {'number': 7, 'question': 'Is your animal a mammal?', 'yes': 9, 'no': 10},
    {'number': 8, 'answer': 'wombat'},
    {'number': 9, 'answer': 'blue whale'},
    {'number': 10, 'answer': 'goldfish'},
]
```

Here's one way you could do it:

```python
i = 0
while True:
    info = data[i]
    if 'question' in info:
        question = info['question']
        x = input(question + ' ')
        if x == 'y':
            i = info['yes']
        if x == 'n':
            i = info['no']
    else:
        answer = info['answer']
        x = input('Is it a ' + answer + '? ')
        if x == 'y':
            print('Wow, I guessed it!')
        if x == 'n':
            print('You beat me!')
        break
```