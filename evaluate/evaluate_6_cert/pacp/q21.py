"""
A. Yes, and it can differentiate its behavior between the regular launch and import. ✅（正确）
解释：
在 Python 中，每个模块（*.py 文件）都可以被 直接运行 或 被导入。Python 提供了 __name__ 变量来区分这两种情况：

如果模块是直接运行的（作为主程序）： __name__ == "__main__"
如果模块是被导入的： __name__ 的值是模块的文件名（不带 .py）

# example.py
def hello():
    print("Hello from example.py")

if __name__ == "__main__":
    print("This module is running as the main program")
    hello()


执行 python example.py，输出：
This module is running as the main program
Hello from example.py


如果在另一个 Python 文件中导入
import example

输出
（无输出）

说明 if __name__ == "__main__" 保护了 hello() 这部分代码，使其不会在被导入时执行。
这证明 模块可以像普通代码一样运行，并且可以区分是直接执行还是被导入。

"""

