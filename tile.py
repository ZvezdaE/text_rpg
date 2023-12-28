
import random
from data_types import point
from Paths import paths
from environment import environ
from functions import decompose

class tile(paths, environ):
    def __init__(self,  travel: int = 0, path_list: int = 0, exclude_list: int = 0, 
                 enviro_list: list = [0,0,0]) -> None:
        paths.__init__(self, path_list, exclude_list)
        environ.__init__(self, enviro_list)

        self.town = 0

        if random.random() > 0.97 - (travel/100):
            self.town = 1

    def get_town(self) -> int:
        return self.town

    def get_enviro(self) -> int:
        return environ.get_enviro(self)
    
    def get_paths(self) -> list:
        return paths.get_paths(self)
    