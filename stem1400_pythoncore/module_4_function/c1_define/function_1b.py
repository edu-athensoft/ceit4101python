"""
function

reusable

step1. define, create
step2. call a function
"""


# step1.define
def myfunc1():
    print("hello")
    print("python function")
    # function body

# step2. call
myfunc1()


# y = x
def mathfunc1(x):
    y = x
    return y

x = 2
result = mathfunc1(x)
print("x={}, for y=x, result: y = {}".format(x, result))

x = -2
result = mathfunc1(x)
print("x={}, for y=x, result: y = {}".format(x, result))

x = 1.5
result = mathfunc1(x)
print("x={}, for y=x, result: y = {}".format(x, result))

# y = 2x
# y = 2x + 1







