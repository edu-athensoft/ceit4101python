"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
3.  Write a program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary (n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

Hints:

"""

# n = 5
#
# mydict = {}
#
# for i in range(1,n+1):
#     mydict[i] = i*i
#
# print(mydict)


def getdict(n):
    mydict = {}
    for i in range(1,n+1):
        mydict[i] = i*i
    return mydict


print(getdict(5))
print(getdict(9))
