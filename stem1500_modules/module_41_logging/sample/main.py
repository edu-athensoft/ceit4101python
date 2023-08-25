import logging

import app1
import app2


def setup_log():
    # logging files
    logbase = './logs/'
    logfile = logbase + 'logging_sample.log'

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
    logger = logging.getLogger("main")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    return logger


def main():
    logger = setup_log()
    logger.debug("main() called")
    app1.foo1()
    app2.foo2()


if __name__ == '__main__':
    main()
