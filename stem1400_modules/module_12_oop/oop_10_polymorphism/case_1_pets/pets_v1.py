"""
Module: OOP
Polymorphism

passing an object as parameter
"""


class Pet:
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
        print(f"{self.name} feeds his pet.")
        pet.eat()


# main
peter = Person("Peter")
cat = Cat()
dog = Dog()

# Peter feeds his cat.
peter.feed(cat)
print()
# Peter feeds his dog.
peter.feed(dog)
print()

# Peter feeds his pet.
pet = Pet()
peter.feed(pet)

