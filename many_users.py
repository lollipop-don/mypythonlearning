users = {
    'aeinstien' : {
        'first' : 'albert',
        'last' : 'einstien',
        'location' : 'princeton',
        },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris'
        }    
         }
for name,info in users.items():
    print(f'username : {name}')
    full_name = f"{info['first']} {info['last']}"
    location = f"{info['location']}"
    print(f'\tfull name : {full_name}')
    print(f'\tlocation : {location}')