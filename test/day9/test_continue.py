
for i in range(20):
    print("turn #", i)
    for x in range(10):
        if x==5:
            continue

        print(x, 'inner loop')


