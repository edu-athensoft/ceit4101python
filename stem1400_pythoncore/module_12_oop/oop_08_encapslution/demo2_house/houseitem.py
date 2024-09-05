"""
project: Just moved in

__repr__ prints out value

__str__ prints out object meta info.
"""


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __repr__(self):
        """
        to print out object info.
        :return:
        """
        return self.name+","+str(self.area)

    # def __str__(self):
    #     return self.name+","+str(self.area)

# test code
bed = HouseItem('bed',4)
print(bed)

chest = HouseItem('chest',2)
print(chest)

table = HouseItem('table',1.5)
print(table)

