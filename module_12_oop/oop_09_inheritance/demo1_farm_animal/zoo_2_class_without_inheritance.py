"""
OOP - inheritance
Animals

v2. Classes without inheritance
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


class Dog:
    def eat(self):
        print("eats.")

    def drink(self):
        print("drinks.")

    def run(self):
        print("runs.")

    def sleep(self):
        print("sleeps.")

    # exclusive
    def bark(self):
        print("barks.")

# there is no exclusive methods
# creature1 = Animal()
#
# creature1.eat()
# creature1.drink()
# creature1.run()
# creature1.sleep()

creature1 = Dog()

creature1.eat()
creature1.drink()
creature1.run()
creature1.sleep()
creature1.bark()