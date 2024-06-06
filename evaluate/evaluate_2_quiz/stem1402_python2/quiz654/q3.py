"""
3. Write a program to check if a given value is present in a set or not.
"""

def is_contain(myset, item):
    if item in myset:
        return True
    else:
        return False


set1 = {5, 3, 9, 1, 10}
value = 9

print(is_contain(set1, value))