# Importing external modules
# numpy to build playermap
# helper for utility functions to improve ui
# player for user data and state

import re
import numpy as np
from world import BuildMap
from helper import utilities
from player import User

# GameMenu requests the user enter a name, greets them with that name, 
# then presents a status list and requires entry of the name entered to continue.
mapMatrix = BuildMap.assign_tiles()
tile = BuildMap.tileDict


# location = (mapMatrix[y, x])

class GameMenu:

    def new_char():
        newname = input("What is your name?\n")
        player = input("which slot? ")

        User.player_name(User,newname)
        utilities.slowPrint("Time for an adventure," + User.name + "!")
    
    def main_menu():
        location = (mapMatrix[User.y, User.x])
        print("Location: ", tile[location].name)
        print("Name: ", User.name)
        print("Current coords: ", User.y, User.x)
        


# Movement Class currently only contains one function to facilitate movement around the map.
                               
class Movement:
    
    def where_to():
        y, x = User.y, User.x
        
        playermap = np.copy(mapMatrix) # Copy of worldmap updated to show player location.
         # Dictionary containing worldmap class names and abbreviated keys.
        # mapMatrix = buildMap.assign_tiles() # 2d Array used for game map
        # Abbreviated tile name on map.
        
        sepinput = re.findall(r"(\D+|\d+)",playerinput)
        direction = sepinput[0]

        
        if direction == "map":
            playermap[y,x]="@ "
            print(playermap)
            playermap = None

        elif len(sepinput) == 2 and direction in '^[nsew]$':
            dist = int(sepinput[1])
            if direction == "n":
                for _ in range(dist):
                    y -= 1
                    location = mapMatrix[y,x]
                    if tile[location].canEnter == False or (y < 1):
                        y +=1
                        break
                    elif tile[location].empty == False:
                        break
                    

            elif direction == "s":
                for _ in range(dist):
                    y += 1
                    location = mapMatrix[y,x]
                    if tile[location].canEnter == False or (y > mapMatrix.shape[0]-2):
                        y -= 1
                        break
                    elif tile[location].empty == False:
                        break
                    

            elif direction == "w":
                for _ in range(dist):
                    x -= 1
                    location = mapMatrix[y,x]
                    if tile[location].canEnter == False or (x < 1):
                        x +=1
                        break
                    elif tile[location].empty == False:
                        break
                    

            elif direction == "e":
                for _ in range(dist):
                    x += 1
                    location = mapMatrix[y,x]
                    if tile[location].canEnter == False or (x > mapMatrix.shape[0]-2):
                        x -= 1
                        break
                    elif tile[location].empty == False:
                        break
                    
                    
            if (y,x) == (User.y,User.x):
                print("You haven't moved...")

            else:
                User.y, User.x = y, x
                location = (mapMatrix[User.y, User.x])
                tile[location].start()
        else:
            print ("invalid input")

    def look_around():
        y,x = User.y,User.x
        if "north" in playerinput:
            location = mapMatrix[y-1,x]
            print("You see the " + tile[location].name)
        elif "south" in playerinput:
            location = mapMatrix[y+1,x]
            print("You see the " + tile[location].name)
        elif "east" in playerinput:
            location = mapMatrix[y,x+1]
            print("You see the " + tile[location].name)
        elif "west" in playerinput:
            location = mapMatrix[y,x-1]
            print("You see the " + tile[location].name)
        else: 
            print("not sure what you mean...")




while True:
    playerinput = input("What do?").lower()
    if playerinput == 'menu':
        GameMenu.main_menu()
    elif playerinput == "name":
        GameMenu.new_char()
    elif "look" in playerinput:
        Movement.look_around()
    elif playerinput == 'quit':
        break
    elif re.match('^[nsew][0-9]+$',playerinput) or playerinput == 'map':
        Movement.where_to()