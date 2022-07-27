"""
python logging

FileHandler
SteamHandler

"""

import logging

# logging files
logbase = './logs/'
logfile = logbase + 'logging_7_3.log'

# formatter
logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(logformat)

# file handler
fileHandler = logging.FileHandler(logfile, mode='w')
fileHandler.setFormatter(formatter)

# steam handler
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)

# logger = logging.getLogger()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

# test
logger.debug("test the custom logger")
logger.info("test the custom logger")
logger.warning("test the custom logger")
logger.error("test the custom logger")
logger.critical("test the custom logger")