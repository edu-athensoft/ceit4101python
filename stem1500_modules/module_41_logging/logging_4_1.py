"""
python logging

1. config
set logging level
set log file and mode
set format - time, level, message
"""

import logging

logbase = './logs/'
logfile = logbase + 'logging_4_1.log'
logging.basicConfig(level=logging.DEBUG, filename=logfile, filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("msg: debug")
logging.info("msg: info")
logging.warning("msg: warning")
logging.error("msg: error")
logging.critical("msg: critical")




