"""
module: exception
finally clause

syntax:
try...finally



"""


try:
    num = int(input("Enter a number: "))
    if num == 1:
        raise ValueError("That is not a positive number!")

    # assert num % 2 == 0

finally:
    print("this is finally clause")

# test 1
# input 1

# test 2
# input 2
