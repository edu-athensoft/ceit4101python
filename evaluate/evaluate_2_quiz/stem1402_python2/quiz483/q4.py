"""
 4. Write a program to swap two given values in a tuple and the
 values are not necessarily in the same data type.
 Hints: Output of the result is required
"""

# my_tuple = (1, '2')
#
# def swap(x):
#     """"""
#     return x[1],x[0]
#
# print(swap(my_tuple))



# test
data = [1, '2', 3, '4']

data[0],data[-1]= data[-1],data[0]
print(data)

# swap two element by given indices
swap_tuple = lambda tpl, i, j: tuple(tpl[j] if idx == i else tpl[i] if idx == j else val for idx, val in enumerate(tpl))

#
t = (1, 2, 3, 4, 5)
swapped_t = swap_tuple(t, 1, 3)  # 交换索引 1 和 3
print(swapped_t)  # 输出: (1, 4, 3, 2, 5)

# ------------------------------------

def swap_tuple(tpl, i, j):
    new_tuple = []  # 创建一个新的列表来存储交换后的值
    for idx, val in enumerate(tpl):  # 遍历元组的索引和对应的值
        if idx == i:
            new_tuple.append(tpl[j])  # 如果当前索引是 i，则放入 j 位置的值
        elif idx == j:
            new_tuple.append(tpl[i])  # 如果当前索引是 j，则放入 i 位置的值
        else:
            new_tuple.append(val)  # 其他索引的值保持不变
    return tuple(new_tuple)  # 转换为元组并返回

# test
my_tuple = (1, 2, 3, 4, 5)
swapped_tuple = swap_tuple(my_tuple, 1, 3)
print(swapped_tuple)  # output: (1, 4, 3, 2, 5)





#
my_tuple = (1, '2')

swap = lambda x: (x[1], x[0])

print(swap(my_tuple))

