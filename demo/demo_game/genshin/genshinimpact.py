"""

"""


class Item:
    def __init__(self, point, quantity):
        self.point = point
        self.quantity = quantity

    def totalpoints(self):
        return self.point * self.quantity

    def getqty(self):
        return self.quantity

    def getpoint(self):
        return self.point


class A(Item):
    def __init__(self, quantity=1):
        self.point = 1
        super().__init__(self.point, quantity)

    def forge_to_B(self):
        RATIO = 3  # 3*A = B
        qty_B = self.getqty() // RATIO
        qty_A_left = self.getqty() % RATIO
        return qty_B, qty_A_left

    def forge_to_C(self):
        RATIO = 9  # 9*A = C
        qty_C = self.getqty() // RATIO
        qty_A_left = self.getqty() % RATIO
        return qty_C, qty_A_left

    def __str__(self):
        return f"A[point={self.point}, qty={self.quantity}]"


class B(Item):
    def __init__(self, quantity=1):
        self.point = 3
        super().__init__(self.point, quantity)

    def __str__(self):
        return f"B[point={self.point}, qty={self.quantity}]"

    def forge_to_C(self):
        RATIO = 3  # 3*B = C
        qty_C = self.getqty() // RATIO
        qty_B_left = self.getqty() % RATIO
        return qty_C, qty_B_left


class C(Item):
    def __init__(self, quantity=1):
        self.point = 9
        super().__init__(self.point, quantity)

    def __str__(self):
        return f"C[point={self.point}, qty={self.quantity}]"


def test_a():

    def convert_a_to_b(materialA):
        print("\nconverting A to B  (3A=1B)")
        qty_B, qty_A_left = materialA.forge_to_B()

        msg = ""
        if qty_A_left == 0:
            msg = f"You will get Bx{qty_B}."
        else:
            msg = f"You will get Bx{qty_B} and Ax{qty_A_left} left."
        print(msg)

    def convert_a_to_c(materialA):
        print("\nconverting A to C  (9A=1C)")
        qty_C, qty_A_left = materialA.forge_to_C()

        msg = ""
        if qty_A_left == 0:
            msg = f"You will get Cx{qty_C}."
        else:
            msg = f"You will get Cx{qty_C} and Ax{qty_A_left} left."
        print(msg)

    # create A
    materialA = A(15)
    qty_A = materialA.getqty()
    print(f"You have Ax{qty_A}.")

    # forge B with A
    convert_a_to_b(materialA)

    # forge C with A
    convert_a_to_c(materialA)


def test_b():
    def convert_b_to_c(materialB):
        print("\nconverting B to C  (3B=1C)")
        qty_C, qty_B_left = materialB.forge_to_C()

        msg = ""
        if qty_B_left == 0:
            msg = f"You will get Cx{qty_C}."
        else:
            msg = f"You will get Cx{qty_C} and Bx{qty_B_left} left."
        print(msg)

    # create B
    materialB = B(7)
    qty_B = materialB.getqty()
    print(f"You have Bx{qty_B}.")

    # forge C with B
    convert_b_to_c(materialB)


def isNeedFarm(qty_a, qty_b, qty_c):
    needFarm = False
    return needFarm


def main():
    print("=== Test Material A ===")
    test_a()
    print("\n\n")

    print("=== Test Material B ===")
    test_b()
    print("\n\n")


if __name__ == "__main__":
    main()
