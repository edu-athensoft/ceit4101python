"""
1. Write a program to find the maximum and minimum values in a set.
"""


def find_max_min(values):
    """
    Returns the maximum and minimum values from a set.

    :param values: A set of numerical values.
    :return: A tuple containing the maximum and minimum values.
    """
    if not values:  # Check if the set is empty
        return None, None  # Return None for both max and min if the set is empty

    max_value = max(values)
    min_value = min(values)
    return max_value, min_value


# Example usage
my_set = {5, 3, 9, 1, 10}
max_val, min_val = find_max_min(my_set)
print("Maximum Value:", max_val)  # Output: Maximum Value: 10
print("Minimum Value:", min_val)  # Output: Minimum Value: 1
