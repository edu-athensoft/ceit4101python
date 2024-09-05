"""
demo of lambda

sorting by any specified attribute

sorted()
"""

data = [{"name":"Max","age":6},
        {"name":"Lisa","age":20},
        {"name":"Ben","age":9}]

sorted_by_age = sorted(data, key=lambda item: item["age"])
print(sorted_by_age)

sorted_by_name = sorted(data, key=lambda item: item["name"])
print(sorted_by_name)

