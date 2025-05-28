# number = input('enter number')
# number = int(number)



# def is_prime(number):
#     for value in range(2,number):
#         if number % value == 0:
#             return False
#         else:
#             return True

    

# is_p = is_prime(number)
# print(is_p)

# for value in range(2,number):
#     if number %value == 0:
#         print('number is not prime')
#         break

def is_odd(num):
    if num %2 == 0:
        return False
    else:
        return True
# number = input('enter number\n')
# number = int(number)
# result = is_odd(number)

# print(f'{number} is {result}')

# def sum_numbers(numbers):
#     num = 0
#     for value in numbers:
#         num = num + value 
#     return num

# res = sum_numbers([2,5,8,45,36,89])
# print(res)




def sum_odd_numbers(numbers):
    num = 0
    for value in numbers:
        if value %2 != 0:
            num = num + value
    return num


res = sum_odd_numbers([5, 87, 6, 41, 58])
print(res)



def func(a):
    # return 40
    return 55

res = func(34)





def sum_numbers(res):
    num = 0
    for value in res:
        num = num + value
    return num

res = sum_numbers([58, 56,77, 25])
print(f"I expect 216. Your answer is {res}")


def sum_even_numbers(lst):
    num = 0
    for value in lst:
        if value %2 == 0:
            num = num + value
    return num



lst = [35, 64, 33, 90, 35, 64, 33, 90,35, 64, 33, 90,35, 64, 33, 90,35, 64, 33, 90,35, 64, 33, 90,35, 64, 33, 90,35, 64, 33, 90,
       35, 64, 33, 90,35, 64, 33, 90,35, 64, 33, 90,35, 64, 33, 90,35, 64, 33, 90,35, 64, 33, 90,35, 64, 33, 90,]
res = sum_even_numbers(lst)

print(f'i excpect 154. i get {res}')


def max_number(nums):
    max_element = 0
    for value in nums:
        if value > max_element:
            max_element = value
    return max_element


# res = max_number([654, 5687, 2254, 5658, 5547, 52547, 22542])
res = max_number([-5, -7, -8])
print(f'I expect 52547. I get {res}')