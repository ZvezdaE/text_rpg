
def decompose(x: int, divider: int = 8) -> list:
    """Create and return a list of the 2^n values that make up x."""
    __number_list = []
    while divider >= 1:
        if x % divider < x:
            __number_list.insert(0,int(divider))
            x -= divider
        divider = divider / 2
    return __number_list

def reverse_paths(x: int) -> int:
    __binary = bin(x)
    __reverse = __binary[-1:1:-1]

    return int(__reverse,2)