"""
quiz 652
6. Write a program to add one or more members to a set at a time
Hints: update()
"""
def is_iterable(value):
    try:
        iter(value)
        return True
    except TypeError:
        return False

# Example usage
print(is_iterable([1, 2, 3]))  # True, because a list is iterable
print(is_iterable("hello"))    # True, because a string is iterable
print(is_iterable(42))         # False, because an integer is not iterable
