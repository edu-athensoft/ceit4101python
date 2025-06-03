"""
生成 0-9 中所有不重复的 3 个数字组合序列

方法 1：使用 itertools.permutations（推荐）
"""

all_sequences = [
    (i, j, k)
    for i in range(10)
    for j in range(10)
    for k in range(10)
    if i != j and i != k and j != k
]
print("总组合数:", len(all_sequences))
print("示例组合:", all_sequences[:5])  # 打印前5个组合
