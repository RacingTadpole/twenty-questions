# Lesson 4: For loops

What do you think this will do?

```python
for x in [1, 2, 3, 5, 8]:
    print(x)
```

It loops through the list and prints each element.

You can do stuff to the element too:

```python
for x in [1, 2, 3, 5, 8]:
    print(x * 2 + 3)
```

And you can put the list in a variable too:

```python
a = [1, 2, 3, 5, 8]
for x in a:
    print(x)
```

We've been using single letters for variables but you can use words.
You just can't put spaces in the words, but we can use "_".

```python
numbers = [1, 2, 3, 5, 8]
for x in numbers:
    print(x)
```

or even

```python
my_numbers = [1, 2, 3, 5, 8]
for number in my_numbers:
    print(number)
```

How would you write a loop to show the squares of the numbers above?

## A little trick

One nice thing about Python is this little trick - you can bring the `for`
"inside" the list like this:

```python
a = [1, 2, 3, 5, 8]
b = [x * 2 for x in a]
print(b)
```
