"""
modeling and implementing

comparing implementation with that in procedural programming

multiple objects in client app

accessing instance variable in a method
"""

class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"name={self.name},weight={self.weight}"

    def run(self):
        # accessing instance variable in a method
        self.weight -= 0.5

    def eat(self):
        # accessing instance variable in a method
        self.weight += 1


# main

# Peter
person1 = Person("Peter",75)
print("initial state:",person1)

person1.run()
print("after running:",person1)

person1.eat()
print("after eating:",person1)




