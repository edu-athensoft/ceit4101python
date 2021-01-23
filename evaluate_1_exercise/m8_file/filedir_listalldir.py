"""
How to list all directories and files with subdirectories under specified directory?
"""


import os


def printlist(mylist):
    for i in mylist:
        print(i)


def showdir(dirname, level=0):
    dir_list = os.listdir(dirname)
    # printlist(dir_list)
    for name in dir_list:
        print(f'{"   "*level}\u2515 {name}')
        if os.path.isdir(dirname+os.sep+name):
            level += 1
            showdir(dirname+os.sep+name, level)
            level -= 1

start_path = os.getcwd()+os.sep+'dirtest'
start_path = '.'
showdir(start_path)

# print(type(result))

# printlist(result)


