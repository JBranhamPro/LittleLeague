from concurrent_log_handler import ConcurrentRotatingFileHandler
import logging
from flask import Flask
from flask_restful import Api, Resource
import properties as props
import resources

LOGGER = logging.getLogger('flask_logger')
LOGGER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(message)s')
ROTATING_FILE_HANDLER = ConcurrentRotatingFileHandler('LL_Flask_API.log', 'a', 1024*1000, 10)
ROTATING_FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(ROTATING_FILE_HANDLER)
LOGGER.info("Logger initialized and running.")

APP = Flask(__name__)
API = Api(APP)

for resource in resources.RESOURCES:
    API.add_resource(resource, resource.endpoint)

if __name__ == '__main__':
    APP.run(host=props.DevHost.ip, port=props.DevHost.port, debug=True)