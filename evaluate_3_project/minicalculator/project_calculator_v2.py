"""
project: calculator
version 2.

step 1. allow to do the calculation for infinite times
step 2. set a condition for terminating the loop
option 1.
to input 'q' or 'quit' to stop the loop or exit the program
option 2.
to input a number other than 1-10 to exit the program


"""

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def mul(x,y):
    return x * y

def div(x, y):
    return x/y

def floordiv(x,y):
    return x // y

def modulus(x,y):
    return x % y

def exponent(a, n):
    return a ** n


def logical_and(x, y):
    return x and y

# logical_and(True, False)
# x = input("1st operand")
# y = input("2nd operand")
# print("x",x, "y",y)
# x = bool(x)
# y = bool(y)
# # print(logical_and(x, y))
# print("x",x,type(x), "y",y, type(y))

def logical_or(x, y):
    return x or y

def logical_not(x):
    return not x

# print out the menu with options that user can input
"""
My Calculator

Arithmetic Operation
1. adding
2. subtracting
3. multiplying
4. division
...

Logical Operation
8. and
9. or
10. not

Please choose an operation [1-10]:
"""

print("=== My Calculator ===")

# print out the menu


while True:
    opt = input("Please choose an operation [1-10]:")

    if opt == '1':
        print("you have selected {}".format(opt))
        x = float(input("Enter the first operand:"))
        y = float(input("Enter the second operand:"))
        result = add(x, y)
        print("The result is {}".format(result))

    elif opt == '2':
        print("you have selected {}".format(opt))
        x = float(input("Enter the first operand:"))
        y = float(input("Enter the second operand:"))
        result = subtract(x, y)
        print("The result is {}".format(result))

    elif opt == '3':
        print("you have selected {}".format(opt))
        x = float(input("Enter the first operand:"))
        y = float(input("Enter the second operand:"))
        result = mul(x, y)
        print("The result is {}".format(result))

    elif opt == '4':
        print("you have selected {}".format(opt))
        x = float(input("Enter the first operand:"))
        y = float(input("Enter the second operand:"))
        result = div(x, y)
        print("The result is {}".format(result))

    elif opt == '5':
        print("you have selected {}".format(opt))
        x = float(input("Enter the first operand:"))
        y = float(input("Enter the second operand:"))
        result = floordiv(x, y)
        print("The result is {}".format(result))

    elif opt == '6':
        print("you have selected {}".format(opt))
        x = float(input("Enter the first operand:"))
        y = float(input("Enter the second operand:"))
        result = modulus(x, y)
        print("The result is {}".format(result))

    elif opt == '7':
        print("you have selected {}".format(opt))
        x = float(input("Enter the first operand:"))
        y = float(input("Enter the second operand:"))
        result = exponent(x, y)
        print("The result is {}".format(result))

    elif opt == '8':
        print("you have selected {}".format(opt))
        x = input("Enter the first operand:")
        y = input("Enter the second operand:")

        if x == 'True':
            x = True
        elif x== 'False':
            x = False

        if y == 'True':
            y = True
        elif y== 'False':
            y = False

        result = logical_and(x, y)
        print("The result is {}".format(result))

    elif opt == '9':
        print("you have selected {}".format(opt))
        x = input("Enter the first operand:")
        y = input("Enter the second operand:")

        if x == 'True':
            x = True
        elif x == 'False':
            x = False

        if y == 'True':
            y = True
        elif y == 'False':
            y = False

        result = logical_or(x, y)
        print("The result is {}".format(result))

    elif opt == '10':
        print("you have selected {}".format(opt))
        x = input("Enter the first operand:")

        if x == 'True':
            x = True
        elif x == 'False':
            x = False

        result = logical_not(x)
        print("The result is {}".format(result))

    else:
        if opt =='q' or opt == 'quit':
            break
        else:
            print("Please try to select from 1-10")

print("Good bye!")








