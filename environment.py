
import random

class environ():

    def __init__(self):
        __environ_rand = random.random()
        if __environ_rand < 0.33:
            self.enviro = 0
        elif __environ_rand < 0.66:
            self.enviro = 1
        else:
            self.enviro = 2

    def get_enviro(self):
        return self.enviro