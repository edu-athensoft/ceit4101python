"""
logging

dictConfig
config in YAML

note: must install yaml module
"""

import logging
from logging.config import dictConfig

import yaml

# run once at startup
with open('config/logging.yaml') as fin:
    conf = yaml.load(fin, yaml.FullLoader)

dictConfig(conf)

# include in each module
log = logging.getLogger(__name__)
log.debug("Logging is configured.")
log.info("Logging is configured.")
log.warning("Logging is configured.")
log.error("Logging is configured.")
log.critical("Logging is configured.")

