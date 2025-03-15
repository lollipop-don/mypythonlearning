guests = ['elene','ana','mari']
print(f'{guests[0]} please come to dinner')
print(f'{guests[1]} please come to dinner')
print(f'{guests[2]} please come to dinner')
print(f'{guests[2]} can not come to dinner')
guests[2] = 'anamaria'
print(f'{guests[0]} please come to dinner')
print(f'{guests[1]} please come to dinner')
print(f'{guests[2]} please come to dinner')
print('everyone i found a bigger dinner table')
guests.insert(0,'tekla')
guests.insert(2,'nini')
guests.append('barbare')
print('i am sorry everyone i can only invite 2 people')
guest_1 = guests.pop()
guest_2 = guests.pop()
guest_3 = guests.pop()
guest_4 = guests.pop()
print(f'{guest_1} sorry')
print(f'{guest_2} sorry')
print(f'{guest_3} sorry')
print(f'{guest_4} sorry')
print(f'{guests[0]} and {guests[1]} you are still invited')
del guests[0]
del guests[0]
print(guests)
pass