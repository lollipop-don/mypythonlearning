rivers = {'nile' : 'egypt', 'amazon' : 'brazil', 'dnepro' : 'ukraine' }
for key,value in rivers.items():
    print(f'The {key.title()} runs through {value.title()}')
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())   