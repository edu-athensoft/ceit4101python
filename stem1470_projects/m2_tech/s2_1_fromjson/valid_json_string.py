"""
Validating JSON string
"""

import json

json_string = '''
[
    1,
    2,
    3,
    4,
    5,
    "hello",
    null,
    true
]
'''

try:
    json_object = json.loads(json_string)
    print("The string is a valid JSON.")
except json.JSONDecodeError as e:
    print("The string is not a valid JSON.")