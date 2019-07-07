# multi-line comment

"""alksdjfksafasldfsakdf
asdlflsadfkdsajf
asdljflsadjflas
asldfjalsdf"""

#

def myfunction():
    """this is a docstring of myfunction"""
    # this is a docstring of myfunction
    print("hello")


print(myfunction.__doc__)
myfunction()