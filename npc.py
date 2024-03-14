# Importing external modules
# game for movement and interaction
# helper for utility functions to improve ui
# player for user data and state

from game import Movement
from helper import utilities
from player import user

class BarTender:
    
    onedrink = "I think one is enough, don't want to get drunk..."

    twodrinks = "Two shouldn't hurt anything...I can handle it."

    threedrinks = "I've got nothing better to do, may as well have fun!"

    manydrinks = "The bartender cut you off after you passed out at the bar..."

    leave = "...actually, I really shouldn't."


###FIX THIS BLOCK, Loop not exiting, and can't handle non integer input.
    def choice():
        while True:
            choice = input("How many should I have? ")
            if choice == 1:
                utilities.slowPrint(BarTender.onedrink)
                break
            elif int(choice) == 2:
                utilities.slowPrint(BarTender.twodrinks)
                break
            elif int(choice) == 3:
                utilities.slowPrint(BarTender.threedrinks)
                break
            elif int(choice) < 1 or choice == "leave":
                utilities.slowPrint(BarTender.leave)
                break
            elif int(choice) > 3:
                user.playerstate(user, True)
                utilities.slowPrint(BarTender.manydrinks)
                user.start_position(user, 2, 1)
                break
            else:
                print("invalid input\n")