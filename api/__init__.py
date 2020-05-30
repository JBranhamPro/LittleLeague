from concurrent_log_handler import ConcurrentRotatingFileHandler
from flask import Flask
from flask_restful import Api, Resource

from . import config as props
from . import resources

APP = Flask(__name__)
API = Api(APP)
DB = db.InMemDB

for resource in resources.RESOURCES:
    API.add_resource(resource, resource.endpoint)
