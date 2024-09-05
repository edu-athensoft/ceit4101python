"""
read specified lines
"""

def read_file_lines(file_path, line_from=1, line_to=-1):
    content_list = list()
    i = 1
    f = open(file_path)
    for line in f:
        if line_to != -1:
            if line_from <= i <= line_to:
                content_list.append(line[:-1])
        else:
            if i >= line_from:
                content_list.append(line[:-1])

        i += 1
    return content_list


# main
filepath = 'file_readline.txt'
content = read_file_lines(filepath, line_from=2, line_to=4)
print(content)