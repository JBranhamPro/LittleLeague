class Team():
    """LittleLeague Team"""
    def __init__(self, unique_id):
        super(Team, self).__init__()
        self._id = unique_id
        self.name = None
        self.summoners = []

    def add_summoner(self, summoner):
        list_of_summoners = list(self.summoners.keys())
        if summoner.name in list_of_summoners:
            return False, f"{summoner.name} is already on this team."
        else:
            summoners[summoner.name] = summoner
            return True, f"{summoner.name} has been added to the team."

    def summoner_in_game(self, summoner):
        current_summoners = [summoner._id for summoner in summoners]
        if summoner._id in current_summoners:
            return True
        else:
            return False
