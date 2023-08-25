"""
Project

File name: houseapp.py
"""

# creating house items
bed = HouseItem('bed',4)
print(bed)

chest = HouseItem('chest',2)
print(chest)

table = HouseItem('table',1.5)
print(table)

# creating house
myhouse = House("Condo-4bedroom",90)
print(myhouse)

myhouse.add_item(bed)
print(myhouse)

myhouse.add_item(chest)
print(myhouse)

myhouse.add_item(table)
print(myhouse)
