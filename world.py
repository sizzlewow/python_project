# Importing external modules
# Random for varied responses from tiles
# numpy for buildmap
# npc contains npc classes
# helper for utility functions to improve ui

import random
import numpy as np
from npc import BarTender
from helper import utilities
from player import User

# Classes here all represent map tile types and their attributes (except buildMap).
# All contain a function to print intro/status text upon entry.
# Some contain functions to facilitate user interaction through choices.

class OpeningTile:

    intro = ('Welcome to your life.'
        '\n'
        '\nYou have hit rock bottom, and are rebuilding from scratch...'
        '\n')
    def start():
        print("\n"*300)
        if User.state == True:    
            utilities.slowPrint(OpeningTile.intro)
        else:
            StreetTile.start()

class TavernTile:

    status = (
                "Ah...The smell of yesterday's mead...",
                "It's the ale house!",
                "I seem to have found the local dive bar."
                )
    
    stay = "I really shouldn't...perhaps one drink isn't so bad though"

    leave = "Time to get back on the wagon!"

    def start():
        print("\n"*300)
        utilities.slowPrint(random.choice(TavernTile.status))
        while True:
            choice = input("stay or leave? ")
            if choice == "stay":
                print("\n"*300)
                BarTender.choice()
                break
            elif choice == "leave":
                print("\n"*300)
                utilities.slowPrint(TavernTile.leave)
                break
            elif choice == "":
                print("\n"*300)
                utilities.slowPrint("I can't just stand here...\n")
            elif choice not in ["stay", "leave"]:
                print("\n"*300)
                print("invalid choice")
                
 
class JobBoard:

    status = (
            'You track down the job board.',
            '...got here too late.',
            'You find two jobs posted.'
            )
    job1 = "BAKERY IN SEARCH OF WIZARD!"
    job2 = "BUTCHER NEEDS RAT CATCHER!"

    def start():
        print("\n"*300)
        utilities.slowPrint(random.choice(JobBoard.status))
        while True:
            choice = input("read or leave\n")
            if choice == "read":
                print("\n"*300)
                utilities.slowPrint(JobBoard.job1)
                utilities.slowPrint(JobBoard.job2)
            elif choice == "leave":
                print("\n"*300)
                break
                
    
class DoogansBakery:

    status = (
            'You smell fresh baked bread, must be a bakery!',
            'Welcome to Doogan\'s Bakery!  What can we get for you?'
            )

    def start():
        print("\n"*300)
        utilities.slowPrint(random.choice(DoogansBakery.status))


class ManksMeats:

    status = (
            'Just a minute...er..Welcome to Mank\'s Meats!',
            'Lookin for meat?'
            )
    
    def start():
        print("\n"*300)
        utilities.slowPrint(random.choice(ManksMeats.status))

class StreetTile:

    status = (
            'The street is bustling with busy folks',
            'The street is oddly empty right now, perhaps the hive-mind decided to stay home',
            'The street is alive with celebration, did I forget about a holiday?'
            )    
   
    def start():
        print("\n"*300)
        utilities.slowPrint(random.choice(StreetTile.status))
    
class EdgeEnd:

    status = (
            "I can't go any further...",
            "There's something blocking my path...",
            "Beyond here be dragons...",
            )    

    def start():
        print("\n"*300)
        print(random.choice(EdgeEnd.status))
    


# The buildMap class contains functions to generate the map and facilitate associating
# the above classes with their respecitive positions on it.
# I have used numpy.array to build the matrix, though it probably wasn't entirely needed.
# This is mostly used by Movement in game.py
        
class buildMap():

    def assign_tiles():
        tile_map = [["EE","EE","EE","EE","EE","EE","EE"],
                    ["EE","ST","ST","ST","ST","ST","EE"],
                    ["EE","OT","ST","ST","ST","DB","EE"],
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



