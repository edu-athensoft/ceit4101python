"""
python logging

1. config
set logging level
set log file and mode
set format
show variable value
"""

import logging

logbase = './logs/'
logfile = logbase + 'logging_5.log'
logging.basicConfig(level=logging.DEBUG, filename=logfile, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

x = 99

logging.debug(f"msg: debug x = {x}")
logging.info("msg: info")
logging.warning("msg: warning")
logging.error("msg: error")
logging.critical("msg: critical")




