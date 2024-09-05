"""
Transferability of Inheritance
"""

class Animal:
    def __init__(self):
        self.name = "animal.name"

    def eat(self):
        print("animal eats.")


class Dog(Animal):
    def __init__(self):
        self.species = "dog"

    def bark(self):
        print("dog barks.")


class PoliceDog(Dog):
    def __init__(self):
        self.age = 2

    def fight(self):
        print("police dog fights")


# main
pdog_peter = PoliceDog()


print(pdog_peter.name)  # ERROR
# ERROR: because subclass did not call super class's __init__ method
# hence the property of pdog_peter.name cannot be accessed.
pdog_peter.eat()

# print(pdog_peter.species)
pdog_peter.bark()

# print(pdog_peter.age)
pdog_peter.fight()