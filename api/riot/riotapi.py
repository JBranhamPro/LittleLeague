import logging
import requests
import config as props

LOGGER = logging.getLogger('flask_logger')

class RiotApi:
    """docstring for RiotApi"""
    
    def get_summoner_by_name(summoner_name):

        endpoint = f'/lol/summoner/v4/summoners/by-name/{summoner_name}'
        response_data = RiotApi.make_request(endpoint)
        
        summoner_details = {}

        summoner_details['puuid'] = response_data.get('puuid')
        summoner_details['account_id'] = response_data.get('accountId')
        summoner_details['profile_icon_id'] = response_data.get('profileIconId')
        summoner_details['summoner_id'] = response_data.get('id')
        summoner_details['summoner_name'] = response_data.get('name')
        summoner_details['summoner_level'] = response_data.get('summonerLevel')
        
        if None in summoner_details.values():
            LOGGER.warning(f"Null value found in request data on getSummonerByName for {summoner_name}. Summoner details found: {summoner_details}")
            return None
        else:
            return summoner_details

    def get_rank_data(summoner_id):

        endpoint = f'/lol/league/v4/entries/by-summoner/{summoner_id}'
        response_data = RiotApi.make_request(endpoint)
        return response_data

    def make_request(endpoint):

        response = requests.get(
            props.RiotApi.na_url + endpoint, 
            headers={"X-Riot-Token": props.RiotApi.api_key}
        )
        response_data = response.json()
        LOGGER.debug(f"Response data returned: {response_data}")
        return response_data
