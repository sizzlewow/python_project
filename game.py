import time
import numpy as np
from helper import utilities



class BuildCharacter():

    def playername():
        player = input('\nwhat is your name?')
        output = ("Time to pick up the pieces, " + player + "\n")
        utilities.slowPrint(output)
    
                
class Movement():
    
    def where_to():
        from world import buildMap
        mapMatrix = buildMap.assign_tiles()
        tile = buildMap.tile_dict()
        print(buildMap.assign_tiles())
        x = 1
        y = 1

        while True: 
            playermap = np.copy(mapMatrix)
            traverse = input("\n[which direction and how far? (n,s,e,w)]")
            if traverse == "n":
                y -= 1
                location = (tile[direction].start_text())
                print(location)
                utilities.slowPrint(location)
                if (y < 1):
                    location = (tile[direction].start_text())
                    utilities.slowPrint(location)
                    y +=1

                else:
                    direction = (mapMatrix[y, x])
                    print(direction)
                    print(y, x)
                    location = (tile[direction].start_text())
                    utilities.slowPrint(location)
            elif traverse == "s":
                y += 1
                if (y > 3):
                    location = (tile[direction].start_text())
                    utilities.slowPrint(location)                    
                    y -= 1

                else:        
                    direction = (mapMatrix[y, x])
                    print(0 <= int(y) <= 2)
                    print(direction)
                    print(y, x)
                    location = (tile[direction].start_text())
                    utilities.slowPrint(location)
            elif traverse == "w":
                x -= 1
                if (x < 1):
                    location = (tile[direction].start_text())
                    utilities.slowPrint(location)                    
                    x += 1

                else:
                    direction = (mapMatrix[y, x])
                    print(direction)
                    print(y, x)
                    location = (tile[direction].start_text())
                    utilities.slowPrint(location)
            elif traverse == "e":
                x += 1
                if (x > 5):
                    location = (tile[direction].start_text())
                    utilities.slowPrint(location)                    
                    x -= 1

                else:
                    direction = (mapMatrix[y, x])
                    print(direction)
                    print(y, x)
                    location = (tile[direction].start_text())
                    utilities.slowPrint(location)
            elif traverse == "map":
                playermap[y,x]="O"
                print(mapMatrix)
                print(playermap)
                print(mapMatrix.shape)
                playermap = None
            else:
                print ("invalid direction")        

Movement.where_to()  
        
        # mapMatrix = buildMap.assign_tiles()
        # tile = buildMap.tile_dict()
        # print(buildMap.assign_tiles())
        # x = 0
        # y = 1
        # traverse = input("\n[which way (n,s,e,w)]")
        # while True:
        #     traverse = input("\n[which way (n,s,e,w)]")
        #     if traverse == "n":
        #         y -= 1
        #         direction = (mapMatrix[y, x])
        #         print(direction)
        #         location = (tile[direction].start_text())
        #         output = utilities.slowPrint(location)
        #     elif traverse == "s":
        #         y += 1
        #         direction = (mapMatrix[y, x])
        #         print(direction)
        #         location = (tile[direction].start_text())
        #         output = utilities.slowPrint(location)
        #     elif traverse == "w":
        #         x -= 1
        #         direction = (mapMatrix[y, x])
        #         print(direction)
        #         location = (tile[direction].start_text())
        #         output = utilities.slowPrint(location)
        #     elif traverse == "e":
        #         x += 1
        #         direction = (mapMatrix[y, x])
        #         print(direction)
        #         location = (tile[direction].start_text())
        #         output = utilities.slowPrint(location)
        #     elif traverse == "map":
        #         print(mapMatrix)
        #     else:
        #         output = "invalid direction"
        #         utilities.slowPrint(output)
            