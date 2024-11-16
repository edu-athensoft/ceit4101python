"""
此函数用于将 Python 对象转换成二进制文件，其基本语法格式为：
dump (obj, file,protocol=None, *, fix mports=True)

其中各个参数的具体含义如下：
obj：要转换的 Python 对象。
file：转换到指定的二进制文件中，要求该文件必须是以"wb"的打开方式进行操作。
protocol：和 dumps() 函数中 protocol 参数的含义完全相同，因此这里不再重复描述。
其他参数：为了兼容以前 Python 2.x版本而保留的参数，可以忽略。
"""

import pickle
tup1 = ('I love Python', {1,2,3}, None)

#使用 dumps() 函数将 tup1 转成 p1
with open ("data.bin", 'wb') as f: #打开文件
    pickle.dump(tup1, f) #用 dump 函数将 Python 对象转成二进制对象文件


# 运行完此程序后，会在该程序文件同级目录中，生成 a.txt 文件，但由于其内容为二进制数据，因此直接打开会看到乱码。


# test
print("reading file...")
with open("data.bin", 'rb') as f2:
    content = f2.read()
    print(content)