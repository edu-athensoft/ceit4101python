"""
python logging

custom - default logger

logfile default file mode is 'a' (appending)

"""

import logging

# logging settings
logbase = './logs/'
logfile = logbase + 'logging_7_1.log'
logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# my logger
# handler = logging.FileHandler(logfile)
handler = logging.FileHandler(logfile, mode='w')
formatter = logging.Formatter(logformat)
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# test
logger.debug("test the custom logger")
logger.info("test the custom logger")
logger.warning("test the custom logger")
logger.error("test the custom logger")
logger.critical("test the custom logger")