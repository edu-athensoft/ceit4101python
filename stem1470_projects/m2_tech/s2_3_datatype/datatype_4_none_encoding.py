"""
Encoding a Python object containing None data to JSON

python object: None
JSON string: null
"""

import json

# Define a Python object containing None data
data = {
    "name": "Alice",
    "age": None,
    "is_student": False
}

# Encode the Python object to a JSON string
json_string = json.dumps(data, indent=4)
print("JSON encoded string:")
print(json_string)




