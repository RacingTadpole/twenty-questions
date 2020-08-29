# Lesson 10: Saving stuff

Saving text files is easy in python - if you want to put "goodbye" into a new file called "hello.txt",
you can just do:

```python
with open('hello.txt', 'w') as file:
    file.write('goodbye')
```

and then to read it in again:

```python
with open('hello.txt', 'r') as file:
    x = file.read()
print(x)
```

The `'w'` is for "write", and `'r'` is for "read".

(If you're wondering about the `with`...`as`, putting it in an indented block like this means the computer
knows when you're done with the file and it can be closed safely. It also means if there's an error
and the program never finishes properly, the computer still knows to close the file properly.)

So the harder question is, what format do we want to write our questions out in?

Luckily, there is a standard answer: "json".

## json

"Json" is basically just the dictionary format you're already used to, and python makes it easy to write
out dictionaries in this format. Eg.

```python
import json

d = {'name': 'Bert', 'mother': 'Amanda', 'father': 'Henry', 'children': 3}
with open('my.json', 'w') as file:
    json.dump(d, file)
```

creates a file `my.json` containing:
```json
{"name": "Bert", "mother": "Amanda", "father": "Henry", "children": 3}
```

The only difference is that "json" format always uses double-quotes,
whereas python can use either single or double quotes.

You can read a `json` file in with `json.load`:

```python
with open('my.json', 'r') as file:
    d = json.load(file)
print(d['mother'])
```

## json from dataclasses

As we saw above, python has a built-in way to turn dictionaries into json files and vice versa.

There's an open-source package online that makes this work for data classes too - it converts dictionaries
to dataclasses and vice versa.

So by stringing the two together, you can convert between data classes into json files.

```python
from dataclasses_serialization.json import JSONSerializer

# To read a json file and turn it into a Question dataclass
with open('game.json') as file:
    d = json.load(file)
q = JSONSerializer.deserialize(Question, d)

# To write dataclass out as a json file
d = JSONSerializer.serialize(q)
with open('game.json', 'w') as file:
    json.dump(d, file, indent=2)
```

The `indent=2` just makes big files easier to read by indenting nested dictionaries by 2 spaces.

(The name "serialize" is programmer-speak for converting a data into a linear, 1-dimensional form
so it can be saved in a file, or sent over the web. "Deserialize" is the reverse.)

## Error handling

Your game will be much more fun when you read the questions in like this at the start of the game,
and save them at the end.

But the very first time you run this code, `game.json` won't exist yet!
In fact the file-reading code above will give you this error:

```
FileNotFoundError: [Errno 2] No such file or directory: 'game.json'
```

Python provides a way to "catch" these errors and handle them better.

In our case, we could start of with a default answer, like this:

```python
try:
    with open('game.json') as file:
        d = json.load(file)
    q = JSONSerializer.deserialize(Question, d)
except FileNotFoundError:
    q = Answer('wombat')
```