from .riotapi import RiotApi

class Summoner(object):
    """docstring for Summoner"""
    def __init__(self, name=None):
        super(Summoner, self).__init__()

        if name:
            details = RiotApi.get_summoner_by_name(name)

            self._id = details['summoner_id']
            self.account_id = details['account_id']
            self.current_game = None
            self.level = details['summoner_level']
            self.name = details['summoner_name']
            self.profile_icon = details['profile_icon_id']
            self.puuid = details['puuid']
            self.rank_value = 150

    def get_data(self):
        data = {}
        data['account_id'] = self.account_id
        data['summoner_level'] = self.level
        data['summoner_name'] = self.name
        data['profile_icon_id'] = self.profile_icon
        data['puuid'] = self.puuid
        data['summoner_id'] = self._id

        rank_data = RiotApi.get_rank_data(self._id)
        data['rank_data'] = rank_data
        
        data['rank_value'] = self.evaluate_rank(rank_data=rank_data)

        return data

    def evaluate_rank(self, rank_data=None):
        if not rank_data:
            rank_data = RiotApi.get_rank_data(self._id)

        leagues = {}

        for league in rank_data:
            league_name = league['queueType'].upper()
            tier = league['tier']
            rank = league['rank']
            leagues[league_name] = (tier, rank)

        if 'RANKED_SOLO_5X5' in leagues.keys():
            league = leagues['RANKED_SOLO_5X5']
        elif 'RANKED_TEAM_5X5' in leagues.keys():
            league = leagues['RANKED_TEAM_5X5']
        else:
            LOGGER.debug(f"The summoner, {self.name}, has no valid leagues for rank_value.")
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
