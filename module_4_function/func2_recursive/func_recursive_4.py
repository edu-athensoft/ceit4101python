"""
recursive function

summary of a sequence of number (integer)

10

"""

def mysum(n):
    if n == 1:
        return 1
    else:
        return mysum(n-1)+n

# main program

result = mysum(100)
print(result)


