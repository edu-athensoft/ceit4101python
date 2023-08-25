"""
module: exception
else clause

syntax:
try...except...else

if no such exception caught,
then goto else block
"""


try:
    num = int(input("Enter a number: "))
    if num == 1:
        raise ValueError("That is not a positive number!")

    assert num % 2 == 0

except AssertionError:
    print("Not an even number!")

except ValueError as ve:
    print("ValueError Caught: ",ve, '\n', ve.args[0])

else:
    reciprocal = 1/num
    print(reciprocal)
