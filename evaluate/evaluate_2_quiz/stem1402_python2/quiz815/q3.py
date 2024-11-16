"""
3. Reading a File in Chunks
Write a Python function called read_file_in_chunks
that opens a text file named "pyetl.log" and
reads its contents in chunks of size characters,
where size is provided as an argument to the function.
The function should return a list of strings,
where each string is a chunk of the file's content.
Use the read(size) method in a loop until the entire file is read.
Hint:
Please download the log file pyetl.log
"""
import os

def read_file_in_chunks(file_path, chunk_size=1024*1024):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1M
    You can set your own chunk size
    """
    file_object = open(file_path, mode='rb')
    while True:
        chunk_data = file_object.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data


# main
file_name = 'pyetl.log'
data = read_file_in_chunks(file_name, chunk_size=1024*1024*1)
print(type(data))

count = 0
for chunk in data:
    print("============================")
    # print(chunk)
    count += 1
    print(f"=== block {count} ===")


file_stats = os.stat(file_name)
# print(file_stats)

print(f'File Size in Bytes is {file_stats.st_size}B')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024):.2f}MB')
