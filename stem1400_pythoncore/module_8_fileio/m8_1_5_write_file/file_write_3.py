"""
write content of string by line
"""

with open("file_write_3.txt",'w', encoding='utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n")
   f.write("contains three lines\n")
