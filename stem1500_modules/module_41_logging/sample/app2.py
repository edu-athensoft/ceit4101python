"""
app2
"""

import logging

log = logging.getLogger("main.app2")


def foo2():
    log.debug("Logging is configured.")
    log.info("Logging is configured.")
    log.warning("Logging is configured.")
    log.error("Logging is configured.")
    log.critical("Logging is configured.")
