


class user:
    y = 2
    x = 2
    state = False
    name = None
    def __init__(self, name, y, x):
        self.name = name
        self.y = y
        self.x = x

    def start_position(cls, y, x):
        cls.y = y
        cls.x = x

    def playerstate(cls, arg):
        cls.state = arg
        