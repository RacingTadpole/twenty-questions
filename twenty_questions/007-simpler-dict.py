ages = {'Jack': 13, 'Olivia': 15, 'Robert': 48, 'Jess': 47}

print ('Jack is', ages['Jack'])
print()

for name in ages:
    print(name, 'is', ages[name])

print()
name = input('Enter a name: ')
print(name, 'is', ages[name])
