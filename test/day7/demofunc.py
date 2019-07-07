import math

def helloKitty():
    # print("Hello")
    bb = 35
    print(bb, math.pi)
    return 99

def helloPikachu():
    # print("Hello")
    bb = 45
    print(bb, math.pi)
    return 99

helloKitty()
helloPikachu()


helloKitty()

a = helloKitty()

# Output: Hello
print(a)

a = helloKitty
a()
a()
a()


def testfunc(number):
    print("test function:()", number)

testfunc(1)
testfunc(2)

testfunc(a)