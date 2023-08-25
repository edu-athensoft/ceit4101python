"""
multiple inheritance

subclass inherits methods in different names
"""

class Orange:
    def orange_action(self):
        print("orange_action()")


class Lemon:
    def lemon_action(self):
        print("lemon_action()")


class Lemange(Orange, Lemon):
    pass


# main
lemange1 = Lemange()
lemange1.orange_action()
lemange1.lemon_action()