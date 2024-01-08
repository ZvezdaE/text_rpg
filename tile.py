
import random
from data_types import point
from Paths import Paths
from environment import Environ
from functions import decompose

class Tile(Paths, Environ):
    def __init__(self,  
                 travel: int = 0, 
                 path_list: int = 0, 
                 exclude_list: int = 0, 
                 enviro_list: list = [0,0,0]
                 ) -> None:
        Paths.__init__(self, path_list, exclude_list)
        #print("Tile Path List: ", decompose(path_list))
        #print("Tile Exclude", decompose(exclude_list))
        #print("Environ List: ", enviro_list)
        #print("Paths: ", self.paths)
        #print("Travel: ", travel)
        Environ.__init__(self, enviro_list)

        self.town = 0
        
        if travel > 97:
            travel = 97
        
        if random.random() > 0.97 - (travel/100):
            self.town = 1

    def __str__(self) -> str:
        environ = self.get_enviro_text()
        paths = self.get_path_text()
        town = self.__town_text()

        return environ + "\n" + paths + "\n" + town
    
    def get_town(self) -> int:

        return self.town

    def get_enviro(self) -> int:
        
        return super().get_enviro()
    
    def get_paths(self) -> list:
        
        return super().get_paths()
    
    def get_tile_description(self) -> str:
        environ = self.get_enviro_text()
        paths = self.get_path_text()
        town = self.__town_text()

        return environ + "\n" + paths + "\n" + town
    
    def __town_text(self) -> str:

        if self.town:
            return "You see a small town in the distance."
        else:
            return ""
        
    