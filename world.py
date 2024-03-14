import random
# from itertools import product
import numpy as np
from drunkard import BarTender
from helper import utilities


class WorldMap:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def start_text(self):
        pass

class OpeningTile():

    def start_text():
        intro = ('Welcome to your life.'
               '\n'
               '\nYou have hit rock bottom, and are rebuilding from scratch...'
                '\n')
        utilities.slowPrint(intro)
class TavernTile():
    
    def stay():
            return ("I really shouldn't...perhaps one drink isn't so bad though")

    def start_text():
        intro = (
                'The smell of yesterday\'s mead reminds'
                # '\nyou to get back to work...'
                # '\n\"Why am I here,\"you think to yourself, \"I need to find a job,'
                # '\n where\'s the job board in this town anyway?'
                )
        utilities.slowPrint(intro)

        while True:
            choice = input("stay or leave? ")
            if choice == "stay":
                print("\n")
                BarTender.choice()

            elif choice == "leave":
                print("\n")
                return (
                        'Time to get back on the wagon!'
                        )

            elif choice not in ["stay", "leave"]:
                utilities.slowPrint("I can't just stand here...\n")

  
class JobBoard():

    def start_text():
        jobs_status = (
                'You track down the job board.\n'
                '...got here too late.\n'
                'You find two jobs posted.\n'
                )
        return (random.choice(jobs_status))

    def bakery():
        return ('BAKERY IN SEARCH OF WIZARD...\n')
                
    def butcher():
        return ('BUTCHER NEEDS RAT CATCHER!\n')
    
class DoogansBakery():

    def start_text():
        bakery_status = ('You smell fresh baked bread, must be a bakery!\n'
                'Welcome to Doogan\'s Bakery!  What can we get for you?\n'
                )
        return (random.choice(bakery_status))

class ManksMeats():

    def start_text():
        butcher_status = (
                        'Just a minute...er..Welcome to Mank\'s Meats!\n'
                        'Lookin for meat?\n'
                        )
        return (random.choice(butcher_status))

class StreetTile():
   
    def start_text():
        
        street_status = (
                        'The street is bustling with busy folks',
                        'The street is oddly empty right now, perhaps the hive-mind decided to stay home',
                        'The street is alive with celebration, did I forget about a holiday?'
                        )
        return (random.choice(street_status))
    
class EdgeEnd():

    def start_text():

        boundary = (
                    "I can't go any further...",
                    "There's something blocking my path...",
                    "Beyond here be dragons...",
                    )
        return(random.choice(boundary))
    



class buildMap():

    def assign_tiles():
        tile_map = [["EE","EE","EE","EE","EE","EE","EE"],
                    ["EE","ST","ST","ST","ST","ST","EE"],
                    ["EE","ST","ST","ST","ST","DB","EE"],
                    ["EE","TT","JB","ST","MM","ST","EE"],
                    ["EE","EE","EE","EE","EE","EE","EE"]]
        mapMatrix = np.array(tile_map, dtype='str_')
        return mapMatrix
    
    def tile_dict():
        tile_types = {
        "OT": OpeningTile,
        "TT": TavernTile,
        "JB": JobBoard,
        "DB": DoogansBakery,
        "MM": ManksMeats,
        "ST": StreetTile,
        "EE": EdgeEnd
        }
        return tile_types



