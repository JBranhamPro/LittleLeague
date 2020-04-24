USERS = {}

def get(username):
    user = USERS.get(username)
    
    if user is None:
        user = User(username)
        USERS[username] = user
        return user
    else:
        return user


class User(object):
    """Discord User"""
    def __init__(self, name):
        super(User, self).__init__()
        self.current_game = None
        self.name = name
        self.discord_id = ''
        self.meta = {'recent_commands': []}

    def log_command(self, command_name, cmd_input=None):
        self.meta['recent_commands'].append(command_name)

    def recent_commands(self):
        recent_commands = self.meta['recent_commands']
        return recent_commands

    def set_active_game(self, game):
        if self.current_game:
            return False, f"{self.name} is already in a game. Please !bye out and try again."
        else:
            self.current_game = game
            return True, f"{self.name} successfully added to {game.name}."
