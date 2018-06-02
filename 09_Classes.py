# class Dog:
#     """A simple attempt to model a dog."""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(self.name.title() + ' is now sitting.')
#
#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(self.name.title() + ' rolled over!')
#
#
# my_dog = Dog('snow', 2)
# other_dog = Dog('max', 4)
#
# print('\n##################')
# print('My dog\'s name is ' + my_dog.name.title() + '.')
# print('My dog is '+str(my_dog.age) + ' years old.')
# print('')
# my_dog.sit()
# my_dog.roll_over()
#
# print('\n##################')
# print('The other dog\'s name is ' + other_dog.name.title() + '.')
# print('The other dog is ' + str(other_dog.age) + ' years old.')
# print('')
# other_dog.sit()
# other_dog.roll_over()


class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(self.name.title() + ' serves ' + self.cuisine.title())

    def open_restaurant(self):
        print(self.name.title() + ' is open!')
#
# panda = Restaurant('panda express', 'chinese food')
# in_n_out = Restaurant('In-N-Out burgers', 'burgers')
# ijji = Restaurant('ijji', 'korean BBQ')
#
# panda.describe_restaurant()
# in_n_out.describe_restaurant()
# ijji.describe_restaurant()

# class User:
#     def __init__(self, first_name, last_name, sex, major):
#         self.first = first_name
#         self.last = last_name
#         self.sex = sex
#         self.major = major
#
#     def describe_user(self):
#         print('Name: ' + self.first.title() + ' ' + self.last.title())
#         print('Sex: ' + self.sex.title())
#         print('Major: ' + self.major.title())
#
#     def greet_user(self):
#         print('Hello ' + self.first.title() + ', welcome!')
#
#
# users = {'admin': ['christian', 'piscos', 'male', 'biochemistry']}
# for role, profile in users.items():
#     print()
#     print(str(role.title()))
#     user = User(profile[0], profile[1], profile[2], profile[3])
#     user.describe_user()
#     print()
#     user.greet_user()

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine='ice cream'):
        super().__init__(name, cuisine)
        self.flavors = []

    def show_flavors(self):


