"""
An example of all data type contained in JSON string
"""

import json

json_string = '''{
    "name": "Alice",
    "age": 25,
    "is_student": false,
    "courses": ["Math", "Science"],
    "address": null,
    "scores": {
        "Math": 95,
        "Science": 90
    },
    "graduated": false
}'''

# Decode the JSON string to a Python object
data = json.loads(json_string)
print("Decoded Python object:")
print(data)



