"""
dumps()
convert python object to JSON string

save to file
"""

import json

python_obj = {
    "name": "Alice",
    "age": 25,
    "is_student": False
}

with open('data.json', 'w') as file:
    json.dump(python_obj, file)
