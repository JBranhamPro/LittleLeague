from flask_restful import Resource
# from riot.riotApi import RiotApi
from riot.summoner import Summoner

class HelloWorld(Resource):

    endpoint = '/hello/'
    endpoints = ['/', '/hello', '/hello/']

    def get(self):
        return {'hello': 'world'}

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