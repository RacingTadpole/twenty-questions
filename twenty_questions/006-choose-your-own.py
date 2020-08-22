data = [
    [0, 'Does your animal fly?', 1, 2],
    [1, 'Is your flying animal a bird?', 3, 4],
    [2, 'Does your animal live underwater?', 7, 8],
    [3, 'Is your bird native to Australia?', 5, 6],
    [4, 'Is it a fruit bat?'],
    [5, 'Is it a kookaburra?'],
    [6, 'Is it a blue jay?'],
    [7, 'Is your animal a mammal?', 9, 10],
    [8, 'Is it a wombat?'],
    [9, 'Is it a blue whale?'],
    [10, 'Is it a goldfish?'],
]

i = 0
while True:
    question = data[i][1]
    x = input(question + ' ')
    if len(data[i]) == 2:
        break
    if x == 'y':
        i = data[i][2]
    if x == 'n':
        i = data[i][3]
print('Thanks for playing')
