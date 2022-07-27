import logging
from logging.config import dictConfig

import yaml

import app1
import app2


def setup_log():
    with open('./config/logging.yaml') as fin:
        conf = yaml.load(fin, yaml.FullLoader)
    dictConfig(conf)
    return logging.getLogger('main2')


def main():
    logger = setup_log()
    logger.debug("main() called")
    app1.foo1()
    app2.foo2()


if __name__ == '__main__':
    main()
