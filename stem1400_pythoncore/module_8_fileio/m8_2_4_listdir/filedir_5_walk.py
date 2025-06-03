"""
list dir recursively
"""
import os

def tree_printer(root):
    for root, directories, files in os.walk(root):
        print(f"Directory: {root}")
        for directory in directories:
            # print(f"  [DIR] {os.path.join(root, directory)}")
            print(f"  [DIR] {directory}")
        for file in files:
            # print(f"  [FILE] {os.path.join(root, file)}")
            print(f"  [FILE] {file}")

# main
PATH = f"D:\workspace\pycharm201803\ceit4101python\stem1400_pythoncore\module_8_fileio"


if __name__ == "__main__":
    # Prompt the user for a directory path
    target_path = PATH.strip()

    if os.path.exists(target_path):
        tree_printer(target_path)
    else:
        print(f"The path '{target_path}' does not exist.")