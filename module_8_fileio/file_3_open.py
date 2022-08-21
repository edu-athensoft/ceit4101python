"""
Module 8:   File I/O
Author:     Athensoft inc.

Open a file at a specified location
on Windows

open() - open a file
close() - close a file
"""

# case 3. open file in specified full path
# different way to represent path in windows system
print("[info] open file in specified full path")
print("[info] opening file_open.txt ...")
f = open("D:/workspace/pycharm201803/ceit4101python/module_8_fileio/file_open.txt")

print("[info] closing ...")
f.close()

print("[info] done.")

