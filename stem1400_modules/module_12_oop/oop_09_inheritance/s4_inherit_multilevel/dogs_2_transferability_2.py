"""
Transferability of Inheritance
"""

class Animal:
    def __init__(self):
        self.name = "animal.name"

    def eat(self):
        print("animal eats.")


class Dog(Animal):
    # def __init__(self):
    #     # super().__init__()
    #     self.species = "dog"

    def bark(self):
        print("dog barks.")


class PoliceDog(Dog):
    # def __init__(self):
    #     super().__init__()
    #     self.age = 2

    def fight(self):
        print("police dog fights")


# main
pdog_peter = PoliceDog()


# super().__init__() allows subclass to inherit superclass's property
# Now the property of pdog_peter.name is accessible.
print(pdog_peter.name)
pdog_peter.eat()
print()

# print(pdog_peter.species)
pdog_peter.bark()
print()

# print(pdog_peter.age)
# pdog_peter.fight()