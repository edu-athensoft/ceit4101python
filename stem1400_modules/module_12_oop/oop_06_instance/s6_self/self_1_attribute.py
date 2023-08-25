"""
self
adding temporary attributes to an object
accessing instance attributes
"""


class Cat:
    def eat(self):
        print("I eat.")
        print(f"{self.name} eat.")

    # def sleep(self):
    #     print("I sleep.")


# main program
tom = Cat()

tom.name = "Tom"
tom.eat()
# tom.sleep()

