# Lesson 5: While Loops

You can also write loops with `while`.

The example below keeps asking you to type something until you type "stop".

Note that `!=` means "does not equal", so the loop keeps going "while `x` does not equal 'stop'". As soon as it does, the computer leaves the indented section.

```python
x = 'ok'
while x != 'stop':
    x = input('Type anything, or "stop" to stop: ')
    print('You typed: ' + x)
print('Finally!')
```

The example below keeps asking for a number until you give it one above 10.

```python
x = 0
while x < 11:
    y = input('Give me a number: ')
    x = int(y)
print('Finally, a number above 10!')
```

Notice how we use `int` here to convert a "string" input to a whole number.

Now you understand variables, "if"s and loops, you basically understand programming!
