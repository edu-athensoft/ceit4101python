"""
9.8 Accessing members of parent classes
case 7. inheriting arguments during initialization of parent class
"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eat(self):
        print("Animal eat()")


class Dog(Animal):
    pass


# main
# we may pass two arguments
dog1 = Dog("Peter",1)

# access parent's attributes
print(dog1.name)
print(dog1.age)


