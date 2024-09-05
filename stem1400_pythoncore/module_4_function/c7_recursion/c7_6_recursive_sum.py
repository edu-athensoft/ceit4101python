"""
1+2+3+4+...+n

f(1)=1
f(2) = 2 + f(1)
...
f(n) = n + f(n-1)
"""


def f(n):
    if n == 1:
        return 1

    return n + f(n - 1)


# main
print(f(100))

print(f(10))

