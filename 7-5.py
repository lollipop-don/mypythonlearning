while True:
    age = input('what is your age?\n')
    if age == 'quit':
       break
    elif int(age) < 3:
      print('your ticket is free')
    elif int(age) < 12:
       print('your ticket is 10$')
    else:
       print('your ticket is 15$')

       