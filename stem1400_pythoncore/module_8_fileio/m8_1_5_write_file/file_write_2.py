"""
write content of string into a text file
"""

# case2. create
f = open("file_write_2_new.txt", 'w')

content = "this is the file to create"
charnum = f.write(content)
f.close()

print(f"charnum={charnum}")
