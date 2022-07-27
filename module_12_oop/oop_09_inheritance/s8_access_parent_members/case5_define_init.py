"""
9.8 Accessing members of parent classes
case 5. defining __init__ method in child class
"""


class Animal:
    def __init__(self):
        print('Animal() init')
        self.name = "animal name"

    def __eat(self):
        print("Animal eat()")


class Dog(Animal):
    def __init__(self):
        print('Dog() init')


# main
dog1 = Dog()

# cannot access parent's method
# because of __init__ defined in Dog(Child) class
# AttributeError: 'Dog' object has no attribute 'name'

try:
    dog1.name
except AttributeError:
    print('AttributeError: \'Dog\' object has no attribute \'name\'')
