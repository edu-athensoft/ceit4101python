"""
find the 2nd target
"""


def find_second_index(lst, element):
    count = 0
    for index, item in enumerate(lst):
        if item == element:
            count += 1
            if count == 2:
                return index
    return -1  # Return -1 if the element doesn't appear twice


numbers = [3, 8, 1, 6, 0, 8, 4, 8, 7, 8, 0]
target = 8
print(find_second_index(numbers, target))
