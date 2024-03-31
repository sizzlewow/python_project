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

    name = ""
    empty = True
    canEnter = True
    intro = ('Welcome to your life.'
        '\n'
        '\nYou have hit rock bottom, and are rebuilding from scratch...'
        '\n')
    
    @classmethod
    def __init__(cls, name):
        cls.name = name
        cls.empty
        cls.canEnter

    def start():
        # print("\n"*300)
        if User.state == True:    
            utilities.slowPrint(OpeningTile.intro)
        else:
            StreetTile.start()

class TavernTile:

    name = 'Tavern'
    empty = False
    canEnter = True
    status = (
                "Ah...The smell of yesterday's mead...",
                "It's the ale house!",
                "I seem to have found the local dive bar."
                )  
    stay = "I really shouldn't...perhaps one drink isn't so bad though"
    leave = "Time to get back on the wagon!"

    @classmethod
    def __init__(cls, name):
        cls.name = name
        cls.empty
        cls.canEnter

    def start():
        # print("\n"*300)
        utilities.slowPrint(random.choice(TavernTile.status))
        while True:
            choice = input("stay or leave? ")
            if choice == "stay":
                # print("\n"*300)
                BarTender.choice()
                break
            elif choice == "leave":
                # print("\n"*300)
                utilities.slowPrint(TavernTile.leave)
                break
            elif choice == "":
                # print("\n"*300)
                utilities.slowPrint("I can't just stand here...\n")
            elif choice not in ["stay", "leave"]:
                # print("\n"*300)
                print("invalid choice")
                
 
class JobBoard:

    name = 'Job Board'
    empty = True
    canEnter = True
    status = (
            'You track down the job board.',
            '...got here too late.',
            'You find two jobs posted.'
            )
    job1 = "BAKERY IN SEARCH OF WIZARD!"
    job2 = "BUTCHER NEEDS RAT CATCHER!"

    @classmethod
    def __init__(cls, name):
        cls.name = name
        cls.empty
        cls.canEnter

    def start():
        # print("\n"*300)
        utilities.slowPrint(random.choice(JobBoard.status))
        while True:
            choice = input("read or leave\n")
            if choice == "read":
                # print("\n"*300)
                utilities.slowPrint(JobBoard.job1)
                utilities.slowPrint(JobBoard.job2)
            elif choice == "leave":
                # print("\n"*300)
                break
                
    
class DoogansBakery:

    name = "Doogan's Bakery"
    empty = False
    canEnter = True
    status = (
            'You smell fresh baked bread, must be a bakery!',
            'Welcome to Doogan\'s Bakery!  What can we get for you?'
            )
    
    @classmethod
    def __init__(cls, name):
        cls.name = name
        cls.empty
        cls.canEnter

    def start():
        # print("\n"*300)
        utilities.slowPrint(random.choice(DoogansBakery.status))


class ManksMeats:

    name = "Mank's Meats"
    empty = False
    canEnter = True
    status = (
            'Just a minute...er..Welcome to Mank\'s Meats!',
            'Lookin for meat?'
            )
    
    @classmethod
    def __init__(cls, name):
        cls.name = name
        cls.empty
        cls.canEnter

    def start():
        # print("\n"*300)
        utilities.slowPrint(random.choice(ManksMeats.status))

class StreetTile:

    name = "street"
    empty = True
    canEnter = True
    status = (
            'The street is bustling with busy folks',
            'The street is oddly empty right now, perhaps the hive-mind decided to stay home',
            'The street is alive with celebration, did I forget about a holiday?'
            )
    
    @classmethod
    def __init__(cls, name):
        cls.name = name
        cls.empty
        cls.canEnter

    def start():
        # print("\n"*300)
        utilities.slowPrint(random.choice(StreetTile.status))
    
class Boundary:

    name = "Boundary"
    empty = False
    canEnter = False
    status = (
            "I can't go any further...",
            "There's something blocking my path...",
            "Beyond here be dragons...",
            )
       
    @classmethod
    def __init__(cls, name):
        cls.name = name
        cls.empty
        cls.canEnter

    def start():
        # print("\n"*300)
        print(random.choice(Boundary.status))
    
# The buildMap class contains functions to generate the map and facilitate associating
# the above classes with their respecitive positions on it.
# I have used numpy.array to build the matrix, though it probably wasn't entirely needed.
# This is mostly used by Movement in game.py
        
class BuildMap():

    tileMap = [
        ["EE","EE","EE","EE","EE","EE","EE"],
        ["EE","  ","  ","  ","  ","  ","EE"],
        ["EE","  ","  ","  ","  ","  ","EE"],   
        ["EE","  ","  ","  ","  ","  ","EE"],
        ["EE","OT","  ","  ","  ","DB","EE"],
        ["EE","TT","JB","  ","MM","  ","EE"],
        ["EE","EE","EE","EE","EE","EE","EE"]
        ]   
    tileDict = {
    "OT": OpeningTile,
    "TT": TavernTile,
    "JB": JobBoard,
    "DB": DoogansBakery,
    "MM": ManksMeats,
    "  ": StreetTile,
    "EE": Boundary,
    }

    @classmethod
    def __init__(cls, tileMap, tileDict):
        cls.tileMap = tileMap
        cls.tileDict = tileDict        

    def assign_tiles():

        mapMatrix = np.array(BuildMap.tileMap, dtype='str_')
        return mapMatrix
    




