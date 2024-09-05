"""
for loop
find the max number from a list
"""

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

max = numbers[0]
for i in numbers:
    if i > max:
        max = numbers[i]

print("max number is {}".format(max))