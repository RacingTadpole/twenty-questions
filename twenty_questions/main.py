from twenty_questions.question import Question

print('Welcome to Twenty Questions')
print('Please think of an animal or plant, and I will try to guess what it is by asking questions.')
print('Please answer questions with "y" or "n"')
print()

question2 = Question(text='Does it live underwater?', yes_answer='sea cucumber', no_answer='wombat')
question1 = Question(text='Is it an animal?', yes_question=question2, no_answer='cactus')

question = question1
guess = None

while question:
    yes_or_no = input(question.text + ' ')

    if yes_or_no == 'y':
        guess = question.yes_answer
        question = question.yes_question
    elif yes_or_no == 'n':
        guess = question.no_answer
        question = question.no_question
    else:
        print('Please only respond y or n.')

print('It is a ' + guess + '!')
