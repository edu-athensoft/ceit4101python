"""
quiz492
q5
"""


def foo():
    global x
    print(f"{x}")
    x = 3
    print(f"{x}")

x = 9
foo()
print(f"{x}")