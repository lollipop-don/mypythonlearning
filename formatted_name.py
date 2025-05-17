def get_formatted_name(first_name, last_name):
    full_name = f'my name is {first_name.title()} and last name {last_name.title()}'
    return full_name

# _f_name = get_formatted_name('tiko', 'tyablaze')
# print(_f_name)


def add_two_numbers(number1, number2):
    number = number1 + number2
    return number

def multiplie_three_numbers(number1, number2, number3):
    number = number1 * number2 * number3
    return number
  
answer = multiplie_three_numbers(10,12345678,11)
print(answer)

# answer = add_two_numbers(3,5)
# print(answer)