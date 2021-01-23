"""
read big file in chunks
"""

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


# main
filepath = 'file5_mode_r.txt'
read_in_chunks(filepath)
