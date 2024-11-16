"""
此函数和 dump() 函数相对应，用于将二进制对象文件转换成 Python 对象。该函数的基本语法格式为：
load(file, *, fix_imports=True, encoding='ASCII', errors='strict')

其中，file 参数表示要转换的二进制对象文件（必须以 "rb" 的打开方式操作文件），
其它参数只是为了兼容 Python 2.x 版本而保留的参数，可以忽略。

看似强大的 pickle 模块，其实也有它的短板，即 pickle 不支持并发地访问持久性对象，在复杂的系统环境下，
尤其是读取海量数据时，
使用 pickle 会使整个系统的I/O读取性能成为瓶颈。这种情况下，可以使用 ZODB。

ZODB 是一个健壮的、多用户的和面向对象的数据库系统，专门用于存储 Python 语言中的对象数据，
它能够存储和管理任意复杂的 Python 对象，并支持事务操作和并发控制。并且，ZODB 也是在 Python
的序列化操作基础之上实现的，因此要想有效地使用 ZODB，必须先学好 pickle。
"""

import pickle

with open ("data.bin", 'rb') as f: #打开文件
    t3 = pickle.load(f) #将二进制文件对象转换成 Python 对象
    print(t3, type(t3))




