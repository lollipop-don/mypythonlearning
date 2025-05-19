def build_person(first_name, last_name, age = None):
    full_name = f'person is {first_name} and last name is {last_name}'
    if age:
        full_name = full_name + f'\nher/his age is {age}'
   
    return full_name

person = build_person('tiko', 'tyablaze')
print(person)
person = build_person('gigi', 'tyabladze', 9)
print(person)

def build_person_dict(first_name , last_name, age = None):
    person = {}
    person['first_name'] = first_name
    person['last_name'] = last_name
    if age:
        person['age'] = age
    return person

p_dict = build_person_dict('tiko', 'tyablaze', 13)
print(p_dict)