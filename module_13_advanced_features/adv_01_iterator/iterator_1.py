"""
examining list and list iterator
"""

numbers = [1, 2, 3]

# option1
number_iterator = numbers.__iter__()
print(type(number_iterator))

# option2
number_iterator = iter(numbers)
print(type(number_iterator))

# get item
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))

# StopIteration
# print(next(number_iterator))
