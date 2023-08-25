"""
c7.1.5
print(flush=False|True)
output to a file

reference: https://blog.csdn.net/Granthoo/article/details/82880562

IMPORTANT!  please try this in the interactive mode
"""

# flush=True
f = open("456.txt", "w")
print("123456789", file = f, flush=True)