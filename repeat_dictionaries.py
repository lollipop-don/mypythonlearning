# fvaourite_languages =  {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust', 
#     'phil': 'python', 
#     }
# friends  = ['phil','sarah',]

# for name in fvaourite_languages:
#     print(f'hi {name}')
#     if name in friends:
#         print(f'\ti see you like {fvaourite_languages[name]}')

responses = {}
polling_active = True
while polling_active:
    name = input('what is your name?')
    mountain = input('which mountain?')
    responses[name] = mountain
    response = input('would you like to continue? yes\\no ')
    if response == 'no':
        polling_active = False

for name,mta in responses.items():
    print(f"{name} would like to climb {mta}")

