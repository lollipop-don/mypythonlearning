from toppings_data import toppings

from toppings_data import available_toppings
from toppings_data import requested_toppings

# for value in toppings:
#     if value == 'mushrooms':
#         print(f'sorry we have no {value}')
#     else:    
#         print(f'adding {value}')

print(type(toppings))
print(len(toppings))
print(f'before clearing the list has {len(toppings)} elements')
toppings.clear()
print(f'after clearing now the list has {len(toppings)} elements ')



#Check if list is empty
#3 ways
# if toppings == []:
#     print('empty')
# else:
#     print('not empty')    

# if len(toppings) == 0:
#     print('empty')
# else:
#     print('not empty')    


# if toppings:
#     print('not empty')
# else:
#     print('empty')  


for value in requested_toppings:
    if value in available_toppings:
        print(f'{value} availeble') 
    else:
        print(f'sorry {value}') 



























