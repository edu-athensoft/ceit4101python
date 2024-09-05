"""
find the 2nd target
"""


def find_second_index(lst, element):
    try:
        first_index = lst.index(element)
        return lst.index(element, first_index + 1)
    except ValueError:
        return -1  # Return -1 if the element doesn't appear twice


# Example usage
numbers = [3, 8, 1, 6, 0, 8, 4, 8, 9, 8]
target = 8
print(find_second_index(numbers, target))  # Output: 5

