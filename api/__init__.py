from flask import Flask
from flask_restful import Api, Resource

from .resources import RESOURCES

APP = Flask(__name__)
API = Api(APP)

for resource in RESOURCES:
    API.add_resource(resource, resource.endpoint)
