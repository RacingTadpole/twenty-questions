data = [
    {'number': 0, 'question': 'Does your animal fly?', 'yes': 1, 'no': 2},
    {'number': 1, 'question': 'Is your flying animal a bird?', 'yes': 3, 'no': 4},
    {'number': 2, 'question': 'Does your animal live underwater?', 'yes': 7, 'no': 8},
    {'number': 3, 'question': 'Is your bird native to Australia?', 'yes': 5, 'no': 6},
    {'number': 4, 'answer': 'fruit bat'},
    {'number': 5, 'answer': 'kookaburra'},
    {'number': 6, 'answer': 'blue jay'},
    {'number': 7, 'question': 'Is your animal a mammal?', 'yes': 9, 'no': 10},
    {'number': 8, 'answer': 'wombat'},
    {'number': 9, 'answer': 'blue whale'},
    {'number': 10, 'answer': 'goldfish'},
]

i = 0
while True:
    info = data[i]
    if 'question' in info:
        question = info['question']
        x = input(question + ' ')
        if x == 'y':
            i = info['yes']
        if x == 'n':
            i = info['no']
    else:
        answer = info['answer']
        x = input('Is it a ' + answer + '? ')
        if x == 'y':
            print('Wow, I guessed it!')
        if x == 'n':
            print('You beat me!')
        break
