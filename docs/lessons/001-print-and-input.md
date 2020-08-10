# Lesson 1: Print and Input

See if you can guess what this program will do:

```python
print('Hello!')
```

Type it into a python interpreter and check. We found putting it into a new file in Visual Studio Code, and then clicking the green "play" button, works well.

How about this program?

```python
print('Hello!')
input('What is your name? ')
```

What if you want to do something with the name the person types in? How about this:

```python
x = input('What is your name? ')
print('Hello ' + x + '!')
```

Notice how `+` "adds" the parts of the sentence together? Programmers call text like this "strings" for some reason.

What do you think the next program would do?

```python
q = 'What is your name? '
x = input(q)
print('Hello ' + x + '!')
```
