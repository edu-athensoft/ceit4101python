"""
modeling and implementing
multiple objects update their own states
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
print("Hi, I am Peter.")
person1 = Person("Peter",75)
print(person1)

# affect Peter's own states
person1.run()
person1.eat()
print(person1)
print()

# Amy
print("Hi, I am Amy.")
person2 = Person("Amy",55)
print(person2)

# affect Amy's own states
person2.run()
person2.eat()
print(person2)



