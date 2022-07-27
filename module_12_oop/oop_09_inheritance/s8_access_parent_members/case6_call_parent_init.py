"""
9.8 Accessing members of parent classes
case 6. calling __init__ method of parent class
"""


class Animal:
    def __init__(self):
        self.name = "animal name"

    def __eat(self):
        print("Animal eat()")


class Dog(Animal):
    pass


# main
dog1 = Dog()

# can access parent's method
# because of NO __init__ defined in Dog(Child) class
print(dog1.name)



