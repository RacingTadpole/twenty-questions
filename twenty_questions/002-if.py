print('Welcome to Guess the Animal')
print('Please think of an animal, and I will try to guess what it is by asking questions.')
print('Please answer questions with "y" or "n"')
print()

x = input('Does your animal fly? ')
if x == 'yes':
    xy = input('Is your flying animal a bird? ')
    if xy == 'yes':
        print('I think your animal is a pelican.')
    if xy == 'no':
        print('I think your animal is a fruit bat.')
if x == 'no':
    print('I think your animal is a wombat.')
