"""
Filtering and Transforming Dictionary Items

Problem Statement:
Write a function filter_and_transform(dictionary) that takes a
dictionary as input and performs the following tasks:

- Filters out all items from the dictionary where the value is not an integer.
- Transforms the remaining items by doubling their values.
- Returns a new dictionary containing the transformed items.

Requirements:
- Use the items() method to iterate through the dictionary items.
- The function should not modify the original dictionary.
- Demonstrate the function with an example input.
"""

def filter_and_transform(dictionary):
    return {key: value * 2 for key, value in dictionary.items() if isinstance(value, int)}

# Example usage:
input_dict = {
    'a': 1,
    'b': 'string',
    'c': 3,
    'd': 4.5,
    'e': 5
}

result_dict = filter_and_transform(input_dict)

print("Original Dictionary:", input_dict)
print("Transformed Dictionary:", result_dict)
