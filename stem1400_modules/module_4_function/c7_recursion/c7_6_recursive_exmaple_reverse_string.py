"""
Reverse string
"""


def reverse(mystr):
    if len(mystr) == 1:
        return mystr

    return reverse(mystr[1:]) + mystr[0]


# main
print(reverse('ward'))
