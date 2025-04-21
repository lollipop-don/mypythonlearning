lst_1 = ['a','b','c','d']
lst_2 = ['e','f','g']
lst_3 = ['h','i','j','k','l','m','n']

full_list = [lst_1, lst_2, lst_3]
# full_list.append(lst_1)
# full_list.append(lst_2)
# full_list.append(lst_3)

for lst in full_list:
    for value in lst:
        print(value)

dict_1 = {
    'a' : 1,
    'b' : 2,
    'c' : 23
}
lst_1 = ['A','B','D','C']
dict_2 = {
    'x' : 11,
    'y' : 12
}
lst_2 = ['keti','aleqsandre','kecxovelis_13','datuna']
full_list = [dict_1,lst_1,dict_2,lst_2]
full_list = [
    {
    'a' : 1,
    'b' : 2,
    'c' : 23
    },
    ['A','B','D','C'],
    {
    'x' : 11,
    'y' : 12
    },
    ['keti','aleqsandre','kecxovelis_13','datuna']
]
print('****************************************')
for element in full_list:
    if type(element) == dict:
        for value in element.values():
            print(f"{value}")
    elif type(element) == list:
        for value in element:
            print(value)          