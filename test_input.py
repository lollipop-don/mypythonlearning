# age = input('input your number:\n')
age = input()
number = int(age)
sum = 0
for value in range(1,number+1):
    sum = sum + value
print(f'sum is {sum}')
