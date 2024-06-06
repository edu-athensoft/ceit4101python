"""
7. Write a program to count target elements in a list.
my_list = [3, [8, 1, 6], [0, 8], [4, 8, 9, 8]]
"""

my_list = [3, [8, 1, 6], [0, 8], [4, 8, 9, 8]]

target = 8
count = 0
row_len = len(my_list)

for i in range(row_len):

    if isinstance(my_list[i], list):
        col_len = len(my_list[i])
        for j in range(col_len):
            if my_list[i][j] == target:
                count += 1
    else:
        if my_list[i] == target:
            count += 1

print(count)
