# find all prime numbers from 100 to 200

# is_prime

def is_prime(num):
    for value in range(2,num):
        if num % value == 0:
            return False
    return True

def is_odd(num):
    if num % 2 == 0:
        return False
    return True

def is_even(number):
    if number % 2 == 0:
        return True
    return False

def max_number_in_list(nums):
    num = nums[0]
    for value in nums:
        if value > num:
            num = value
    return num

def sum_all_numbers(nums):
    num = 0 
    for value in nums:
        num = num + value
    return num


def max_between_two_numbers(num1,num2):
    if num1 > num2:
        return num1
    return num2