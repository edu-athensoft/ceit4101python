"""
python logging

custom - __main__ logger

logfile default file mode is 'a' (appending)

"""

import logging

# logging settings
logbase = './logs/'
logfile = logbase + 'logging_7_2.log'
logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# my logger
handler = logging.FileHandler(logfile)
formatter = logging.Formatter(logformat)
handler.setFormatter(formatter)

# logger = logging.getLogger()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# test
logger.debug("test the custom logger")
logger.info("test the custom logger")
logger.warning("test the custom logger")
logger.error("test the custom logger")
logger.critical("test the custom logger")