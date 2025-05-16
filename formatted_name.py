def get_formatted_name(first_name, last_name):
    full_name = f'my name is {first_name.title()} and last name {last_name.title()}'
    return full_name

_f_name = get_formatted_name('tiko', 'tyablaze')
print(_f_name)