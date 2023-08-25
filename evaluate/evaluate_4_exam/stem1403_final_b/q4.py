"""
question 4. Parameter passing

9,10,9,11,10
"""

def foo(num):
    num = num + 1
    print(num)

num = 9
print(num)
foo(num)
print(num)
num = 10
foo(num)
print(num)

