"""
convert python object to JSON string
"""

import json

python_obj = {
    "name": "Alice",
    "age": 25,
    "is_student": False
}

json_string = json.dumps(python_obj)
print("Python object to JSON string")
print(json_string)
# output: {"name": "Alice", "age": 25, "is_student": false}
print()

# output formatting, indentation
json_string_pretty = json.dumps(python_obj, indent=4)
print("Python object to JSON string")
print(json_string_pretty)
