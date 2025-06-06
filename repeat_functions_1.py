from my_functions import *

res = is_prime(7)
print(f'7 is prime {res}')


res = is_prime(17)
print(f'17 is prime {res}')


res = is_prime(25)
print(f'25 is prime {res}')


for value in range(2,50):
    if is_prime(value) == True:
        print(f'{value} is prime')


# from my_functions import sum_all_numbers
lst = [2, 5, 8, 65]
res = sum_all_numbers(lst)
print(res)


# from my_functions import is_even
res = is_even(8)