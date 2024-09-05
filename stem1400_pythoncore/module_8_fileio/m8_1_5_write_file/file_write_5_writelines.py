"""
write lines
"""

data = ["my first file\n", "This file\n", "contains three lines\n"]

with open("file_write_5.txt",'w', encoding='utf-8') as f:
   f.writelines(data)
