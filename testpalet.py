import numpy as np
from numpy import ndindex
from world import *
from game import *


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
    
mapMatrix = assign_tiles()
matrixdim = mapMatrix.shape
y_end = matrixdim[0]
x_end = matrixdim[1]
tile = tile_dict()
x = 1
y = 1

while True: 
    playermap = np.copy(mapMatrix)
    traverse = input("\n[which way (n,s,e,w)]")
    if traverse == "n":
        y -= 1
        if (y < 1):
            y +=1
            location = (tile[direction].start())
            utilities.slowPrint(location)
        else:
            direction = (mapMatrix[y, x])
            print(direction)
            print(y, x)
            location = (tile[direction].start())
            utilities.slowPrint(location)
    elif traverse == "s":
        y += 1
        if (y > 3):
            y -= 1
            location = (tile[direction].start())
            utilities.slowPrint(location)
        else:        
            direction = (mapMatrix[y, x])
            print(0 <= int(y) <= 2)
            print(direction)
            print(y, x)
            location = (tile[direction].start())
            utilities.slowPrint(location)
    elif traverse == "w":
        x -= 1
        if (x < 1):
            x += 1
            location = (tile[direction].start())
            utilities.slowPrint(location)
        else:
            direction = (mapMatrix[y, x])
            print(direction)
            print(y, x)
            location = (tile[direction].start())
            utilities.slowPrint(location)
    elif traverse == "e":
        x += 1
        if (x > 5):
            x -= 1
            location = (tile[direction].start())
            utilities.slowPrint(location)
        else:
            direction = (mapMatrix[y, x])
            print(direction)
            print(y, x)
            location = (tile[direction].start())
            utilities.slowPrint(location)
    elif traverse == "map":
        playermap[y,x]="O"
        print(mapMatrix)
        print(playermap)
        print(mapMatrix.shape)
        playermap = None
    else:
        print ("invalid direction")
# else:
#     if (y > 3):
#         y -= 1
#         print("There's a wall here.")
#     elif (y < 1):
#         y +=1
#         print("There's a wall here.")
#     elif (x > 4):
#         x -= 1
#         print("There's a wall here.")
#     elif (x < 1):
#         x += 1
#         print("There's a wall here.")
##  need to limit movement to within range of array and prevent loopback.