from random import randint

class Game():
    """LittleLeague Game"""
    def __init__(self, unique_id):
        super(Game, self).__init__()
        self._id = unique_id
        self.host = None
        self.start_time = None
        self.teams = []
        self.summoners = []
        self.bench = []

    def add_summoner(self, summoner):
        list_of_summoners = list(self.summoners.keys())
        if summoner.name in list_of_summoners:
            return False, f"{summoner.name} is already an active summoner in this game."
        else:
            summoners[summoner.name] = summoner
            return True, f"{summoner.name} has been added as an active summoner to the game."

    def add_summoner_to_game(self, summoner):
        if summoner_in_game(summoner):
            return False, f"{summoner.name} is already in this game."
        elif summoner.current_game and summoner.current_game != self._id:
            return False, f"{summoner.name} is already active in another game."

        self.summoners.append(summoner)
        summoner.set_current_game(self)
        return True, f"{summoner.name} was added to this game."

    def add_team(self, team):
        list_of_teams = list(self.teams.values())
        for active_team in list_of_teams:
            if team.summoners == active_team.summoners:
                return False, f"{team.name} is already an active team in this game."
        teams[team.name] = team
        return True, f"{team.name} has been added as active team in this game."

    def random_draft(self):
        draft_pool = self.summoners.copy()
        team_one = self.teams[0]
        team_two = self.teams[1]
        i = 0
        while i < 10:
            summoner = draft_pool[randint(0, len(draft_pool) - 1)]
            if len(team_one.summoners) <= 5:
                team_one.add_summoner(summoner)
            else:
                team_two.add_summoner(summoner)
            draft_pool.remove(summoner)
            i += 1
        team_one_summoners = [summoner.name for summoner in team_one.summoners]
        team_two_summoners = [summoner.name for summoner in team_two.summoners]
        return team_one_summoners, team_two_summoners

    def ranked_draft(self):
        pass

    def summoner_in_game(self, summoner):
        current_summoners = [summoner._id for summoner in summoners]
        if summoner._id in current_summoners:
            return True
        else:
            return False
