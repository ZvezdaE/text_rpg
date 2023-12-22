
from data_types import point
from tile import tile


class map:

    def __init__(self):
        __initial_point = point(0,0)
        self.map_dict = {__initial_point : tile(__initial_point)}

    get