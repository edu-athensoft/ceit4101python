"""
python dir

Making a New Directory
"""

import os

d1 = os.getcwd()
print(d1)

# Making a New Directory

# not safe
# os.mkdir('test_dir')

# safe
if not os.path.exists('test_dir'):
    os.makedirs('test_dir')


listdir = os.listdir(d1)
print(listdir)

