"""
logging
"""

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s- %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

string_msg = "logging message"
logging.debug(string_msg)
logging.info(string_msg)
logging.warning(string_msg)
logging.error(string_msg)
logging.critical(string_msg)
