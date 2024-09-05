# break - jump out of for loop

# case 1
for i in range(10):
    if i == 8:
        break
    print("i = {}".format(i))

print("program ends")


# case 2
for i in range(10):
    print("i = {}".format(i))
    if i == 8:
        break

print("program ends")


# break - jump out of while loop
# case 3
i = 0
while i < 10:
    if i == 8:
        break
    print("i = {}".format(i))
    i += 1

print("program ends")


# case 4
i = 0
while i < 10:
    print("i = {}".format(i))
    if i == 8:
        break
    i += 1
print("program ends")