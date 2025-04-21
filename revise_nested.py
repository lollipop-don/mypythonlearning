favourite_languages = {
    'jehn' : ['python','rust'],
    'sarah' : ['c'],
    'edward' : ['rust','go'],
    'phil' : ['python', 'haskell']
     } 

# for name,languages in favourite_languages.items():
#     print(f"{name.title()}'s favourite languages are:")
#     for value in languages:
#         print(f'\t {value.title()}')



# Jehn's favourite language is:
#   Python
#   Rust

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton'
    },
    'mcurie' : {
         'first' : 'marie',
         'last' : 'curie',
         'location' : 'paris'
    }
}

# Username: aeinstein
#     Full name: Albert Einstein
#     Location: Princeton

for name,info in users.items():
    print(f'Username : {name}')
    print(f"\tFull name : {info['first'].title()} {info['last'].title()}")
    print(f"\tLocation : {info['location'].title()}")

