"""
adding properties by assignment
"""


class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


# test
tool1 = Tool("hammer")
print(f'{tool1.count} tool(s) is(are) created.')
print()

tool1.count = 99
print(f'The instance tool1 has extra property: count')
print(f'{tool1.count} tools are created.')
print()

print(f'Now instance property has nothing to do with class property: count')
print(f'{Tool.count} tools are created.')

