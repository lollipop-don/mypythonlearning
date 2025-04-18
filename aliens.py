#First create empty list and then
# append 30 alien dictionary in it
aliens = []
for value in range(1,31):
    alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(alien)
# for value in aliens[0:5]:
    # print(value)





d = {"one":1, "two":2}
d['two'] = 3


#iterate first 3 aliens(dictionary) in aliens list
# if alien's color is green, then make decision
#elif color is yellow make decision also.
for value in aliens[0:3]:
    if value['color'] == 'green':
        value['color'] = 'yellow'
        value['speed'] = 'medium'
        value['points'] = 10  
    elif value['color'] == 'yellow':
        value['color'] = 'red'  
        value['speed'] = 'fast'
        value['points'] = 15
for value in aliens[0:5]:
    print(value)