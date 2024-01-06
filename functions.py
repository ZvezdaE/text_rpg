
def decompose(x: int, divider: int = 8) -> list:
    """Create and return a list of the 2^n values that make up x."""
    __number_list = []
    while divider >= 1:
        if x % divider < x:
            __number_list.insert(0,int(divider))
            x -= divider
        divider = divider / 2
    return __number_list

def reverse_paths(x: int, bitSize: int = 4) -> int:
    __binary = bin(x)
    __reverse = __binary[-1:1:-1]
    __reverse = __reverse + (bitSize - len(__reverse))*'0'

    return int(__reverse,2)

def base_2_direction(direction: int) -> str:
        """Transform the path int into text."""
        if direction == 1:
            return "North"
        if direction == 2:
            return "West"
        if direction == 4:
            return "East"
        if direction == 8:
            return "South"