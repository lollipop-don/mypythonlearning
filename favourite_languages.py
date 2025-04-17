from fav_languages import name_language_dict

favourite_languages = {
    'jen' : 'python', 
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
    }
language = favourite_languages['sarah'].title()
print(f'sarahs favourite language is {language}')
for key, value in favourite_languages.items():
    print(f"{key.title()}'s favourite language is {value.title()}")


#Next exersice

print("***********************************")
#hello all people and give an extra greeting to your friends
friends = ['phil','sarah']
for value in favourite_languages.keys():
    print(f"Hello {value.title()}")
    if value in friends:
       print(f"\t{value.title()} you are my friend and i see you love {favourite_languages[value]}")

#How to iterate keys in dictionary in alphabetical order:
for gigi in sorted(favourite_languages.keys()):
    print(gigi)

#How to iterate values in dictionary in alphabetical order:
for tiko in sorted(favourite_languages.values()):
    print(tiko)

print(type(name_language_dict))
print(name_language_dict)

#How to iterate values in dictionary, not repeating them. 
for value in set(name_language_dict.values()):
    print(value)
