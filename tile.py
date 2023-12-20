
import random
from data_types import paths

class tile_element(paths):
    def __init__(self, travel: int = 0, path_list = [0,0,0,0]):
        super().__init__(path_list)
        self.town = 0

        #

        if random.random() > 0.97 - (travel/100):
            self.town = 1
        

