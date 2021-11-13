"""
Module 12: OOP
Topic:  Encapsulation
demo:   Soldier
entity:  Solider
"""

class Solider:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        # do not write code like this:
        # self.gun == None
        # using is, is not instead
        if self.gun is not None:
            print("Ahaaaa!")
            self.gun.add_bullet(self.gun.capacity)
            self.gun.shoot()
        else:
            print("Stay in position")


class Gun:
    def __init__(self, model):
        self.model = model
        self.capacity = 6
        self.bullet_count = self.capacity

    def add_bullet(self, count):
        # if self.bullet_count < self.capacity:
        self.bullet_count += count
        if self.bullet_count >= self.capacity:
            self.bullet_count = self.capacity
        print(f"The {self.model} has been reloaded.")

    def shoot(self):
        if self.bullet_count > 1:
            self.bullet_count -= 1
            print(f"The {self.model} shot.")
        else:
            print(f"Reload!")


# main
soldier1 = Solider("Peter")
# case 1. with a gun
ak47 = Gun("AK47")
soldier1.gun = ak47
soldier1.fire()
print()

# case 2. without a gun
soldier1.gun = None
soldier1.fire()
