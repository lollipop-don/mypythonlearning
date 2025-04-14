#How to get value from dictionary using key
alien_0 = {'color' : 'green', 'points' : 5}
print(type(alien_0))   
print(alien_0)
print(f"aliens color is {alien_0['color']}")
new_points = alien_0['points']

#Add 2 new (key/value) to alien_0
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 1
alien_0['color'] = 'yellow'


#How to modify a value inside dictionary based on  speed
alien_0 = {'x_position' : 7, 'y_position' : 25, 'speed' : 'fast', 'points' : 5}
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment     
pass  

#How to delete key-value from alien_0 dictionary?
print(f'before deleting points alien_0 is {alien_0}')
del alien_0['points']
print(f'after deleting points now alien_0 is {alien_0}')