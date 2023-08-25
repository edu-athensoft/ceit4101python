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
    def __init__(self):
        super().__init__()


# main
dog1 = Dog()

# can access parent's method
# super().__init__ is called in Dog(Child) class
print(dog1.name)



