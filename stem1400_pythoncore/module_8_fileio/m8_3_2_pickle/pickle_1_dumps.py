"""
pickle 模块提供了以下 4 个函数供我们使用：

其中 dumps 和 loads 实现基于内存的 Python 对象与二进制互转；
dumps()：将 Python 中的对象序列化成二进制对象，并返回；
loads()：读取给定的二进制对象数据，并将其转换为 Python 对象；

dump 和 load 实现基于文件的 Python 对象与二进制互转。
dump()：将 Python 中的对象序列化成二进制对象，并写入文件；
load()：读取指定的序列化数据文件，并返回对象。
"""

"""
此函数用于将 Python 对象转为二进制对象
dumps(obj, protocol=None, *, fix_imports=True)

此格式中各个参数的含义为：
obj：要转换的 Python 对象；
protocol：pickle 的转码协议，取值为 0、1、2、3、4，其中 0、1、2 对应 Python 早期的版本，
3 和 4 则对应 Python 3.x 版本及之后的版本。未指定情况下，默认为 3。
其它参数：为了兼容 Python 2.x 版本而保留的参数，Python 3.x 中可以忽略。
"""

import pickle

tup1 = ('I love Python', {1,2,3}, None)

#使用 dumps() 函数将 tup1 转成 p1
p1 = pickle.dumps(tup1)
print(p1)


