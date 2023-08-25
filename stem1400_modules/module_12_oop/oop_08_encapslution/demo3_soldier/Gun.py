"""
Module 12: OOP
Topic:  Encapsulation
demo:   Soldier
entity:  Solider
"""

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


# test
ak47 = Gun("AK47")
ak47.shoot()
ak47.shoot()
ak47.shoot()
ak47.shoot()
ak47.shoot()
ak47.shoot()
ak47.add_bullet(ak47.capacity)
ak47.shoot()
ak47.shoot()
ak47.shoot()
ak47.shoot()
ak47.shoot()
ak47.shoot()






