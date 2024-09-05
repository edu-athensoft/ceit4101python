"""
Mode	Description
'r'	    Open a file for reading. (default)
'w'	    Open a file for writing.
        Creates a new file if it does not exist or truncates the file if it exists.
'x'	    Open a file for exclusive creation.
        If the file already exists, the operation fails.
'a'	    Open for appending at the end of the file without truncating it.
        Creates a new file if it does not exist.
't'	    Open in text mode. (default)
'b'	    Open in binary mode.
'+'	    Open a file for updating (reading and writing)
"""

# demo
# 1st. create file and the file does not exist before creating
f = open("file7_mode_x.txt", 'x')

content = "this is the new content to write"
charnum = f.write(content)
f.close()

print(f"charnum={charnum}")


# 2nd. try to create another time and an error occurs
try:
    f = open("file7_mode_x.txt", 'x')

    content = "this is the new content to write"
    charnum = f.write(content)
    # f.close()

    print(f"charnum={charnum}")
except Exception as e:
    print(e)
finally:
    f.close()


