"""
6. Write a program to calculate the sum of a number list from 1 to 1000 using recursion.
"""

import sys

sys.setrecursionlimit(2000)  # set recursion depth limit to 2000

def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

print("Sum from 1 to 1000:", sum_recursive(1000))
