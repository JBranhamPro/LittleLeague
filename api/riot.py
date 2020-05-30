import logging
import requests
import config
# TODO: Need to add riot_api_key to config

LOGGER = logging.getLogger('ll_api_logger')


class RiotApi:
    """Methods to access League of Legends data via the Riot REST API"""
    
    def get_summoner_by_name(summoner_name, region='na1'):
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
            LOGGER.warning(f"NULL value in summoner details: {summoner_details}")
            return None
        else:
            return summoner_details

    def get_rank_data(summoner_id, region='na1'):
        endpoint = f'/lol/league/v4/entries/by-summoner/{summoner_id}'
        response_data = RiotApi.make_request(endpoint)
        return response_data

    def make_request(endpoint, region):
        request_url = f'https://{region}.api.riotgames.com{endpoint}'

        response = requests.get(request_url, headers={"X-Riot-Token": config.riot_api_key})

        response_data = response.json()
        LOGGER.debug(f"Response summoner_data returned: {response_data}")
        return response_data


class Summoner(object):
    """Object containing all the data for a player or Summoner """
    def __init__(self, _id=None, name=None):
        super(Summoner, self).__init__()

        if _id:
            details = RiotApi.get_summoner_by_id(_id)
        elif name:
            details = RiotApi.get_summoner_by_name(name)

        self._id = details['summoner_id']
        self.account_id = details['account_id']
        self.current_game = None
        self.level = details['summoner_level']
        self.name = details['summoner_name']
        self.profile_icon = details['profile_icon_id']
        self.puuid = details['puuid']
        self.rank_value = 150

    def get_summoner_data(self):      
        summoner_data = {}
        rank_data = RiotApi.get_rank_data(self._id)
        
        summoner_data['account_id'] = self.account_id
        summoner_data['summoner_level'] = self.level
        summoner_data['summoner_name'] = self.name
        summoner_data['profile_icon_id'] = self.profile_icon
        summoner_data['puuid'] = self.puuid
        summoner_data['summoner_id'] = self._id
        summoner_data['rank_data'] = rank_data
        summoner_data['rank_value'] = self.evaluate_rank(rank_data=rank_data)

        return summoner_data

    def evaluate_rank(self, rank_data=None):    
        if not rank_data:
            rank_data = RiotApi.get_rank_data(self._id)

        ranked_leagues = {}

        for league in rank_data:
            league_name = league['queueType'].upper()
            tier = league['tier']
            rank = league['rank']
            ranked_leagues[league_name] = (tier, rank)

        if 'RANKED_SOLO_5X5' in ranked_leagues.keys():
            league = ranked_leagues['RANKED_SOLO_5X5']
        elif 'RANKED_TEAM_5X5' in ranked_leagues.keys():
            league = ranked_leagues['RANKED_TEAM_5X5']
        else:
            LOGGER.debug(f"The summoner, {self.name}, has no valid ranked leagues.")
            return 150

        tier = league[0]
        rank = league[1]

        tier_values = {
            'IRON': 100,
            'BRONZE': 125,
            'SILVER': 156.25,
            'GOLD': 195.3125,
            'PLATINUM': 244.1406,
            'DIAMOND': 305.1758,
            'MASTER': 381.4697,
            'GRANDMASTER': 476.8372,
            'CHALLENGER': 596.0464
        }

        rank_modifiers = {
            'IV': 1,
            'III': 1.0625,
            'II': 1.125,
            'I': 1.1875
        }

        tier_value = tier_values.get(tier)

        rank_modifier = rank_modifiers.get(rank)
        
        if None in (tier_value, rank_modifier):
            LOGGER.warning(f"The tier and rank, {tier} {rank}, was supplied but is invalid.")
            return 150

        rank_value = tier_value * rank_modifier

        self.rank_value = rank_value

        return rank_value

    def set_current_game(self, game):     
        self.current_game = game
