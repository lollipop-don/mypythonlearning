cities = {
    'tbilisi' : {
        'country' : 'georgia',
        'population' : '1.7m',
        'fact' : 'mamida lives there'
    },
    'london' : {
        'country' : 'great britain',
        'population' : '9m',
        'fact' : 'capital of uk'
    },
    'tokyo' : {
        'country' : 'japan',
        'population' : '37m',
        'fact' : 'advanced city'
    }
}

for city,info in cities.items():
    print(city.title())
    for key,value in info.items():
        print(f'\t{key.title()} : {value.title()}')
    # print('\n')