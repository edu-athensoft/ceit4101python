"""
multi-level init

grandson inherits init() of Son.
Son has not property: age


grandson looks up for the init() by MRO rules.
Once it finds an init() then stops.

"""


class GrandParent:
    def __init__(self, name):
        print('GrandParent __init__() called.')
        self.name = name


class Son(GrandParent):
    # accessed but parameters did not match
    def __init__(self):
        print('Son __init__() called.')


class GrandSon(Son):
    def __init__(self, age):
        print('GrandSon __init__() called.')
        super().__init__(age)


# main
gs1 = GrandSon(16)
print(gs1.age)
