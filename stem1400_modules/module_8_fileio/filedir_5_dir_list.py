"""
python dir

Changing Directory
"""

import os

d1 = os.getcwd()
print(d1)

# change dir
os.chdir('/')

# case 1. list in current direction
dirlist = os.listdir()
print(dirlist)

# case 2. list in specified direction
sourcedir = 'D:\\workspace\\pycharm201803\\ceit4101python\\module_8_fileio'
dirlist = os.listdir(sourcedir)
print(dirlist)


