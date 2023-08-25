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

    @classmethod
    def getToolCount(cls):
        return cls.count


# test
tool1 = Tool("screwdriver")
print(f'{Tool.getToolCount()} tool(s) is(are) created.')

tool2 = Tool("drill")
print(f'{Tool.getToolCount()} tool(s) is(are) created.')

tool3 = Tool("saw")
print(f'{Tool.getToolCount()} tool(s) is(are) created.')

tool4 = Tool("hammer")
print(f'{Tool.getToolCount()} tool(s) is(are) created.')

tool5 = Tool("Tweezers")
print(f'{Tool.getToolCount()} tool(s) is(are) created.')
