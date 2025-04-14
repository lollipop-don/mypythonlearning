alien_0 = {'color' : 'green', 'speed' : 'slow'}


# How to get value from dictionary  without mistake when key is not in dictionary
#When key is not in dictionary get still returns value which is second argument to get
# print(alien_0['points'])
point_value = alien_0.get('points','no point value aasigned')
print(point_value)

color_value = alien_0.get('color','no color value aasigned')
print(color_value)