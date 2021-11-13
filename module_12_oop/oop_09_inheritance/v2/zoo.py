"""
OOP - inheritance
Animals
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

