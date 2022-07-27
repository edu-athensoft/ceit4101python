"""
multi-level init

grandson directly inherits init() of GrandParent
grandson looks up for the init() by MRO rules.
"""


class GrandParent:
    def __init__(self):
        print('GrandParent __init__() called.')


class Son(GrandParent):
    pass


class GrandSon(Son):
    pass


# main
gs1 = GrandSon()
