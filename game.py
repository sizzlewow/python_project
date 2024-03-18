# Importing external modules
# numpy to build playermap
# helper for utility functions to improve ui
# player for user data and state

import logging
import numpy as np
from helper import utilities
from player import User

logging.basicConfig(filename="pylog.log", format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    filemode='w')
logger = logging.getLogger("game")
logger.setLevel(logging.DEBUG)

# GameMenu requests the user enter a name, greets them with that name, 
# then presents a status list and requires entry of the name entered to continue.

class GameMenu:

    def new_char():
        newname = input("What is your name?\n")
        User.player_name(User,newname)
        utilities.slowPrint("Time for an adventure," + User.name + "!")
    
    def main_menu():
        print("Name: ", User.name)
        print(User.state)
        print("Current coords: ", User.y, User.x)
        
        while True:
            if input("Enter your name and press enter to continue") == User.name:
                Movement.where_to()
            else:
                logger.info("User forgot name")
                print("Do you not even know your name?")


# Movement Class currently only contains one function to facilitate movement around the map.
                               
class Movement:
    
    def where_to():
        from world import buildMap
        mapMatrix = buildMap.assign_tiles() # 2d Array used for game map
        tile = buildMap.tile_dict() # Dictionary containing worldmap class names and abbreviated keys.
        y, x = User.y, User.x # Player starting coords, stored in player module
        location = (mapMatrix[y, x]) # Abbreviated tile name on map.

        while True:
            playermap = np.copy(mapMatrix) # Copy of worldmap updated to show player location.
            
            choice = input("\n[which location (n,s,e,w)]")
            
            if choice == "n":
                y -= 1
                if (y < 1):
                    logger.warning("Attempted leave map.")
                    location = (mapMatrix[y, x])
                    tile[location].start() 
                    y +=1

                else:
                    location = (mapMatrix[y, x])
                    tile[location].start()

            elif choice == "s":
                y += 1
                if (y > mapMatrix.shape[0]-2):
                    logger.warning("Attempted leave map.")
                    location = (mapMatrix[y, x])
                    tile[location].start()                  
                    y -= 1

                else:        
                    location = (mapMatrix[y, x])
                    tile[location].start()
 
            elif choice == "w":
                x -= 1
                if (x < 1):
                    logger.warning("Attempted leave map.")
                    location = (mapMatrix[y, x])
                    tile[location].start()
                    x += 1

                else:
                    location = (mapMatrix[y, x])
                    tile[location].start()
            elif choice == "e":
                x += 1
                if (x > mapMatrix.shape[1]-2):
                    logger.warning("Attempted leave map.")
                    location = (mapMatrix[y, x])
                    tile[location].start()                  
                    x -= 1

                else:
                    location = (mapMatrix[y, x])
                    tile[location].start()
            elif choice == "map":
                print("\n"*300)
                playermap[y,x]="O"
                print(playermap)
                playermap = None
            elif choice == "":
                    location = (mapMatrix[y, x])
                    tile[location].start()                
            else:
                logger.error("Invalid input")
                print ("invalid location")

            