# exception handling

"""single exception"""

try:
    a=5
    b=0
    c = a/b
    print("division=",c)
except ZeroDivisionError:
    print('ZeroDivisionError')
