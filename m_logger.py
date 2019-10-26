import logging


def do_logging(ex: Exception):
    log = logging.getLogger(__name__)
    log.exception(ex, exc_info=True)