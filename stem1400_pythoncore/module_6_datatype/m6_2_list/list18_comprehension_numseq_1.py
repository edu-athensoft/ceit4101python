"""
生成 0-9 中所有不重复的 3 个数字组合序列

方法 1：使用 itertools.permutations（推荐）
"""
import itertools

# 生成所有 3 个数字的排列组合（顺序不同算不同组合）
all_sequences = list(itertools.permutations(range(10), 3))
print("总组合数:", len(all_sequences))
print("示例组合:", all_sequences[:5])  # 打印前5个组合

