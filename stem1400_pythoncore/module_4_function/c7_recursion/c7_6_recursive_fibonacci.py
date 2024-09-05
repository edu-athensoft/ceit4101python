"""
Fibonacci sequence

f(n) = f(n-1) + f(n-2)
f(1) = 1
f(2) = 1
"""


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return f(n - 1) + f(n - 2)


# main
print(f(0))
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))
print(f(6))


