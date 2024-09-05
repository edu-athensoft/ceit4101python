"""
9.8 Accessing members of parent classes
case 3. accessing methods of parent class
super() - refer to the parent object
"""


class Animal:
    def __init__(self):
        self.name = "animal name"

    def eat(self):
        print("Animal eat()")


class Dog(Animal):
    def eat(self):
        super().eat()
        print("Dog called Animal's eat()")


# main
dog1 = Dog()

# access parent's method
dog1.eat()


