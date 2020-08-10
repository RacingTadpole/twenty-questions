print('Welcome to Guess the Animal')
print('Please think of an animal, and I will try to guess what it is by asking questions.')
print('Please answer questions with "y" or "n"')
print()

x=input('Does your animal fly? ')
print('You said '+x)
if x=='y':
    xa=input ('Is your flying animal a bird? ')
    if xa=='y':
        input ('Does your bird eat other birds? ')
    if xa=='n':
        print('Your animal is a bat.')
if  x=='n':
    input ('Does your animal live under water? ')
