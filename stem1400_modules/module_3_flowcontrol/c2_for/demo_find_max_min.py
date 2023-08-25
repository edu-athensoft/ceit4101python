"""
for loop
find the max number from a list
"""

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

max = numbers[0]
min = numbers[0]
for i in numbers:
    if i > max:
        max = numbers[i]
    if i < min:
        min = numbers[i]

print("The max number is {} and the min number is {}".format(max,min))