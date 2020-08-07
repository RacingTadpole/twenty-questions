from twenty_questions.question import Question, Answer

print('Welcome to Twenty Questions')
print('Please think of an animal or plant, and I will try to guess what it is by asking questions.')
print('Please answer questions with "y" or "n"')
print()

cactus = Answer(text='cactus')
sea_cucumber = Answer(text='sea cucumber')
wombat = Answer('wombat')

question2 = Question(text='Does it live underwater?', yes=sea_cucumber, no=wombat)
question1 = Question(text='Is it an animal?', yes=question2, no=cactus)

next = question1

while isinstance(next, Question):
    yes_or_no = input(next.text + ' ')
    if yes_or_no == 'y':
        next = next.yes
    elif yes_or_no == 'n':
        next = next.no
    else:
        print('Please only respond y or n.')

print('It is a ' + next.text + '!')
