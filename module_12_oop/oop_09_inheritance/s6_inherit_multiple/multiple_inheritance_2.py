"""
multiple inheritance

subclass inherits methods in the same names
which one will be called?
"""

class Orange:
    def parent_action(self):
        print("orange_action()")


class Lemon:
    def parent_action(self):
        print("lemon_action()")


class LemangeA(Orange, Lemon):
    pass


class LemangeB(Lemon, Orange):
    pass


# main
lemange1 = LemangeA()
lemange1.parent_action()

lemange2 = LemangeB()
lemange2.parent_action()