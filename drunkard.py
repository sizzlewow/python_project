from game import Movement
from game import utilities

class BarTender():
    
    def drink_slinging():
        pass

    def bar_fight():
        pass

    def arrested():
        pass

    def choice():
        choice = input("How many should I have? ")
        if int(choice) == int(1):
            utilities.slowPrint("I think one is enough, don't want to get drunk...\n")
        elif int(choice) == int(2):
            utilities.slowPrint("Two shouldn't hurt anything...I can handle it.\n")
        elif int(choice) == int(3):
            utilities.slowPrint("I've got nothing better to do, may as well have fun!\n")
        else:
            if int(choice) < int(1):
                utilities.slowPrint("...actually, I really shouldn't.\n")
                Movement.where_to()
            elif int(choice) > int(3):
                utilities.slowPrint("The bartender cut you off after you fell asleep at the bar...")
                BarTender.arrested()
            elif choice.isdigit() == False:
                print("invalid input\n")