"""
The main class for managing the map dictionary. 
"""
from data_types import point
from tile import Tile
from functions import base_2_direction
from functions import reverse_paths

class Map():

    def __init__(self):

        self.current_loc = point(0,0)
        self.map_dict = {self.current_loc : Tile()}
        self.travel = 0

    def get_tile(self, tile_loc: point):
        
        return self.map_dict[tile_loc]
    
    def get_tile_description(self) -> str:

        return self.get_tile(self.current_loc).get_tile_description()
    
    def add_tile(self, tile_loc: point) -> None:
        
        if not self.check_tile(tile_loc):
            path_list, exclude_list, environ = self.__surrounding_tiles(self.current_loc)
            self.map_dict[tile_loc] = Tile(self.travel, path_list, exclude_list, environ)

    def set_location(self, loc: point) -> None:
        self.current_loc = loc

    def check_tile(self, tile_loc : point) -> bool:
        
        return tile_loc in self.map_dict
    
    def __surrounding_tiles(self, tile_loc : point) -> tuple[int, int, list]:
        #---------------------------------------------------------------
        # This function does a tile check on the 4 tiles surrounding a point 
        # and if there is a tile that has been generated will return the
        # directions of paths that lead to/from the initial tile, any directions
        # where paths should not be due to a tile without a path leading 
        # to/from the initial path as well as the number of each environment
        # type of all the surrounding fields.
        #---------------------------------------------------------------
        
        shift_list = [point(0,1), point(-1,0), point(1,0), point(0,-1)]
        environ_extra_loc = [point(1,1), point(-1,1), point(1,-1), point(-1,-1)]
        lookup_list = [8,4,2,1]
        path_list = 0
        path_exclude = 0
        environ_list = [0,0,0]

        for x in range(len(shift_list)):
            temp_loc = tile_loc + shift_list[x]
            if self.check_tile(temp_loc):
                temp_tile = self.get_tile(temp_loc)

                if lookup_list[x] in temp_tile.get_paths():
                    path_list += lookup_list[x]
                else:
                    path_exclude += lookup_list[x]
                environ_list[temp_tile.get_enviro()] += 1

        for x in range(len(environ_extra_loc)):
            temp_loc = tile_loc + shift_list[x]
            if self.check_tile(temp_loc):
                environ_list[temp_tile.get_enviro()] += 1

        print("Environment list: ", environ_list)
        return reverse_paths(path_list), reverse_paths(path_exclude) ,environ_list
    
    def __move(self, direction : int, move_direct: point) -> str:

        if direction not in self.get_tile(self.current_loc).get_paths():
            return "There is no path in that direction."
        else:
            self.current_loc += move_direct

        if not self.check_tile(self.current_loc):
            if self.travel < 97:
                self.travel += 1
            
            self.add_tile(self.current_loc)
            if self.get_tile(self.current_loc).get_town():
                self.travel = 0
            
        return "You travel to the " + base_2_direction(direction) + ".\n" + self.get_tile(self.current_loc).get_tile_description()

    def move_north(self):
        return self.__move(1, point(0,1))
            
    def move_south(self):
        return self.__move(8, point(0,-1))

    def move_east(self):
        return self.__move(4, point(1,0))

    def move_west(self):
        return self.__move(2, point(-1,0))