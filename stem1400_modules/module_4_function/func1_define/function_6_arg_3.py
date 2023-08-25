"""
function argument

multiple parameters and arguments


"""

def adding(x, y):
    z = x + y
    return z


def adding(x, y, z):
    sum = x + y + z
    return sum

# adding n1 and n2
n1 = 10
n2 = 20
result = adding(n1, n2)
# print("adding n1:{n1} and n2:{n2} = {res}".format(n1=n1, n2=n2, res = result))
print("{n1} + {n2} = {res}".format(n1=n1, n2=n2, res = result))


# adding n1, n2, n3


