"""
方法三：借助range函数遍历获取
"""

def get_index3(lst=None, item=''):
    return [i for i in range(len(lst)) if lst[i] == item]


lst = ['A', 1, 4, 2, 'A', 3]

print(get_index3(lst, 'A'))

