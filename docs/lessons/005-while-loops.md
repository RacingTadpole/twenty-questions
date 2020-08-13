# Lesson 5: While Loops

You can also write loops with `while`.

This gives you more flexibility, eg. you don't have to know how long the loop will go for
before you start.

The example below keeps asking you to type something until you type "stop".

```python
x = 'ok'
while x != 'stop':
    x = input('Type anything, or "stop" to stop: ')
    print('You typed: ' + x)
print('Finally!')
```

Note that `!=` means "does not equal", so the loop keeps going "while `x` does not equal 'stop'". As soon as it does, the computer leaves the indented section.

You could write the `for` loop from the last section using `while` like this:

```python
a = [1, 2, 3, 5, 8]
i = 0
while i < len(a):
    print(a[i])
```

Now you understand variables, "if"s and loops, we can get back to our game!
