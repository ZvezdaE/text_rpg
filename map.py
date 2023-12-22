
from data_types import point
from tile import tile


class map:

    def __init__(self):
        __initial_point = point(0,0)
        self.map_dict = {__initial_point : tile(__initial_point)}

    def get_tile(self, tile_loc: point):
        return self.map_dict[tile_loc]
    
    def add_tile(self, tile_loc: point) -> None:
        if not self.check_tile(tile_loc):
            self.map_dict[tile_loc] = tile(tile_loc)

    def check_tile(self, tile_loc : point) -> bool:
        return tile_loc in self.map_dict