"""
define a simple class
with instance attributes and methods
"""


class Duck:
    # define instance attributes
    def __init__(self, name, color, height=18.0, weight=1.8):
        self.name = name
        self.color = color
        self.height = height
        self.weight = weight

    def swim(self):
        pass

    def walk(self):
        pass

    def quack(self):
        pass

    def eat(self):
        pass

