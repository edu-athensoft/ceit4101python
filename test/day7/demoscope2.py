def outer_func():
    a = 20

    def inner_func():
        a = 30
        print('a=', a)

    inner_func()
    print('a=', a)


a = 10
outer_func()
print("a=", a)


