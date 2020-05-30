import logging
import sys

from concurrent_log_handler import ConcurrentRotatingFileHandler

from . import APP


LOGGER = logging.getLogger('ll_api_logger')
LOGGER.setLevel(logging.DEBUG)
FORMATTER = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(message)s')
ROTATING_FILE_HANDLER = ConcurrentRotatingFileHandler('LL_Flask_API.log', 'a', 1024*1000, 10)
ROTATING_FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(ROTATING_FILE_HANDLER)
LOGGER.info("Logger initialized and running.")

DEV_SERVER_IP = sys.argv[0]
DEV_SERVER_PORT = sys.argv[1]


if __name__ == '__main__':
    APP.run(host=DEV_SERVER_IP, port=DEV_SERVER_PORT, debug=True)
