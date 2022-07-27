"""
multi-level init

grandson inherits init() of Son.
Son has a property: age

grandson looks up for the init() by MRO rules.
Once it found an init() then stops.

"""


class GrandParent:
    # not accessed in this case
    def __init__(self, name):
        print('GrandParent __init__() called.')
        self.name = name


class Son(GrandParent):
    # accessed and parameters matched
    def __init__(self, age):
        print('Son __init__() called.')
        self.age = age


class GrandSon(Son):
    def __init__(self, age):
        print('GrandSon __init__() called.')
        super().__init__(age)


# main
gs1 = GrandSon(16)
print(gs1.age)
