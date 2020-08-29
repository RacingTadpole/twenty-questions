# Lesson 9: Learning new animals

We're ready for the fun part - teaching the computer new animals!

The idea is, if the computer guesses wrong, then it should ask what animal you were thinking of,
and a question that could use to distinguish it from the wrong guess.

So let's add some extra inputs from the user to the end of the game, by changing

```python
z = input('Is it a ' + current.text + '? ')
if z == 'y':
    print('Wow, I guessed it!')
if z == 'n':
    print('You beat me!')
```

to

```python
z = input('Is it a ' + current.text + '? ')
if z == 'y':
    print('Wow, I guessed it!')
if z == 'n':
    print('You beat me!')
    new_animal = input('So what was your animal? ')
    new_answer = Answer(new_animal)
    new_question_text = input('What is a question (with answer yes for your animal) that distinguishes a ' + new_animal + ' from a ' + current.name + '? ')
    new_question = Question(text=new_question_text, yes=new_answer, no=current)
```

Now we have the pieces we need, we just have to store `new_question` in the tree of questions in the right spot.

Unfortunately we don't keep track of where that is - all we have is `current` which is the wrong answer.
We need to remember the question that went before, so we can add the new question after it.

That's easy - just add:

```python
    previous = current
```

before the `if x == 'y':` in the loop.

Then you can hook the new question into the right spot at the end, with: 
```python
    if x == 'y':
        previous.yes = new_question
    if x == 'n':
        previous.no = new_question
```

Done!... expect that the game then ends and the new question is lost forever.

For now you can solve that by putting the entire game inside another `while True:` loop,
so when the game ends, you start another one using the new tree of questions.

But it would be better to save the new questions and answers to a file, right?

Let's do that next.
