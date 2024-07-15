"""
serializing
customized or complex data type
"""

import json
from datetime import datetime

def as_complex(dct):
    if 'time' in dct:
        dct['time'] = datetime.fromisoformat(dct['time'])
    return dct

json_string = '{"name": "Alice", "time": "2023-10-21T10:00:00"}'
data = json.loads(json_string, object_hook=as_complex)
print(data)
