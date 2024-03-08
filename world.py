import time
import random
import numpy as np
import game




class WorldMap():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
            
class OpeningTile():
    def start_text(intro):
        intro = ('Welcome to your life.'
               '\n'
               '\nYou have hit rock bottom, and are rebuilding from scratch...'
               '\n'
               '\nWhat is your name?'
              )
    
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

class TavernTile(WorldMap):
    def start_text(self):
        return (
                'The smell of yesterday\'s mead reminds'
                '\nyou to get back to work...'
                '\n\"Why am I here,\"you think to yourself, \"I need to find a job,'
                '\n where\'s the job board in this town anyway?'
            )
    
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
    
    def stay(self):
        return (
                'I really shouldn\'t...perhaps one drink isn\'t so bad though'
            )
    def leave():
        return (
                'Time to get back on the wagon!'
            )
class JobBoard(WorldMap):
    def start_text(self):
        return (
                'You track down the job board, \"...got here too late\",'
                '\nyou grumble; realizing you did this to yourself'
                '\nYou find two jobs posted:'
            )
    
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def bakery(self):
        return (
                'BAKERY IN SEARCH OF WIZARD...'
            )
    def butcher(self):
        return (
                'BUTCHER NEEDS RAT CATCHER!'
            )
    
class DoogansBakery(
):
    def start_text(self):
        return (
            'Welcome to Doogan\'s Bakery!  What can we get for you?'
        )
    
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

class ManksMeats(WorldMap):
    def start_text(self):
        return (
            'Just a minute...er..Welcome to Mank\'s Meats!'
            'What do you need?'
        )

class StreetTile(WorldMap):
    def start_text(self):

        street_status = (
            'The street is bustling with busy folks',
            'The street is oddly empty right now, perhaps the hive-mind decided to stay home',
            'The street is alive with celebration, did I forget about a holiday?'
        )
        return (random.choice(street_status))
    
    def __init__(self, x, y, z):
        super().__init__(x, y, z)


def read_world_map():
    tile_types = {
        "OT": OpeningTile,
        "TT": TavernTile,
        "JB": JobBoard,
        "DB": DoogansBakery,
        "MM": ManksMeats,
        "ST": StreetTile
        }
    
class utilities(OpeningTile):
    def slowtype():
        for char in ():
            print(char, end='', flush=True)
            time.sleep(0.05)
    
    tile_list = tile_types.items()

    tile_array = np.array(tile_list)
    print(tile_array)

    print(tile_array)