

#Holds player state during runtime, or default state otherwise.

class User:
    y = 2
    x = 2
    state = False
    name = None
    def __init__(self, name):
        self.name = name

    def start_position(cls, y, x):
        cls.y = y
        cls.x = x

    def playerstate(cls, arg):
        cls.state = arg

    def player_name(cls, name):
        cls.name = name
        