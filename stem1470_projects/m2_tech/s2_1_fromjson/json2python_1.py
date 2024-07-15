"""
convert JSON string to python object
"""

import json

json_string = '{"name": "Alice", "age": 25, "is_student": false}'
python_obj = json.loads(json_string)

print(python_obj)
# output: {'name': 'Alice', 'age': 25, 'is_student': False}

print(type(python_obj))
# output: <class 'dict'>
