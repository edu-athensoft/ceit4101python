# try except

try:
    value = 10/0
except ZeroDivisionError:
    print("ZeroDivisionError")


try:
    value = 10/0
except ZeroDivisionError as err:
    print(err)


try:
    number = int(input("Enter a number"))
    print(number)
except ValueError:
# except:
    print("Invalid input")
