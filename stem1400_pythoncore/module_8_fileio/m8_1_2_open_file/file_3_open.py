"""
Module 8:   File I/O
Author:     Athensoft inc.

Open a file with a relative path
on Windows

open() - open a file
close() - close a file
"""

# case 3. open file in specified full path
# different way to represent path in windows system
print("[info] open file with a relative path")
print("[info] opening file3_open.txt ...")
# f = open("/stem1400_modules/module_8_fileio/file_open.txt")
f = open("../mydocs/file3_open.txt")

print("[info] closing ...")
f.close()

print("[info] done.")

