# Importing external modules
# helper for utility functions to improve ui
# player for User data and state

from helper import utilities
from player import User

class BarTender:
    
    onedrink = "I think one is enough, don't want to get drunk..."

    twodrinks = "Two shouldn't hurt anything...I can handle it."

    threedrinks = "I've got nothing better to do, may as well have fun!"

    manydrinks = "The bartender cut you off after you passed out at the bar..."

    leave = "...actually, I really shouldn't."

    def choice():
        while True:
            choice = int(input("How many should I have? "))

            if not isinstance(choice, int):
                print("invalid input\n")
                continue
            else:                
                if choice == 1:
                    utilities.slowPrint(BarTender.onedrink)
                    utilities.slowPrint("*"*100)
                    break
                elif choice == 2:
                    utilities.slowPrint(BarTender.twodrinks)
                    utilities.slowPrint("*"*100)
                    break
                elif choice == 3:
                    utilities.slowPrint(BarTender.threedrinks)
                    utilities.slowPrint("*"*100)
                    break
                elif choice > 3:
                    User.playerstate(User, True)
                    utilities.slowPrint(BarTender.manydrinks)
                    User.start_position(User, 2, 1)
                    utilities.slowPrint("*"*100)
                    break
                elif choice == 0:
                    utilities.slowPrint(BarTender.leave)
                    break
