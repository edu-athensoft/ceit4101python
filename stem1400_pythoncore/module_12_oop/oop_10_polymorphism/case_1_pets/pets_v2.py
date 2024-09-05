"""
Module: OOP
Polymorphism

show pet's name
"""


class Pet:
    def __init__(self, petClass='pet'):
        self.petClass = petClass

    def eat(self):
        print("A pet eats food.")


class Cat(Pet):
    def eat(self):
        print("Cat eats fish.")


class Dog(Pet):
    def eat(self):
        print("Dog eats meat.")


class Person:
    def __init__(self, name):
        self.name = name

    def feed(self, pet):
        print(f"{self.name} feeds his {pet.petClass}.")
        pet.eat()

        # if pet is Dog:
        #     pass
        # elif pet is Cat:
        #     pass
        # elif pet is Pet:
        #     pass


# main
peter = Person("Peter")
cat = Cat("cat")
dog = Dog("dog")

# Peter feeds his cat.
peter.feed(cat)
print()

# Peter feeds his dog.
peter.feed(dog)
print()

# Peter feeds his pet.
pet = Pet()
peter.feed(pet)

