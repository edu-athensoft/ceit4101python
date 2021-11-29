"""
OOP - inheritance
Animals

v1. Multi-level inheritance
"""

class Animal:
    def eat(self):
        print("eats.")

    def drink(self):
        print("drinks.")

    def run(self):
        print("runs.")

    def sleep(self):
        print("sleeps.")


class Dog(Animal):
    # exclusive
    def bark(self):
        print("A dog barks.")


class PoliceDog(Dog):
    # exclusive
    def track(self):
        print("A police dog tracks.")

    def sniff(self):
        print("A police dog sniff out dangerous items.")

    def fight(self):
        print("A police dog fights bad guys.")

# main
farmDog1 = Dog()

# inherited methods from base class
farmDog1.eat()
farmDog1.drink()
farmDog1.run()
farmDog1.sleep()

# exclusive methods of Dog
farmDog1.bark()

# exclusive methods of PoliceDog
policeDog1 = PoliceDog()

policeDog1.eat()
policeDog1.drink()
policeDog1.run()
policeDog1.sleep()

policeDog1.bark()

policeDog1.track()
policeDog1.sniff()
policeDog1.fight()



