"""
Please write a Python program to determine which of the three numbers entered from the keyboard
is the largest and which one is the smallest. and output them in ascending order.
"""

# Read three numbers from the keyboard
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest and smallest numbers
if num1 > num2:
    if num1 > num3:
        max_number = num1
    else:
        max_number = num3
else:
    if num2 > num3:
        max_number = num2
    else:
        max_number = num3

if num1 < num2:
    if num1 < num3:
        min_number = num1
    else:
        min_number = num3
else:
    if num2 < num3:
        min_number = num2
    else:
        min_number = num3

# Determine the middle number
middle_number = num1 + num2 + num3 - max_number - min_number

# Print the numbers in ascending order
print("Numbers in ascending order:", min_number, middle_number, max_number)