"""
create 2 functions
1. y = 2x
2. y = 2x + 1
(whereas 2x means 2 * x)

call each function for 3 time with different input of x (value of x)
then print out the returned value for y
"""


def func1a(x):
    y = 2 * x
    return y


def func1b(x):
    return 2 * x


def func2a(x):
    y = 2 * x + 1
    return y


# call func1a when x = 1,2,3
result = func1a(1)
print("result: for y= 2x when x=1, then y={}".format(result))

result = func1a(2)
print("result: for y= 2x when x=2, then y={}".format(result))

result = func1a(3)
print("result: for y= 2x when x=3, then y={}".format(result))
print()

# call func2a when x = 1
result = func2a(1)
print("result: for y= 2x+1 when x=1, then y={}".format(result))

result = func2a(2)
print("result: for y= 2x+1 when x=2, then y={}".format(result))

result = func2a(3)
print("result: for y= 2x+1 when x=3, then y={}".format(result))
