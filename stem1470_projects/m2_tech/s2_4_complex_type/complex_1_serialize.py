"""
serializing
customized or complex data type
"""

import json
from datetime import datetime

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    "name": "Alice",
    "time": datetime.now()
}

json_string = json.dumps(data, cls=ComplexEncoder)
print(json_string)