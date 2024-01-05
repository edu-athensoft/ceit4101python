"""
quiz 273
Input and Output (Formatting)

Format Code of Number Type
d, c, b, o, x, X, n, e, E, f, F, g, G, %

"""

# 1. Please fill in the blank to complete the code to output an integer in binary format.
print("The binary number is {:b}".format(273))

# 2. Please fill in the blank to complete the code to output an integer in hexadecimal format.
print("The hex number is {:x}".format(273))

# 3. Please fill in the blank to complete the code to output a binary integer in decimal format.
print("The decimal number is {}".format(0b000100010001))

# 4. Please fill in the blank to output the floating-point number and round it up to 3 decimal places.
print("The floating-point number is {:.3f}".format(123.34567))

# 5. Please fill in the blank to output the given number in 9-character width
print("The floating-point number is {:9}".format(12.34))

# 6. Please fill in the blank to output the given number in width of 9 and filling with padding zero
print("The floating-point number is {:09} ".format(12.34))

# 7. Please fill in the blank to output the given number in percentage format
print("The number of correct answers is {}, the total number of questions is number is {}, and "
      "the correctness rate is {:%}".format(15, 20, 15/20))

