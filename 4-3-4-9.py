#4-3
# for value in range(1,21):
#     print(value)

#4-4
#a
# one_million = []
# for value in range(1,1000000): 
#     one_million.append(value)
#b
# one_million = list(range(1,1000001))    

#c
# one_million = [value for value in range(1,1000001)]

# 4-5
# onemillion = list(range(1,1000001))
# a = min(onemillion)
# b = max(onemillion)
# print(f'min element is {a} and max element is {b}')
# c = sum(onemillion)
# print(c)

# 4-6
# lst = [value for value in range(1,21,2)]

# for value in lst: 
#    print(value) 
#     
 
#4-7
# threes = [value for value in range(3,31,3)]
# for value in threes:
#     print(value)


#4-8
#list creation
# cubes = []
# for value in range(1,11):
#     cubes.append(value**3)
#end of list creation

#now print each element from already created list
# for value in cubes:
#     print(value)

#4-9
cubes = [value**3 for value in range(1,11)]
for value in cubes:
    print(value)
