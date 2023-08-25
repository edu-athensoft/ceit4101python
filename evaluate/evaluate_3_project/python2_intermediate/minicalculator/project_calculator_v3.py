"""
project: calculator
version 3.

to optimize the current program
refine

refactor, refactoring
keep the features and functions unchanged
upgrade or optimize the code

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

def logical_or(x, y):
    return x or y

def logical_not(x):
    return not x

def str2bool(x):
    if x == 'True':
        x = True
    elif x == 'False':
        x = False
    return x

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

        x = str2bool(x)
        y = str2bool(y)

        result = logical_and(x, y)
        print("The result is {}".format(result))

    elif opt == '9':
        print("you have selected {}".format(opt))
        x = input("Enter the first operand:")
        y = input("Enter the second operand:")

        x = str2bool(x)
        y = str2bool(y)

        result = logical_or(x, y)
        print("The result is {}".format(result))

    elif opt == '10':
        print("you have selected {}".format(opt))
        x = input("Enter the first operand:")

        x = str2bool(x)

        result = logical_not(x)
        print("The result is {}".format(result))

    else:
        if opt =='q' or opt == 'quit':
            break
        else:
            print("Please try to select from 1-10")

print("Good bye!")








