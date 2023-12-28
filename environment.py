
import random

class environ():

    def __init__(self, enviro_list: list = [0,0,0]) -> None:
        __environ_rand = random.random()
        
        __grass_value = (1 + enviro_list[0]) ** enviro_list[0]
        __forest_value = (1 + enviro_list[1]) ** enviro_list[1]
        __mount_value = (1 + enviro_list[2]) ** enviro_list[2]
        __total_env = __grass_value + __forest_value + __mount_value
        __environ_rand = random.random()
        if __environ_rand < __grass_value/__total_env:
            self.environ = 0
        elif __environ_rand > __mount_value/__total_env:
            self.environ = 2
        else:
            self.environ = 1

    def get_enviro(self):
        return self.enviro