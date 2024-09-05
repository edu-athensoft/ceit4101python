"""
inheritance
hierarchical
"""

class Pet:
    def __init__(self, name="pet", species=None):
        self.name = name
        self.species = species
        self.istamed = True

    def inhabit(self):
        print(f"{self.species} inhabit with human")

    def set_species(self, s):
        self.__species = s


class Dog(Pet):
    def bark(self):
        print(f"{self.species} barks")

    def chew(self):
        print(f"{self.species} chews")


class Cat(Pet):
    def climb(self):
        print(f"{self.species} climbs")

    def groom(self):
        print(f"{self.species} grooms")


# main logic
dog1 = Dog()
dog1.inhabit()      # parent's method
dog1.bark()
dog1.chew()
print()

dog2 = Dog(name="Peter", species="Dog")
dog2.inhabit()      # parent's method
dog2.bark()
dog2.chew()
