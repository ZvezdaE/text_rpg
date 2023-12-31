import random
#from tile import tile
from functions import decompose
#from functions import reverse_paths
from data_types import point
#from Paths import paths
from map import map



z = map()

print(z.get_tile_description())
x  = True
while x:
    direct = input("What direction would you like to travel? ")
    if direct == "n":
        print(z.move_north())
    elif direct == "s":
        print(z.move_south())
    elif direct == "e":
        print(z.move_east())
    elif direct == "w":
        print(z.move_west())
    elif direct == "exit":
        x = False
    else:
        print("That is not a valid command")
