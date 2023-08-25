# arbitrary arguments

def greet(*names):

    for name in names:
        print("Hello",name)

greet("Monica","Luke","Steve","John","Monica","Luke","Steve","John")