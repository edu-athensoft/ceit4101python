# read multiple lines
def read_in_chunks(file_path, chunk_size=1024*1024):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1M
    You can set your own chunk size
    """
    file_object = open(file_path)
    while True:
        chunk_data = file_object.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data


def read_file_lines(file_path, line_start=1, line_end=-1):
    content_list = list()
    i = 1
    for chunk in read_in_chunks(file_path, 1024*1024*10):
        for tmp in chunk.split('\n'):
            if line_end != -1:
                if i >= line_start and i <= line_end:
                    content_list.append(tmp)
            else:
                if i >= line_start:
                    content_list.append(tmp)
            i += 1
    return content_list


# main
filepath = 'file5_mode_r.txt'
content = read_file_lines(filepath, line_start=2, line_end=4)
print(content)