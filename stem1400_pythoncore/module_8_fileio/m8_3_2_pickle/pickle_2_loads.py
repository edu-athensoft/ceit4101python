"""
此函数用于将二进制对象转换成 Python 对象，其基本格式如下：
loads(data, *, fix_imports=True, encoding='ASCII', errors='strict')
"""

import pickle
tup1 = ('I love Python', {1,2,3}, None)
p1 = pickle.dumps(tup1)

#使用 loads() 函数将 p1 转成 Python 对象
t2 = pickle.loads(p1)

print(t2)

