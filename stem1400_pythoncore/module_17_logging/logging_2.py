"""
file logging
"""

import logging

logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# set level
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# set formatter
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s');
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# add handler
logger.addHandler(stream_h)
logger.addHandler(file_h)


# test
logger.warning("a warning message")
logger.error("an error message")
