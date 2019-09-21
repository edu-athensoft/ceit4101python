# exception handling

"""raise exception manually"""

try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print('ZeroDivisionError')
except:
    print('some error occured')
