"""
python dir

Changing Directory
"""

import os

d1 = os.getcwd()
print(d1)

# change dir
os.chdir('/')

d2 = os.getcwd()
print(d2)