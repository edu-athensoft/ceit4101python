"""
read lines of small files
"""

filepath = 'file5_mode_r.txt'
f = open(filepath,'rb')
data = f.readlines()
# read line 1 to 10
print(data[0:10])