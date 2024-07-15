"""
convert JSON string to python object
loading JSON file
"""

import json

with open('data.json', 'r') as file:
    python_obj = json.load(file)

print(python_obj)
