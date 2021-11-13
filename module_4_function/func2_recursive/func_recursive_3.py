"""
recursive function
"""

# factorial of 6
# 6x5x4x3x2x1
# 6!

"""
product = 1
for i in range(1,7):
    product *= i

print("Factorial of 6 is {}".format(product))
"""

"""
f(n) = n * f(n-1)
...
f(6) = 6 * f(5)
f(5) = 5 * f(4)
f(4) = 4 * f(3)
f(3) = 3 * f(2)
f(2) = 2 * f(1)
f(1) = 1

f(n) = n * f(n-1)
1x2x3x......x(n-1)xn
"""


def fact(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * fact(n-1)
    else:
        print("n must be a positive integer!")
        return


product = fact(6)
print(product)


