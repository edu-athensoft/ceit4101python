# continue

# case 1
# for i in range(10):
#     if i == 8:
#         continue
#     print("i = {}".format(i))
#
# print("program ends")


# case 2
# for i in range(10):
#     print("i = {}".format(i))
#     if i == 8:
#         continue
#
# print("program ends")


# case 3
i = 0
while i < 10:
    if i == 8:
        continue
    print("i = {}".format(i))
    i += 1

print("program ends")