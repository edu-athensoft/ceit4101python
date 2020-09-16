"""
function docstring

docstring with auto-complete function


"""

def adding(x, y):
    """
    adding two numbers
    :param x: the first number (n1)
    :param y: the second number (n2)
    :return: the sum of n1 and n2
    """
    z = x + y
    return z


def adding(x, y, z):
    """

    :param x:
    :param y:
    :param z:
    :return:
    """
    sum = x + y + z
    return sum


# adding n1 and n2
n1 = 10
n2 = 20
result = adding(n1, n2)

# print("adding n1:{n1} and n2:{n2} = {res}".format(n1=n1, n2=n2, res = result))
print("{n1} + {n2} = {res}".format(n1=n1, n2=n2, res = result))


# adding n1, n2, n3



