"""
获取所有'A'元素的索引列表
"""


def get_index1(lst=None, item=''):
    tmp = []
    tag = 0
    for i in lst:
        if i == item:
            tmp.append(tag)
            tag += 1
        return tmp


lst = ['A', 1, 4, 2, 'A', 3]
print(get_index1(lst, 'A'))
# [0, 4]
