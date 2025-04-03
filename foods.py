my_foods = ['pizza','fallafel','carrot cake']



# print(f'my_foods created on address: {id(my_foods)}.')

# first_two_foods = my_foods[:2]
# print(f'first_two_foods is created on address: {id(first_two_foods)}.')

friend_foods = my_foods
print(f'address of my_foods is {id(my_foods)} and address of friend_foods is {id(friend_foods)}')
# print(list_copy)
print(my_foods)
print(friend_foods)
my_foods.append('lobio')
friend_foods.append('potato')
print(my_foods)
print(friend_foods)
# print(first_two_foods)

















