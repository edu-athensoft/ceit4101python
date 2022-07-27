"""
python logging

1. config
set logging level to INFO

"""

import logging

logging.basicConfig(level=logging.INFO)

logging.debug("msg: debug")
logging.info("msg: info")
logging.warning("msg: warning")
logging.error("msg: error")
logging.critical("msg: critical")




