
from data_types import point
import random
from functions import decompose

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
        __key = random.randint(1,14)
        __key = __key | path_list
        __key = ~exclude_list & __key
        self.paths = decompose(__key,8)

    def get_paths(self) -> list:
        return self.paths
    
    