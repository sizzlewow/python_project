# Importing external modules
# numpy to build playermap
# helper for utility functions to improve ui
# player for user data and state

import numpy as np
from helper import utilities
from player import user




# class BuildCharacter():

#     def playername():
#         user(input('\nwhat is your name?'))
#         output = ("Time to pick up the pieces, " +  + "\n")
#         utilities.slowPrint(output)
    
                
class Movement():

    last_loc = None
    
    def where_to():
        from world import buildMap
        mapMatrix = buildMap.assign_tiles() # 2d Array used for game map
        tile = buildMap.tile_dict() # Dictionary containing worldmap class names and abbreviated keys.
        y, x = user.y, user.x # Player starting coords, stored in player module
        location = (mapMatrix[y, x]) # Abbreviated tile name on map.

        while True:
            playermap = np.copy(mapMatrix) # Copy of worldmap updated to show player location.
            choice = input("\n[which location (n,s,e,w)]")

            if choice == "n":
                y -= 1
                if (y < 1):
                    location = (mapMatrix[y, x])
                    tile[location].start() 
                    y +=1

                else:
                    location = (mapMatrix[y, x])
                    tile[location].start()

            elif choice == "s":
                y += 1
                if (y > mapMatrix.shape[0]-2):
                    location = (mapMatrix[y, x])
                    tile[location].start()                  
                    y -= 1

                else:        
                    location = (mapMatrix[y, x])
                    tile[location].start()
 
            elif choice == "w":
                x -= 1
                if (x < 1):
                    location = (mapMatrix[y, x])
                    tile[location].start()
                    x += 1

                else:
                    location = (mapMatrix[y, x])
                    tile[location].start()
            elif choice == "e":
                x += 1
                if (x > mapMatrix.shape[1]-2):
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
                print ("invalid location")

            