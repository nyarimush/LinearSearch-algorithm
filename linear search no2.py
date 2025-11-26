import random

items = [random.randint(0, 100) for i in range(100)]
print(items)


searchTerm = int(input('What is your search term?: '))
found = False
position = []

for x in range (0, len(items)):

    if (searchTerm == items[x]):

        found = True
        position.append(x)


if (found == True):
    
    print(f'Item found at position {position}')

else:
    print('Item not found')


