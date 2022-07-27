"""
OOP - inheritance
Animals

v3. Classes with inheritance
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
        print("barks.")

# main
creature1 = Dog()

# inherited methods from base class
creature1.eat()
creature1.drink()
creature1.run()
creature1.sleep()

# exclusive methods of subclass
creature1.bark()