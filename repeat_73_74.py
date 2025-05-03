# while True:
#     topping = input('please add a topping\n')
#     if topping == 'quit':
#        break
#     print(f'adding {topping}')


# topping = ''
# while topping != 'quit':
#     topping = input('please add a topping\n')
#     if topping != 'quit':
#       print(f'adding {topping}')


while True:
    age = input('please enter age\n')
    if age == 'quit':
      break
    age = int(age)

    if age < 3 :
      print('your ticket is free')
    elif age <= 12:
      print('your ticket is 10$')
    else:
      print('your ticket is 15$')       


