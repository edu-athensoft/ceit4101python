"""
module 7. exception handling

Raise multiple exceptions
pay attention to the order in which exceptions raise
compare with exception_4_raise_2.py
"""

try:
    num = int(input("Enter a number: "))

    assert num % 2 == 0

    if num == 1:
        raise ValueError("That is not a positive number!")

except AssertionError:
    print("Not an even number!")

except ValueError as ve:
    print("ValueError Caught: ", ve, ve.args[0])


