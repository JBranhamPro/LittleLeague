from flask_restful import Resource, request
import json
# from riot.riotApi import RiotApi
from riot import Summoner


class HelloWorld(Resource):

    endpoint = '/hello/'
    endpoints = ['/', '/hello', '/hello/']

    def get(self):
        return {'hello': 'world'}


class Summoner(Resource):

    endpoint = '/summoner/<string:summoner_name>/'

    def get(self, summoner_name):

        summoner = Summoner(summoner_name)

        return summoner.get_data()


class Summoner(Resource):

    endpoint = '/summoners/'

    def get(self):

        request_data = request.json()
        request_data = json.loads(request_data)
        summoner_id = request_data.get('summoner_id')
        summoner_name = request_data.get('summoner_name')

        if summoner_id:
            summoner = Summoner(_id=summoner_id)
        elif summoner_name:
            summoner = Summoner(name=summoner_name)
        else:
            LOGGER.warning('No summoner data was provided with this request.')
            summoner = None

        return summoner


class Test(Resource):

    endpoint = '/test/<string:summoner_name>/'
    endpoints = ['/test', '/test/']

    # def get(self, summoner_name):

    #     summoner_details = RiotApi.get_summoner_by_name(summoner_name)
    #     ranked_data = RiotApi.get_ranked_data(summoner_details['summoner_id'])

    #     return ranked_data, 200

    def get(self, summoner_name):

        summoner = Summoner(summoner_name)
        
        return summoner.get_data()

RESOURCES = [HelloWorld, Test]
