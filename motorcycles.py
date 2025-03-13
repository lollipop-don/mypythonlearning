motorcycles = ['honda','yamaha','suzuki']
#print(motorcycles[0])
#print(motorcycles)
motorcycles[0] = 'ducati'
#print(motorcycles)
#print(motorcycles[1])

#append element at the end of list
motorcycles.append('ducati')
#print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

motorcycles.insert(0,'ducati')
motorcycles.insert(2,'tiko')
del motorcycles[2]
removed_element = motorcycles.pop()
pass
