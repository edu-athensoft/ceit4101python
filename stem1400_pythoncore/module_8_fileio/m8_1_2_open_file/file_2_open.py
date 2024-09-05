"""
Module 8:   File I/O
Author:     Athensoft Inc.

Open a file with an absolute path
on Windows

open() - open a file
close() - close a file
"""

# case 2. open file in specified full path
print("[info] open file with an absolute path")
print("[info] opening file2_open.txt ...")
f = open("D:\\workspace\\pycharm201803\\ceit4101python\\module_8_fileio\\file2_open.txt")

print("[info] closing ...")
f.close()

print("[info] done.")