"""
Lambda Function

parameterized, table
"""


def table(n):
    return lambda a: a * n;


n = int(input("Enter the number?"))
b = table(n)

for i in range(1, n+1):
    print(n, "X", i, "=", b(i));
