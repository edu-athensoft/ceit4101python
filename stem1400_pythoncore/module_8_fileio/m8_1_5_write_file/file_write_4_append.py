"""
appending text content
"""

with open("file_write_4.txt",'a', encoding='utf-8') as f:
   f.write("[info]system responded at 19:00 on 2024-09-01\n")
   f.write("[info]system responded at 19:20 on 2024-09-01\n")
   f.write("[info]system responded at 19:10 on 2024-09-03\n")

