"""
生成 0-9 中所有不重复的 3 个数字组合序列

方法 3：递归生成（通用性强）
"""

def generate_sequences(length, digits=range(10), current=[]):
    if len(current) == length:
        return [tuple(current)]
    sequences = []
    for d in digits:
        if d not in current:  # 确保不重复
            sequences += generate_sequences(length, digits, current + [d])
    return sequences

all_sequences = generate_sequences(3)
print("总组合数:", len(all_sequences))
print("示例组合:", all_sequences[:50])  # 打印前5个组合


"""
详细解释
1. itertools.permutations（最佳方法）
功能：生成所有长度为 3 的排列，顺序不同视为不同组合（如 (1,2,3) 和 (3,2,1) 算两个组合）。

参数：

range(10)：数字池（0-9）

3：组合长度

输出：共 10 × 9 × 8 = 720 个组合。

优点：高效、代码简洁，直接利用标准库。

2. 列表推导式
逻辑：三层循环遍历所有可能的 (i,j,k)，通过条件 i != j != k 排除重复数字。

输出：同样生成 720 个组合。

缺点：代码嵌套较深，性能略低于 itertools。

3. 递归生成
逻辑：递归构建组合，逐步添加不重复的数字。

优点：灵活，可轻松修改为其他组合长度或数字池。

缺点：递归深度受限，可能栈溢出（但本题组合数较少无风险）。

关键概念
排列 (Permutation)

顺序敏感，(1,2,3) ≠ (3,2,1)。

数学公式：P(10,3) = 10! / (10-3)! = 720。

不重复约束

每个数字在组合中仅出现一次，通过 if d not in current 或 itertools 自动处理。

"""

