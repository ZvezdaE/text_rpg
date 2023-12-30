"""
The main class for managing the map dictionary. 
"""
from data_types import point
from tile import tile

class map:

    def __init__(self):
        
        self.current_loc = point(0,0)
        self.map_dict = {self.current_loc : tile()}
        self.travel = 0

    def get_tile(self, tile_loc: point):
        
        return self.map_dict[tile_loc]
    
    def add_tile(self, tile_loc: point) -> None:
        
        if not self.check_tile(tile_loc):
            self.map_dict[tile_loc] = tile(self.travel)

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
        
        __shift_list = [point(0,1), point(-1,0), point(1,0), point(0,-1)]
        __lookup_list = [8,4,2,1]
        __path_list = 0
        __path_exclude = 0
        __environ_list = [0,0,0]

        for __x in range(len(__shift_list)):
            __temp_tile = self.get_tile(tile_loc + __shift_list[__x])
            if self.check_tile(__temp_tile):
                if __lookup_list[__x] in __temp_tile.get_paths():
                    __path_list + __lookup_list[__x]
                else:
                    __path_exclude + __lookup_list[__x]
                __environ_list[__temp_tile.get_enviro()] + 1

        return __path_list, __path_exclude ,__environ_list
    
        def __move(self, direction : int, move_direct: point) -> str:

            if direction not in self.get_tile(self.current_loc).get_paths():
                 return "There is no path in that direction."
            else:
                self.current_loc += move_direct
            
            return None

        def move_north(self):
            if 1 not in self.get_paths():
                return "There is no path in that direction."
            else:
                self.current_loc += point(0,1)

                if self.check_tile(self.current_loc):
                    return self.get_tile(self.current_loc).get_tile_description()
                else:
                    if self.travel <=97:
                        self.travel += 1
                    else:
                        self.travel = 0
                    self.add_tile(self.current_loc)

        def move_south(self):
            return self.__move(8, point(0,-1))

        def move_east(self):
            if 4 not in self.get_paths():
                return "There is no path in that direction."

        def move_west(self):
            if 2 not in self.get_paths():
                return "There is no path in that direction."