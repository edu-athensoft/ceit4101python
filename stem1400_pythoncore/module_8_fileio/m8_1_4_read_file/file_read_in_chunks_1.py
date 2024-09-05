"""
read big file in chunks
"""

import os

def read_in_chunks(file_path, chunk_size=1024*1024):
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
file_name = 'video.MP4'
data = read_in_chunks(file_name, chunk_size=1024*1024*10)
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
