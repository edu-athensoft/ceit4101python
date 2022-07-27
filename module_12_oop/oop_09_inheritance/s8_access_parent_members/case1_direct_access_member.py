"""
9.8 Accessing members of parent classes
case 1. directly accessing properties and methods of parent class
"""

class Animal:
    def __init__(self):
        self.name = "animal name"

    def eat(self):
        print("Animal eat()")


class Dog(Animal):
    # do not write __init__() here
    # so that dog object can access Animal's attribute
    pass


# main
dog1 = Dog()

# directly access parent's attribute
print(dog1.name)

# directly access parent's method
dog1.eat()
