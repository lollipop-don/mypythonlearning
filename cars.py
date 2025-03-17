cars = ['bmw','audi','toyota','subaru']


#sorts list in ascending order(modifies list)
cars.sort()

#sorts list in descending order(modifies list)
cars.sort(reverse=True)

#print list in sorted but doesnt change the list itself 
cars = ['bmw','audi','toyota','subaru']
print(f'here are the original cars {cars}')
print(f'here is the sorted list {sorted(cars,reverse=True)}')
print(f'these are the cars after sorting {cars}')

#how to reverse list(and modifies list)
cars = ['bmw','audi','toyota','subaru']
cars.reverse()

numbers = [3,5,6,8,7]
numbers.reverse()
#count the number of elements in the list
print(f'number of elements in numbers is {len(numbers)}')

pass