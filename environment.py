
import random

class Environ():
    #---------------------------------------------------------------
    # A class to manage the environment for a tile. A tile can have
    # one of 3 types of environment:
    # 0 - Grass
    # 1 - Forest
    # 2 - Mountains
    # Which environment is chosen for a tile is randomly chosen but
    # the chance is impacted by the surrounding tiles.
    #---------------------------------------------------------------
    def __init__(self, enviro_list: list = [0,0,0]) -> None:
        
        grass_value = (1 + enviro_list[0]) ** enviro_list[0]
        forest_value = (1 + enviro_list[1]) ** enviro_list[1]
        mount_value = (1 + enviro_list[2]) ** enviro_list[2]
        total_env = grass_value + forest_value + mount_value
        environ_rand = random.random()

        if environ_rand < grass_value/total_env:
            self.environ = 0
        elif environ_rand > 1 - mount_value/total_env:
            self.environ = 2
        else:
            self.environ = 1

    def get_enviro(self) -> int:
        
        return self.environ
    
    def set_environ(self, enviro: int) -> None:
        
        self.environ = enviro

    def get_enviro_text(self) -> str:
        
        if self.environ == 0:
            return "You are standing on a grassy plain."
        if self.environ == 1:
            return "You are standing in a dark forest."
        if self.environ == 2:
            return "You are standing amoung mighty mountains."