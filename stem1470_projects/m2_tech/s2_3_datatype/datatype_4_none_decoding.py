"""
Decoding a JSON string containing null data to a Python object

JSON string: null
python object: None
"""

import json

# Define a JSON string containing null data
json_string = '''
{
    "name": "Alice",
    "age": null,
    "is_student": false
}
'''

# Decode the JSON string to a Python object
data = json.loads(json_string)
print("Decoded Python object:")
print(data)
