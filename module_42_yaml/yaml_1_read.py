"""
logging

dictConfig
config in YAML

note: must install yaml module
"""

import yaml

# run once at startup
with open('config/logging.yaml') as fin:
    # content = fin.read()
    # conf = yaml.load(content, Loader=yaml.FullLoader)
    conf = yaml.load(fin, Loader=yaml.FullLoader )

print(type(conf))
print(conf)

