"""
string method - partition()

string.partition(separator)

"""

str1 = "Python is easy"

res = str1.partition('is ')
print(res)

res = str1.partition('is')
print(res)

# 'Python ', 'is', ' easy'
# 'Python', 'is', 'easy'
mylist = list(res)
print(mylist)

for i in range(len(mylist)):
    # print(mylist[i])
    mylist[i] = mylist[i].strip()

print(tuple(mylist))








