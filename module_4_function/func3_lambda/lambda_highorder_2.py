"""
High Order Function
lambda as parameter
"""


add = lambda x, y : x+y
sub = lambda x, y : x-y
mul = lambda x, y : x*y
div = lambda x, y : x/y

def cal(a, b, oper):
    return oper(a, b)

a = 2
b = 3

result = cal(2,3, add)
print(result)

result = cal(2,3, sub)
print(result)

result = cal(2,3, mul)
print(result)

result = cal(2,3, div)
print(result)