"""
4. Reading the Last n Characters of a File
Write a Python function called read_last_n_characters that opens a text file
named "story.txt" and reads the last n characters, where n is provided as an argument
to the function. You will need to use the seek() method to position the file pointer
before reading the last n characters. Return the string of characters read from the file.
"""

def read_last_n_characters(n):
    try:
        with open("q4_story.txt", "rb", encoding="utf-8") as file:
            # Move to the end of the file and get its size
            file.seek(0, 2)
            file_size = file.tell()
            print(f"file size={file_size}")
            # Ensure `n` does not exceed the file length
            if n > file_size:
                file.seek(0)  # Move to the start if n is larger than the file
                print(f"moved to the start of file")
            else:
                print(f"seeking ...")
                file.seek(-n, 2)  # Seek n characters from the end
                print(f"file pos={file.tell()}")

            # Read and return the last n characters
            # content = file.read().decode("utf-8")
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found"
    except ValueError:
        return "Value error encountered during file read"


# Test case
print(read_last_n_characters(1))


# with open("q4_story.txt", "rb") as file:
#     # Move to the end of the file and get its size
#     file_pos = file.tell()
#     print(file_pos)
#
#     file.seek(0, 2)
#     file_pos = file.tell()
#     print(file_pos)
#
#     file.seek(-10, 2)
#     file_pos = file.tell()
#     print(file_pos)
#
#     content = file.read()
#     print(content)
#     print("----------")
#     print(content.decode("utf-8"))
#     print("----------")