# create a list

a = []
print(a,type(a))
# print(a[0])  # IndexError


b = [1,2,3,4,5,6]
print(b,type(b))
print(b[0], b[5], b[len(b)-1],'\n')


c = [1,2,3,'a','b','c', 1.0, 2.3, 5.6]
print(c,type(c))
print(c[4], "\n")


d = [1, 2, 3, 7, 8, 9, ['a','b','c']]
print(d,type(d))
# print(d[6],"\n")
# temp_c = d[6]
# print(temp_c[1],"\n")
print(d[6][1],"\n")


e = [1,2,3,b,8,9,['a','b','c']]
print(e,type(e))
# get 6




