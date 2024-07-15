"""
parameters
1. indent
json_string = json.dumps(python_obj, indent=4)

2. separators
json_string = json.dumps(python_obj, separators=(',', ':'))

3. sort_keys
json_string = json.dumps(python_obj, sort_keys=True)

4. ensure_ascii
json_string = json.dumps(python_obj, ensure_ascii=False)
"""

import json

python_obj = {
    "name": "Alice",
    "age": 25,
    "is_student": False
}

print("Python object to JSON string Parameter")
print("0. origin")
json_string = json.dumps(python_obj)
print(json_string)
print()

print("1. indent=2")
json_string = json.dumps(python_obj, indent=2)
print(json_string)
print()

print("2. separators=(',', '->')")
json_string = json.dumps(python_obj, separators=(',', '->'))
print(json_string)
print()

print("3. sort_keys=True")
json_string = json.dumps(python_obj, sort_keys=True)
print(json_string)
print()

print("4. ensure_ascii=False")
json_string = json.dumps(python_obj, ensure_ascii=False)
print(json_string)
print()
