class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"the restaurant's name is {self.name} and cuisine type is {self.cuisine_type}")
    def open_restaurant(self):
        print('the restaurant is open')

restaurant = Restaurant('Magnolia','Georgian cuisine')
print(f"the restaurant's name is {restaurant.name}")
print(f"the restaurnats cuisine type is {restaurant.cuisine_type}")


restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2.py
restaurant_2 = Restaurant('Chveni qalaqi','fast food')
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant('Mwvane ezo','different foods')
restaurant_3.describe_restaurant()