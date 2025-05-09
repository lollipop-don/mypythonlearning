while True:

    number = input('please enter a number\n')
    if number == 'quit':
       break
    number = int(number)

    for value in range(2,number):
        if number % value == 0:
           print(f'{number} is not prime')
           break

