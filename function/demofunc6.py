def my_func():
    # x = 10
    global x
    x = 10
    print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)