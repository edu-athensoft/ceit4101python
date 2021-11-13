"""
merge dict(s)
"""

dict1 = {"k1":"v1","k2":"v2"}

dict2 = {"k3":"v3","k4":"v4"}

dict3 = {**dict1, **dict2}
print(dict3)