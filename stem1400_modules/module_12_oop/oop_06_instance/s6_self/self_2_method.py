"""
self

call other instance methods
"""


class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        # print("I eat.")
        print(f"{self.name} eat.")

    def sleep(self):
        # print("I sleep.")
        print(f"{self.name} eat.")

    def live(self):
        # call other methods with self
        self.sleep()
        self.eat()


# main program
tom = Cat('Tom')

tom.live()
