
from data_types import point
import random
from functions import decompose
from functions import base_2_direction

class paths():
#---------------------------------------------------------------
# A class to manage the paths on a tile.
# directions are indicated by 
# 1 is North
# 2 is West
# 4 is East
# 8 is South
#----------------------------------------------------------------
    def __init__(self, path_list: int = 0 , exclude_list : int = 0) -> None:
        __key = random.randint(1,15)
        #print("Paths Rolled: ", decompose(__key))
        __key = __key | path_list
        __key = ~exclude_list & __key
        self.paths = decompose(__key,8)

    def get_paths(self) -> list:
        return self.paths
    
    def set_paths(self, path_list: int) -> None:
        self.paths = decompose(path_list)

    def get_path_text(self) -> str:

        __path_names = []
        for x in self.paths:
            __path_names.append(base_2_direction(x))
        if len(self.paths) == 1:
            __path_string = "There is a path heading to the " + __path_names[0]
        else:
            __path_string = "There are paths heading to the "
            for y in __path_names:
                __path_string += y
                if y == __path_names[-2]:
                    __path_string += " and "
                elif y == __path_names[-1]:
                    __path_string += "."
                else:
                    __path_string += ", "
        
        return __path_string
