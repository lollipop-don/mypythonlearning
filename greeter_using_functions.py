def get_formmated_name(f_name, l_name):
    formmated_name = f'my name is {name} and my last name is {last_name}'
    return formmated_name

while True:
    name = input('your name\n')
    last_name = input('last name\n')
    if name == 'quit' or last_name == 'quit':
        break

    

    full_name = get_formmated_name(name, last_name)
    print(full_name) 