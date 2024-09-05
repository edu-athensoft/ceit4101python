"""
9.8 Accessing members of parent classes
case 2. overriding properties and methods of parent class
"""

class Animal:
    def __init__(self):
        self.name = "animal name"

    def eat(self):
        print("Animal eat()")


class Dog(Animal):

    def eat(self):
        print("Dog eat()")


# main
dog1 = Dog()

# overriding parent's method
# Animal's eat() was not accessed
dog1.eat()
print(dog1.name)

dog1.name = 'dog name: peter'
print(dog1.name)


