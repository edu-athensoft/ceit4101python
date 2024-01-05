"""
Problem: Recursive File System Search

Problem Statement
Imagine a file system represented as a tree where each node is either a file or a folder. Each folder can contain
multiple files and/or subfolders. Write a Python function using recursion to search for a specific file name in
this file system tree and return the path to the file if it exists.

The file system is represented as a nested dictionary, where each key-value pair corresponds to a folder or file.
If the value is a dictionary, it represents a folder; if the value is None, it represents a file.

Your task is to implement the function find_file(file_system, file_name) that searches for file_name in file_system
and returns the path to the file as a list of folder names leading to the file, or None if the file does not exist.

"""


def find_file(file_system, file_name, path=None):
    if path is None:
        path = []

    for key, value in file_system.items():
        # Check if the current key is the file we are looking for
        if key == file_name and value is None:
            return path + [key]
        # If it's a directory, search recursively
        elif isinstance(value, dict):
            found_path = find_file(value, file_name, path + [key])
            if found_path:
                return found_path

    # File not found in the current path
    return None


# Sample file system structure
file_system = {
    'Documents': {
        'Photos': None,
        'Projects': {
            'Project1': None,
            'Project2': None
        }
    },
    'Downloads': {
        'Movies': {
            'Inception.mp4': None,
            'Interstellar.mp4': None
        },
        'Music': None
    }
}

# Sample file search
file_name = 'Project1'
print(find_file(file_system, file_name))

file_name = 'Inception.mp4'
print(find_file(file_system, file_name))
