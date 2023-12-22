
import random
from data_types import point
from Paths import paths
from environment import environ
from functions import decompose

class tile(paths, environ):
    def __init__(self, loc: point = point(0,0), travel: int = 0, path_list: list = [0,0,0,0]) -> list:
        paths.__init__(self)
        environ.__init__(self)

        self.town = 0

        if random.random() > 0.97 - (travel/100):
            self.town = 1

    def get_town(self):
        return self.town