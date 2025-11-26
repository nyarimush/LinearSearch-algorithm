#[Nyari Mushaikwa]
#{LinearSearch]

import random

items = [i for i in range(100)]

random.shuffle(items)

searchTerm = int(input('What is your search term?: '))
found = False
position = ''

for x in range (0, len(items)):

    if (searchTerm == items[x]):

        found = True
        position = x


if (found == True):
    
    print(f'Item found at position {position}')

else:
    print('Item not found')

