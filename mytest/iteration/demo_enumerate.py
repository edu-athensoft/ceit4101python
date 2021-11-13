"""
enumerate()

using enumerate() instead of range(len())

"""

data = [1,2,3,4,5,6]
for index, num in enumerate(data):
    print(f"value={data[index]}, value={num}, index={index}")
