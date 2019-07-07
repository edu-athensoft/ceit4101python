x1 = 5
y1 = 5

print(x1 is y1 )
print(x1 is not y1 )

t1 = (2,3,4)
t2 = (2,3,4)

print(t1 is t2)
print(t1 is not t2)

d1 = {"k1":"v1", "k2":"v2"}
d2 = {"k1":"v1", "k3":"v2"}
print(d1 is d2)


list_1 = [1,2,3,4,5,6]
list_2 = [1,'d','4',4,6,2,8]
print(7 in list_1)
print(6 not in list_1)


y = {1:'a',2:'b'}
# Output: False
print('a' in y)
print(1 in y)