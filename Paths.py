
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
    def __init__(self, path_list = [0,0,0,0]):
        __key = random.randint(1,14)
        self.paths = decompose(__key,8)

    def get_paths(self):
        return self.paths