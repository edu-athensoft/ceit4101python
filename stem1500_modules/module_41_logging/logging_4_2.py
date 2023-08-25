"""
python logging

1. config
set logging level
set log file and mode
set format - adding logger name
"""

import logging

logbase = './logs/'
logfile = logbase + 'logging_4_2.log'
logging.basicConfig(level=logging.DEBUG, filename=logfile, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.debug("msg: debug")
logging.info("msg: info")
logging.warning("msg: warning")
logging.error("msg: error")
logging.critical("msg: critical")




