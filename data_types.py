#------------------------------------------------------------------
# Classes for managing custom datatypes.
# 
# ----------------------------------------------------------------- 
import random
from functions import decompose

'''
A class to manage the location(point) on the grid
'''    
class point():
    def __init__(self, x: int = 0, y: int = 0) -> None:
        """Create a point object with the provided coordinates."""
        self.x = x
        self.y = y

    def __hash__(self):
        """Create a hash value of the object, use in dictionaries."""
        return hash((self.x, self.y))

    def __eq__(self, comp_point: "point") -> "point":
        """Check if 2 points are equal to each other."""
        return (self.x, self.y) == (comp_point.x, comp_point.y)

    def __ne__(self, comp_point: "point") -> bool:
        """Check if 2 points are not equal to each other"""
        return not(self == comp_point)

    def get_x(self) -> int:
        """Return the x coordinate of the point."""
        return self.x

    def get_y(self) -> int:
        """Returns the y coordinate of the point."""
        return self.y

    def set_x(self, x: int) -> None:
        """Make a change to the x value of the point."""
        self.x = x
    
    def set_y(self, y: int) -> None:
        """Make a change to the y value of the point"""
        self.y = y

    def __str__(self) -> str:
        """Define how the point will be displayed using the Print function"""
        return "[" + str(self.get_x()) + "," + str(self.get_y()) + "]"

    def __add__(self, other_point: "point") -> "point":
        """Add x and y values to the point"""
        other_point.__x = self.x + other_point.__x
        other_point.__y = self.y + other_point.__y

        return other_point

    def __sub__(self, other_point: "point") -> "point":
        """Subtract x and y values from the point"""
        other_point.__x = self.x - other_point.__x
        other_point.__y = self.y - other_point.__y

        return other_point

    def move(self, x: int = 0, y: int = 0) -> None:
        self.x += x
        self.y += y

