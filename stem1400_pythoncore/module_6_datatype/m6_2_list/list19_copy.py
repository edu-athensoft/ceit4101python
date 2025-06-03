"""
deep copy and shallow copy
"""

import copy

# 原始对象：一个嵌套列表
original = [[1, 2], [3, 4]]

# 浅拷贝
shallow = copy.copy(original)

# 深拷贝
deep = copy.deepcopy(original)

# 修改原始对象中的子元素
original[0][0] = 99

print("Original:", original)   # [[99, 2], [3, 4]]
print("Shallow:", shallow)     # [[99, 2], [3, 4]] → 子元素引用的是同一个
print("Deep:", deep)           # [[1, 2], [3, 4]] → 完全独立的对象
