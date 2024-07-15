"""
Please write a program to find the larger and smaller numbers
between two given numbers and give proper feedback to the user on console.
"""

num1 = 15
num2 = 15


# find the larger and smaller numbers
larger = None
smaller = None

if num1 > num2:
    larger = num1
    smaller = num2
elif num1 < num2:
    larger = num2
    smaller = num1
else:
    larger = smaller = num1


# output
if smaller != larger:
    print(f"The larger number is {larger}, and the smaller number is {smaller}.")
else:
    print(f"The two numbers are both equal to {larger}.")
