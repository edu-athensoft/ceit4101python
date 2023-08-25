# Program to add natural
# numbers upto
# sum = 1+2+3+...+n
# avoid magic value
# flexible

n = 150
i = 1
summary = 0
while i <= n:
    summary += i
    i += 1

print("the result is {}".format(summary))
