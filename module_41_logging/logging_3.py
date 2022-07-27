"""
python logging

1. config
set logging level
set log file and mode
"""

import logging

logbase = './logs/'
logfile = logbase + 'logging_3.log'
logging.basicConfig(level=logging.INFO, filename=logfile, filemode='w')

logging.debug("msg: debug")
logging.info("msg: info")
logging.warning("msg: warning")
logging.error("msg: error")
logging.critical("msg: critical")




