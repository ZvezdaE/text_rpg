#------------------------------------------------------------------
# Classes for managing custom datatypes.
# 
# ----------------------------------------------------------------- 
import random
from binary_decompose import decompose

'''
A class to manage the location(point) on the grid
'''    
class point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        """Create a point object with the provided coordinates."""
        self.__x = x
        self.__y = y

    def __hash__(self):
        """Create a hash value of the object, use in dictionaries."""
        return hash((self.__x, self.__y))

    def __eq__(self, comp_point):
        """Check if 2 points are equal to each other."""
        return (self.__x, self.__y) == (comp_point.__x, comp_point.__y)

    def __ne__(self, comp_point):
        """Check if 2 points are not equal to each other"""
        return not(self == comp_point)

    def get_x(self):
        """Return the x coordinate of the point."""
        return self.__x

    def get_y(self):
        """Returns the y coordinate of the point."""
        return self.__y

    def set_x(self, x: int):
        """Make a change to the x value of the point."""
        self.__x = x
    
    def set_y(self, y: int):
        """Make a change to the y value of the point"""
        self.__y = y

    def __str__(self):
        """Define how the point will be displayed using the Print function"""
        return "[" + str(self.get_x()) + "," + str(self.get_y()) + "]"

    def __add__(self, other_point):
        """Add x and y values to the point"""
        other_point.__x = self.__x + other_point.__x
        other_point.__y = self.__y + other_point.__y

        return other_point

    def __sub__(self, other_point):
        """Subtract x and y values from the point"""
        other_point.__x = self.__x - other_point.__x
        other_point.__y = self.__y - other_point.__y

        return other_point

    def move(self, x: int = 0, y: int = 0):
        self.__x += x
        self.__y += y

class paths:
#---------------------------------------------------------------
# A class to manage the paths on a tile.
# directions are indicated by 
# 1 is North
# 2 is West
# 4 is East
# 8 is South
#----------------------------------------------------------------
    def __init__(self, path_list = [0,0,0,0]):
        __key = random.randint(1,14)
        self.paths = decompose(__key,8)

    def get_paths(self):
        return self.paths