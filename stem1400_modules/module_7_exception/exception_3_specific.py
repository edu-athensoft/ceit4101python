"""
module 7. exception handling

Catching Specific Exceptions in Python
"""

"""
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass
"""

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except ValueError as e:
        print("Oops!", e.__class__, "occurred.")
        print()
    except (TypeError, ZeroDivisionError) as e:
        print("Oops!", e.__class__, "occurred.")
        print()
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print()
print("The reciprocal of", entry, "is", r)