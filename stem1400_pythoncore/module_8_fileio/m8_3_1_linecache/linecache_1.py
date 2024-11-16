"""
下面程序示范了使用 linecache 模块来随机读取指定行：
"""

import linecache
import random

# 读取random模块的源文件的第3行
print(linecache.getline(random.__file__, 18))

# 读取本程序的第3行
print(linecache.getline('linecache_1.py', 12))

# 读取普通文件的第2行
# line no starts from 1, not 0
print(linecache.getline('data.txt', 1), end="")
print(linecache.getline('data.txt', 2), end="")
print(linecache.getline('data.txt', 3), end="")