class Game():
	"""LittleLeague Game"""
	def __init__(self, host, start_time):
		super(Game, self).__init__()
		self.host = host
		self.start_time = start_time
		self.teams = {}
		self.players = {}
		self.bench = {}

	def add_player(self, player):
		list_of_players = list(self.players.keys())
		if player.name in list_of_players:
			return False, f"{player.name} is already an active player in this game."
		else:
			players[player.name] = player
			return True, f"{player.name} has been added as an active player to the game."

	def add_team(self, team):
		list_of_teams = list(self.teams.values())
		for active_team in list_of_teams:
			if team.players == active_team.players:
				return False, f"{team.name} is already an active team in this game."
		teams[team.name] = team
		return True, f"{team.name} has been added as active team in this game."
