# Lesson 3: More about Variables

Let's learn one more thing before we get to loops.

Remember we had

```python
q = 'What is your name? '
x = input(q)
print('Hello ' + x + '!')
```

Programmers call `q` and `x` "variables", because they can vary.

## String variables
These particular variables are "strings" - they contain text.
(Remember programmers call text "strings" for some reason.)

Variables can be other types of things too.

## Numeric variables
In order to do maths, you might expect numbers, and these are called "integers" (for whole numbers) or "floats" (for decimal numbers - the word "float" was picked originally because the computer stores them in a way that lets the decimal place "float" a long way to the left or right).

```python
n = 10
print(n)
print(n + 5)
print(n / 2)
print(n * 3)

k = n * 3 + 1
print(k)

x = k / 10
print(x)
```

Etc.

You can ask if a variable is a string (`str`), an integer (`int`) or a float (`float`) using `isinstance` like this:

```python
n = 10
print(isinstance(n, int))
print(isinstance(n, str))
```

which returns `True` or `False`.
In fact these responses are another type of variable, which can only be
True or False. Such variables are named "boolean" (`bool`) after George Boole, an 1800s mathematician, for some reason, although the idea of true and false must be older than that.

## True/False variables

```python
a = True
print(a)

x = 'yes'
print(x == 'yes')
```

Notice the double equals sign gives us a True or False too.
If you think about it, that makes sense for using with "if", right?
If something is true, do something; if it's false, do something else.

## Lists

Let's talk about one more, fancier type of variable - a list, eg.

```python
x = [1, 3, 4, 7, 'hello']
print(x)

print(isinstance(x, list))
```

This will be handy in our next lesson, on loops.
