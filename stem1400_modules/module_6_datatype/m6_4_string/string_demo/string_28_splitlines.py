"""
string method - splitlines
"""

grocery = "Wilk\nChicken\r\nBread\rButter"

# case 1.
res = grocery.splitlines()
print(res)

# case 2.
res = grocery.splitlines(True)
print(res)

# case 3.
grocery = "Wilk Chicken Bread Butter"
res = grocery.splitlines()
print(res)

res = grocery.split()
print(res)




