"""
4. Write a program to check if two given sets have no elements in common.
"""

def has_common(set1, set2):
    return not set1 & set2

set_a = {1,2,3}
set_b = {1,2,3}
set_b = {4,5,6}
print(has_common(set_a, set_b))