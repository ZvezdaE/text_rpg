
from data_types import point
import random
from functions import decompose
from functions import base_2_direction

class Paths():
#---------------------------------------------------------------
# A class to manage the paths on a tile.
# directions are indicated by 
# 1 is North
# 2 is West
# 4 is East
# 8 is South
#----------------------------------------------------------------
    def __init__(self, path_list: int = 0 , exclude_list : int = 0) -> None:
        key = random.randint(1,15)
        #print("Paths Rolled: ", decompose(__key))
        key = key | path_list
        key = ~exclude_list & key
        self.paths = decompose(key,8)

    def get_paths(self) -> list:
        return self.paths
    
    def set_paths(self, path_list: int) -> None:
        self.paths = decompose(path_list)

    def get_path_text(self) -> str:

        path_names = []
        for x in self.paths:
            path_names.append(base_2_direction(x))
        if len(self.paths) == 1:
            path_string = "There is a path heading to the " + path_names[0]
        else:
            path_string = "There are paths heading to the "
            for y in path_names:
                path_string += y
                if y == path_names[-2]:
                    path_string += " and "
                elif y == path_names[-1]:
                    path_string += "."
                else:
                    path_string += ", "
        
        return path_string
