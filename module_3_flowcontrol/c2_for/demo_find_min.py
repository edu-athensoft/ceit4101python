"""
for loop
find the max number from a list
"""

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

min = numbers[0]
for i in numbers:
    if i < min:
        max = numbers[i]

print("min number is {}".format(min))