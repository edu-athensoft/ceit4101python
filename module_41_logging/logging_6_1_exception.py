"""
python logging

1. config
set logging level
set log file and mode
set format
show exception information

syntax:
logging.error("ZeroDivisionError", exc_info=True)

"""

import logging

logbase = './logs/'
logfile = logbase + 'logging_6_1.log'
logging.basicConfig(level=logging.DEBUG, filename=logfile, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

try:
    x = 99
    x / 0
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError", exc_info=True)

