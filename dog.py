class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f'{self.name} is now sitting')
    def roll_over(self):
        print(f'{self.name} rolled over')


my_dog =  Dog('bobi',2)    
print(f"my dog's name is {my_dog.name}")
print(f"my dog's age is {my_dog.age}")

my_dog.sit()
my_dog.roll_over()


your_dog = Dog('Lucy',3)
print(f"your dog's name is {your_dog.name}")
print(f"your dog's age is {your_dog.age}")

your_dog.sit()
your_dog.roll_over()
