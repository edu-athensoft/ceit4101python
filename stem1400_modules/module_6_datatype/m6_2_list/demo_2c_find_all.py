"""
find the 2nd target
"""


def find_index(lst, element, start=0, indices=None):
    if indices is None:
        indices = []
    # 递归终止条件：当起始索引超过列表长度时
    if start >= len(lst):
        return indices
    # 如果找到元素，将其索引添加到indices列表中
    if lst[start] == element:
        indices.append(start)
    # 递归调用，增加start索引
    return find_index(lst, element, start + 1, indices)


# Example usage
numbers = [3, 8, 1, 6, 0, 8, 4, 8, 9, 8]
target = 8
print(find_index(numbers, target))

