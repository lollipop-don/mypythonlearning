# my_foods = ['lobio','potato','tomato']
# print(f'my foods is {my_foods} and its address is {id(my_foods)}.')
# mari_foods = my_foods
# print(f'mari foods is {mari_foods} and its address is {id(mari_foods)}.') 
# my_foods.append('kalbasi')
# print(f'now my foods is {my_foods} and maris foods is {mari_foods}.')


my_foods = ['lobio','potato','tomato']
print(f'my foods is {my_foods} and its address is {id(my_foods)}.')
mari_foods = my_foods[:]
print(f'mari foods is {mari_foods} and its address is {id(mari_foods)}.') 
my_foods.append('kalbasi')
print(f'now my foods is {my_foods} and maris foods is {mari_foods}.')


