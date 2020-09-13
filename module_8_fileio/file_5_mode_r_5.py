"""
read files in multiply way
https://zhuanlan.zhihu.com/p/87789408

更好的按行读取文件的方式是**for line in open('file')**，
不用刻意使用readline()等函数去读取。

它每次只读一行到内存，
在需要读下一行的时候再去文件中读取，
直到读完整个文件也都只占用了一行数据的内存空间。

上面的print()设置了end=''，因为读取每一行时会将换行符也读入，
而print默认是自带换行符的，所以这里要禁止print的终止符，否则每一行后将多一空行。
"""




for line in open('file5_mode_r.txt'):
    print(line, end='')

print()

"""
这种一次性全部读取的方式在大多数情况下并非良方，
如果是一个大文件，它会占用大量内存，甚至可能会因为内存不足而读取失败。

但并非必须要选择for line in open('a.txt')的方式，
因为有些时候必须加载整个文件才能进行后续的操作，
比如要排序文件，必须要拥有文件的所有数据才能进行排序。

而且对于小文件来说，一次性读取到一个列表中操作起来可能会更加方便，
因为列表对象有很多好用的方法。
所以，不能一概而论地选择for line in open('a.txt')。
"""

for line in open('file5_mode_r.txt').readlines():
    print(line, end='')