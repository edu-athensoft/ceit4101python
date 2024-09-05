"""
write content of string into a text file
"""

# case1. truncates
f = open("file_write_1.txt", 'w')
content = "this is the new content to write"
charnum = f.write(content)
f.close()

print(f"charnum={charnum}")
