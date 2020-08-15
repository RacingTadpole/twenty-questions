# Lesson 6: Game Loop Ideas

At the end of lesson 2 we had a version of our game already, with lots of `if`s -
but it was hard to add new animals to it.

## Idea 1: For
So, we want to put it in a loop somehow. Let's start with a `for` loop - what would this do?

```python
questions = [
    'Is it blue?',
    'Is it bigger than a football?',
    'Is it a mammal?',
    'Does it fly?',
]
for question in questions:
    x = input(question + ' ')
print('Thanks for playing.')
```

It asks all the questions ok, but it asks them _all_ and ignores the answers.

## Idea 2: While

This looks like a job for a `while` loop.

With the same `questions` as above, let's try:

```python
i = 0
while i < len(questions):
    x = input(questions[i] + ' ')
    if x == 'n':
        i = i + 1
    if x == 'y':
        i = i + 2
```

Now the questions depend on the answers - but not in a very sensible way.

## Idea 3: Choose your own adventure

What we need is, for each question, a way to say which question comes next when you answer no,
and which question comes next when you answer yes.

Here's an idea: for each question, replace it with the question, its number, and the question
numbers to go to when you answer yes and no.

You can think of the question numbers like the page numbers in a "Choose your own Adventure" book.

```python
data = [
    [0, 'Does your animal fly?', 1, 2],
    [1, 'Is your flying animal a bird?', 3, 4],
    [2, 'Does your animal live underwater?', 7, 8],
    [3, 'Is your bird native to Australia?', 5, 6],
    [4, 'Is it a fruit bat?'],
    [5, 'Is it a kookaburra?'],
    [6, 'Is it a blue jay?'],
    [7, 'Is your animal a mammal?', 9, 10],
    [8, 'Is it a wombat?'],
    [9, 'Is it a blue whale?'],
    [10, 'Is it a goldfish?'],
]
```

See if you can trace through in your mind how the questions and answers are linked.

Notice what we did when there are no more questions to ask - we just left off the last two numbers.

If you say yes, the animal does fly (question number 0),
then you are asked if it's a bird (question number 1); if you say no to that,
you are asked "is it a fruit bat?" (number 4) - and there are no more questions after that.

The first column is really just there to help us humans.

How can we write a loop for this? Try and write one yourself. You might want to start
by choosing a variable name for the "current" question number. And we don't really know
what should stop the "while" loop yet, so you could write it for now as `while True:`,
which will go forever (or until there's an error).

Here's a first pass, that doesn't fully work yet.

```python
i = 0
while True:
    question = data[i][1]
    yes_number = data[i][2]
    no_number = data[i][3]
    x = input(question)
    if x == 'y':
        i = yes_number
    if x == 'n':
        i = no_number
```

That almost works, but it fails when there are no page numbers to go to (which happens when it
gets to the end).

Here's one way you could fix that.

```python
i = 0
while i >= 0:
    info = data[i]
    question = info[1]
    x = input(question + ' ')
    if len(info) == 2:
        # There are no more questions
        if x == 'y':
            print('Wow, I guessed it!')
        if x == 'n':
            print('You beat me!')
        i = -1
    else:
        # Go to the next question
        if x == 'y':
            i = info[2]
        if x == 'n':
            i = info[3]
```

Notice when we got to an answer, we set `i = -1` - so our while loop should continue only
when `i >= 0`. You might be able to come up with other ways to do this.

It's a little fiddly to write the questions now, but it works!
