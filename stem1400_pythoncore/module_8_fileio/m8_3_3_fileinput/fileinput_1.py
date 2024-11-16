"""
fileinput 模块提供了 input 函数，可以把多个输入流合并在一起，该函数的语法格式如下：
fileinput.input（files="filename1, filename2, ...", inplace=False, backup='', bufsize=0, mode='r', openhook=None）

fileinput.filename()	返回正在读取的文件的文件名。
fileinput.fileno()	返回当前文件的文件描述符（file descriptor），该文件描述符是一个整数。
fileinput.lineno()	返回当前读取的行号。
fileinput.filelineno()	返回当前读取的行在其文件中的行号。
fileinput.isfirstline()	返回当前读取的行在其文件中是否为第一行。
fileinput.isstdin()	返回最后一行是否从 sys.stdin 读取。程序可以使用“-”代表从 sys.stdin 读取。
fileinput.nextfile()	关闭当前文件，开始读取下一个文件。
fileinput.close()	关闭 FileInput 对象。
"""

# 下面程序示范了使用 fileinput 模块来读取以上 2 个文件：
import fileinput

# 一次读取多个文件
last_file = 'data1.txt'
for line in fileinput.input(files=('data1.txt', 'data2.txt')):
    # 输出文件名，当前行在当前文件中的行号
    if fileinput.filename() != last_file:
        print()
    print(fileinput.filename(), fileinput.filelineno(), line, end="")
    last_file = fileinput.filename()

# 关闭文件流
fileinput.close()

