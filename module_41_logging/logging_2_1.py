"""
python logging

1. config
set logging level to DEBUG

"""

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("msg: debug")
logging.info("msg: info")
logging.warning("msg: warning")
logging.error("msg: error")
logging.critical("msg: critical")




