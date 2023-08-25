"""
9.8 Accessing members of parent classes
case 4. forcely accessing private properties and methods of parent class
"""


class Animal:
    def __init__(self):
        self.name = "animal name"

    def __eat(self):
        print("Animal eat()")


class Dog(Animal):
    def eat(self):
        super()._Animal__eat()
        print("Dog called Animal's private eat()")


# main
dog1 = Dog()

# access parent's method
dog1.eat()


