"""
project: calculator
version 1.

Menu system
1.1 adding
1.2 subtracting
1.3 multiplying
1.4 division
1.5 floor division
1.6 modulus
1.7 exponent
2.1 logical and
2.2 logical or
2.3 logical not

user can choose an operation
    user can perform arithmetic operation
    user can perform logical operation
user can input operand(s) as needed

hints:
function
input()
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
    print("Please try to select from 1-10")

print("Good bye!")








