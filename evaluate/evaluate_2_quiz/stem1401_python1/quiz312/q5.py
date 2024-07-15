"""
Write a python program to get the min and max number from a given list of 10 numbers.
list1 = [2,6,5,1,9,0,4,8,7,3]
"""

# Given list of 10 numbers
list1 = [2, 6, 5, 1, 9, 0, 4, 8, 7, 3]

# Initial assumptions for min and max
min_number = list1[0]
max_number = list1[0]

# Manually compare each element to find the min and max

# Compare to the second element
if list1[1] < min_number:
    min_number = list1[1]
if list1[1] > max_number:
    max_number = list1[1]

# Compare to the third element
if list1[2] < min_number:
    min_number = list1[2]
if list1[2] > max_number:
    max_number = list1[2]

# Compare to the fourth element
if list1[3] < min_number:
    min_number = list1[3]
if list1[3] > max_number:
    max_number = list1[3]

# Compare to the fifth element
if list1[4] < min_number:
    min_number = list1[4]
if list1[4] > max_number:
    max_number = list1[4]

# Compare to the sixth element
if list1[5] < min_number:
    min_number = list1[5]
if list1[5] > max_number:
    max_number = list1[5]

# Compare to the seventh element
if list1[6] < min_number:
    min_number = list1[6]
if list1[6] > max_number:
    max_number = list1[6]

# Compare to the eighth element
if list1[7] < min_number:
    min_number = list1[7]
if list1[7] > max_number:
    max_number = list1[7]

# Compare to the ninth element
if list1[8] < min_number:
    min_number = list1[8]
if list1[8] > max_number:
    max_number = list1[8]

# Compare to the tenth element
if list1[9] < min_number:
    min_number = list1[9]
if list1[9] > max_number:
    max_number = list1[9]

# Print the results
print("The minimum number in the list is:", min_number)
print("The maximum number in the list is:", max_number)