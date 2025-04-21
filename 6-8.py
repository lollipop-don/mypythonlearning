bobi = {
    'kind' : 'bulldog',
    'owner' : 'tatia'
    }

popi = {
    'kind' : 'golden retriever',
    'owner' : 'ana'
}

pets = []
pets.append(bobi)
pets.append(popi)
for pet in pets:
        print(f"kind : {pet['kind']}   owner : {pet['owner']}")

# ["{'kind': 'bulldog', 'owner': 'tatia'}{'kind': 'golden retriever', 'owner': 'ana'}"]

