"""
app1
"""

import logging

log = logging.getLogger("main2.app1")


def foo1():
    log.debug("Logging is configured.")
    log.info("Logging is configured.")
    log.warning("Logging is configured.")
    log.error("Logging is configured.")
    log.critical("Logging is configured.")
