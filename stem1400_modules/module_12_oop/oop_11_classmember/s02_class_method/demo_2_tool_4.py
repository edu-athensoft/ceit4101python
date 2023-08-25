"""
class attributes

Tool class
counting how many instances are created

calling a class method
"""


class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def getToolCount(cls):
        return cls.count

    @classmethod
    def showToolCount(cls):
        print('cls.getToolCount()='+str(cls.getToolCount()))


# test
Tool.showToolCount()
print()

tool1 = Tool("screwdriver")
print(f'{Tool.getToolCount()} tool(s) is(are) created.')
Tool.showToolCount()
print()

tool2 = Tool("drill")
Tool.showToolCount()

