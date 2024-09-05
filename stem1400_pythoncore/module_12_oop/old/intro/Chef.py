# oop
# inheritance

class Chef:
    def make_chicken(self):
        print("mk chicken")

    def make_salad(self):
        print("mk salad")

    def make_dish(self):
        print("mk dish")


class ChineseChef(Chef):
    def make_porc(self):
        print("mk porc")

    def make_dish(self):
        print("mk Chinese dish")