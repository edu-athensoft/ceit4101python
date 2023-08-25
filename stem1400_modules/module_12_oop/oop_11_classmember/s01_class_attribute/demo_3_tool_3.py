"""
class attributes

Tool class
counting how many instances are created

access class attributes via instance
"""


class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


# test
tool1 = Tool("screwdriver")
print(f'{tool1.__class__.count} tools are created.')

tool2 = Tool("drill")
print(f'{tool2.__class__.count} tools are created.')

tool3 = Tool("saw")
print(f'{tool3.count} tools are created.')

tool4 = Tool("hammer")
print(f'{Tool.count} tools are created.')

tool5 = Tool("Tweezers")
print(f'{Tool.count} tools are created.')
