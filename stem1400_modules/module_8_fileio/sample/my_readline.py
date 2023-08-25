f = open("file5_mode_r.txt", 'r')

# readline
# read the first line

while True:
    line = f.readline()
    if line:
        print(line, end="")
    else:
        break

f.close()