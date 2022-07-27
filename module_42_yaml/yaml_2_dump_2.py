"""
logging

dictConfig
config in YAML

note: must install yaml module
"""

import yaml


# dict
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
    },
    'loggers': {
        'root': { # root logger
            'handlers': [ 'default' ],
            'level': 'WARNING',
            'propagate': False
        },
        'my.packg': {
            'handlers': [ 'default' ],
            'level': 'INFO',
            'propagate': False
        },
        '__main__': { # if __name__ == '__main__'
            'handlers': [ 'default' ],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

content = yaml.dump(LOGGING_CONFIG)
print(content)

with open('./config/config.yaml', mode='w') as fout:
    fout.write(content)

