import time
import numpy as np
from helper import utilities
from player import user




# class BuildCharacter():

#     def playername():
#         user(input('\nwhat is your name?'))
#         output = ("Time to pick up the pieces, " +  + "\n")
#         utilities.slowPrint(output)
    
                
class Movement():
    
    def where_to():
        from world import buildMap
        mapMatrix = buildMap.assign_tiles()
        tile = buildMap.tile_dict()
        # print(buildMap.assign_tiles())
        y, x = user.y, user.x
        location = (mapMatrix[y, x])
        print(user.y, user.x)

        while True:
            playermap = np.copy(mapMatrix)
            choice = input("\n[which location (n,s,e,w)]")

            if choice == "n": 
                y -= 1
                if (y < 1):
                    location = (mapMatrix[y, x])
                    output = (tile[location].start_text())
                    utilities.slowPrint(output)
                    y +=1

                else:
                    location = (mapMatrix[y, x])
                    # print(location)
                    output = (tile[location].start_text())
                    utilities.slowPrint(output)
            elif choice == "s":
                y += 1
                if (y > mapMatrix.shape[0]-2):
                    location = (mapMatrix[y, x])
                    output = (tile[location].start_text())
                    utilities.slowPrint(output)                   
                    y -= 1

                else:        
                    location = (mapMatrix[y, x])
                    output = (tile[location].start_text())
                    utilities.slowPrint(output)
            elif choice == "w":
                x -= 1
                if (x < 1):
                    location = (mapMatrix[y, x])
                    output = (tile[location].start_text())
                    utilities.slowPrint(output)                   
                    x += 1

                else:
                    location = (mapMatrix[y, x])
                    output = (tile[location].start_text())
                    utilities.slowPrint(output)
            elif choice == "e":
                x += 1
                if (x > mapMatrix.shape[1]-2):
                    location = (mapMatrix[y, x])
                    output = (tile[location].start_text())
                    utilities.slowPrint(output)                    
                    x -= 1

                else:
                    location = (mapMatrix[y, x])
                    output = (tile[location].start_text())
                    utilities.slowPrint(output)
            elif choice == "map":
                playermap[y,x]="O"
                print(playermap)
                playermap = None
            else:
                print ("invalid location")

            