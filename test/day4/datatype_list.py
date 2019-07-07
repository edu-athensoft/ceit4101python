# declare list

a = [5,10,15,20,25,30,35,40]

size = len(a)

print(type(size))
print(type("size ="))
print("size ="+str(size))

print(a[0])
print(a[7])

print("a[0:3] = ", a[0:3])

print(a[3:6])  # 20,25,30

print(a[:3])
print(a[6:])

print(a[6:6])
print(a[5:5])
print(a[0:0])

a[0] = 1
print(a)