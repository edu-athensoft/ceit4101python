"""
c7.1.5
print(flush=False|True)
output to a file

reference: https://blog.csdn.net/Granthoo/article/details/82880562

IMPORTANT!  please try this in the interactive mode
"""

# flush=False
f = open("123.txt", "w")
print("123456789", file = f)
# f.close()