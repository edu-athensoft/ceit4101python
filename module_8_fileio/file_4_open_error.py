"""
python file I/O

Opening Files
open()

first look

"""

# case 4. open file which does not exist
# error occurs
print("[info] open file in specified full path")
print("[info] opening file_open.txt ...")

# FileNotFoundError: [Errno 2] No such file or directory:
f = open("D:/workspace/pycharm201803/ceit4101python/module_8_fileio/file_not_exist.txt")

print("[info] closing ...")
f.close()

print("[info] done.")

