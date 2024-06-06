"""
quiz 652
6. Write a program to add one or more members to a set at a time
Hints: update()
"""

def update_set(my_set, *args):
    """
    Update the set based on the arguments:
    - Use add() if a single value is provided.
    - Use update() if multiple values are provided.
    """
    if len(args) == 1:
        my_set.add(args[0])
    elif len(args) > 1:
        my_set.update(args)
    return my_set

# Example usage
my_set = set()
print("Initial set:", my_set)

# Updating set with a single value
update_set(my_set, 'a')
print("After adding a single element:", my_set)

# Updating set with multiple values
update_set(my_set, 'b', 'c', 'd')
print("After adding multiple elements:", my_set)