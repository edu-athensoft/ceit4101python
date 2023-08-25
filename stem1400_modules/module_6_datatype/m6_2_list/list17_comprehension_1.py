"""
list comprehension
"""

array = [x * x for x in range(1, 11) if x % 2 == 0]

print(array)


array2 = [m + n for m in 'ABC' for n in 'XYZ']

print(array2)
