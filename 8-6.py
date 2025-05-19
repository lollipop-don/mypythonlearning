def city_country(city, country):
    city_and_country = f'{city.title()}, {country.title()}'
    return city_and_country
info = city_country('paris', 'france')
print(info)