class User:
    def __init__(self, first_name, last_name, age, gender):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.gender = gender
    def describe_user(self):
        print(f"user info: name-{self.f_name}, last name-{self.l_name}, age-{self.age},gender-{self.gender}")
    def greet_user(self):
        print(f'hello {self.f_name} {self.l_name}')

user_tiko = User('tiko','tyablaze',13,'female')
user_tiko.describe_user()
user_tiko.greet_user()


user_gigi = User('gigi','tyablaze',9,'male')
user_gigi.describe_user()
user_gigi.greet_user()