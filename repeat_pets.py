pets = ['dog','cat','snake','cat','monkey','tiger','cat']
while 'cat' in pets:
    pets.remove('cat')
for value in pets:
    print(value)
print('now remove each element until pets list is empty')
while pets:
    popped_element = pets.pop()
    print(f'popped : {popped_element}')
print(f'after removing all elements now there are {len(pets)} elemnts in pets')