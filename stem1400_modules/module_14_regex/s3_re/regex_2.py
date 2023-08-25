"""
regex
re.findall()

Calculating average score
"""

import re

mystr = """
zhangsan 100
lisi 90
wangwu 80
zhaosi 85
"""
pattern = r"\d+"

results = re.findall(pattern, mystr)

total = 0
for item in results:
    print(item)
    total += int(item)

num = len(results)
print(f"total is {total}")

avg = total/num
print(f"average score is {avg}")

