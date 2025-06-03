# import my_functions

# for value in range(100,200):
#     if my_functions.is_prime(value) == True:
#         print(f'{value} is prime')

from  my_functions import is_prime

# res = is_prime(7)
for value in range(100,200):
    if is_prime(value) == True:
        print(f'{value} is prime')

 
from my_functions import is_odd
res = is_odd(7)
print(f'7 is_odd {res}')

from my_functions import is_even
res = is_even(7)
print(f' 7 is_even {res}')



for value in range(50,80):
    if is_odd(value) == True:
        print(value)
   
from my_functions import max_number_in_list

max = max_number_in_list([2,8,4,3,6,7])

print(f'max is {max}')

max = max_number_in_list([-2,-5,-6])
print(f'max is {max}')


from my_functions import sum_all_numbers

    
res = sum_all_numbers([52, 68, 67, 51])
print(f'the sum is {res}')




from my_functions import max_between_two_numbers

max = max_between_two_numbers(78, 45)
print(max)