"""
module 7. exception handling

Raise multiple exceptions
pay attention to the order in which exceptions raise
compare with exception_4_raise_3.py
"""

try:
    num = int(input("Enter a number: "))
    if num == 1:
        raise ValueError("That is not a positive number!")

    assert num % 2 == 0

except AssertionError:
    print("Not an even number!")

except ValueError as ve:
    print("ValueError Caught: ", ve, ve.args[0])


