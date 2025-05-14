def greet_user(username):
    print(f'hello {username}')





greet_user('tiko')
greet_user('gigi')
greet_user('kate')

# number = input('enter number')
# number = int(number)

def is_prime(number):
    is_number_prime = True
    for value in range(2,number):
        if number % value == 0:
            is_number_prime = False
            break
        
    if is_number_prime == True:
        print(f'the {number} is prime')
    else:
        print(f'the {number} is not prime')


for value in range(2, 101):
    is_prime(value)
