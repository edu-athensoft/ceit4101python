"""
return statement

return None
"""


# return None implicitly
def foo1():
    x = 1


# return None implicitly
def foo2():
    x = 1
    return


# return None explicitly
def foo3():
    x = 1
    return None


# test
print(f'foo1() returned {foo1()}')
print(f'foo2() returned {foo2()}')
print(f'foo3() returned {foo3()}')
