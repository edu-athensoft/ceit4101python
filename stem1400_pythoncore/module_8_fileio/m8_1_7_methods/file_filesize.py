"""
python

get file size

https://www.digitalocean.com/community/tutorials/how-to-get-file-size-in-python
"""

import os

# main
file_name = 'video.MP4'
file_stats = os.stat(file_name)
print(file_stats)
print(f'File Size in Bytes is {file_stats.st_size}B')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024):.2f}MB')

