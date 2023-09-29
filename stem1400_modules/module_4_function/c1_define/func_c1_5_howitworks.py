"""
1.5 how does a function work?
"""


def foo1():
    print("1111", 'in foo1()')
    print("1112", 'in foo1()')
    print("1113", 'in foo1()')
    a = 1
    b = a + 1
    print(b, 'in foo1()')
    return b


print("== start ===")
result = 0
foo1()
print(result, 'in main program')
print("== end ===")
