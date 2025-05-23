unprinted_designs = ['phone case','robot pendant','dodekahedron']
completed_models = []

print(f'unprinted design is created at address: {id(unprinted_designs)}')
# while unprinted_designs:
#     popped_design = unprinted_designs.pop()
#     print(f'{popped_design} printed')
#     completed_models.append(popped_design)

# print('***************************************')
# print(f'the following models have been printed:')
# for value in completed_models:
#     print(value)

def print_designs(unprinted_designs, completed_models):
    while unprinted_designs:   
        popped_design = unprinted_designs.pop()
        print(f'{popped_design} printed')
        completed_models.append(popped_design)

def show_completed_models(models):
    pass
    for value in models:
        print(f'completed model is {value}')
print_designs(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(f'unprinted designs is {unprinted_designs} and its address now is {id(unprinted_designs)}')
print('tiko')

