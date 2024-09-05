# file io
# reading file

# r, w, a
course_file = open("courses_read.txt", "r")
s = course_file.read()
course_file.close()
print(s)

print("====================")

course_file2 = open("courses_read.txt", "r")
s2 = course_file2.read(10)
course_file2.close()
print(s2)

print("====================")

course_file3 = open("courses_read.txt", "r")
sa = course_file3.readline()
sb = course_file3.readline()
course_file3.close()
print(sa)
print(sb)

print("====================")

course_file4 = open("courses_read.txt", "r")
for line in course_file4:
    print(line, end="")
course_file4.close()


