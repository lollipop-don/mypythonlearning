pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# pets.remove('cat')
# print(pets)

while 'cat' in pets:
    pets.remove('cat')


# print(pets)


def describe_pet(pet_name, animal_type = "dog"):  #defualt argument is dog
    print(f'i have {animal_type}')
    print(f"my {animal_type}'s name is {pet_name}")

describe_pet('willy', 'dog') 


describe_pet('harry', 'hamster') #call function by positional arguments
# describe_pet(animal_type = 'hamster', pet_name = 'harry') # call function by keyword arguments
# describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet('jim', 'dog') #positional arguments
describe_pet(animal_type ='dog', pet_name = 'loma')

describe_pet(pet_name= 'loki')
describe_pet(pet_name= 'little hamster', animal_type= 'hamster')