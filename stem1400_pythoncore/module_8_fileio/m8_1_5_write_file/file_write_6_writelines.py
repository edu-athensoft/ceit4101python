"""
write lines
"""

data = ["the first line", "the second line", "the third line"]
with open("file_write_6.txt",'w', encoding='utf-8') as f:
   f.writelines(data)
