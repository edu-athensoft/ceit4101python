"""
Module 8:   File I/O
Author:     Athensoft Inc.

Open a file at the same location
open() - open a file
close() - close a file
"""

# case 1. open file in current directory
# print("[info] open file in current directory")
print("[info] opening file_open.txt ...")
f = open("file1_open.txt")

print("[info] closing ...")
f.close()

print("[info] done.")