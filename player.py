import json

#Holds player state during runtime, or default state otherwise.

class User:

    y = 2
    x = 2
    state = False
    name = None
    location = None

    def __init__(self, name):
        self.name = name

    def start_position(cls, y, x):
        cls.y = y
        cls.x = x

    def playerstate(cls, state):
        cls.state = state

    def player_name(cls, name):
        cls.name = name



## Different implementation of User class using dictionary to keep track of user stats.

class TestUser():

    def __init__(self, name, y, x, hp):
        self.name = name
        self.y = y
        self.x = x
        self.hp = hp

    def move(self, y, x):
        self.y += y
        self.x += x

    def move_north(self):
        self.move(x=0,y=-1)

    def move_south(self):
        self.move(x=0,y=+1)

    def move_east(self):
        self.move(x=+1,y=0)

    def move_west(self):
        self.move(x=-1,y=0)

# users = {}

# name = input("what is your name? ")

# while name != "":
#     users[name]= TestUser(name, 2, 2, 100)
#     break

# print(users[name].name)
# print(users[name].y)
# print(users[name].x)
# print(users[name].hp)
# print(users)
# with open('test.txt','w') as convert_file:
#     convert_file.write(str(users))