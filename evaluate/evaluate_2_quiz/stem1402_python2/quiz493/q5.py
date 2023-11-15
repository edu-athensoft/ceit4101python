"""
quiz493
q5
"""

def outer():
    def inner():
        nonlocal x
        print("inner:", x)

    inner()

outer()
