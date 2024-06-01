import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def getLogger():
    return logger


def debug(title, content):
    logger.debug('%s: %s', title, content)


def info(title, content):
    logger.info('%s: %s', title, content)


def warn(title, content):
    logger.warn('%s: %s', title, content)


def error(title, content):
    logger.error('%s: %s', title, content)


def fatal(title, content):
    logger.fatal('%s: %s', title, content)


debug('Status', 'Logger Init')
