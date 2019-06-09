class User(object):
    """docstring for User"""
    def __init__(self, discord_id, name):
        super(User, self).__init__()
        self.id = discord_id
        self.name = name
