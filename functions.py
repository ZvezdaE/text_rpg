
def decompose(x: int, divider: int = 8) -> list:
    """Create and return a list of the 2^n values that make up x."""
    number_list = []
    while divider >= 1:
        if x % divider < x:
            number_list.insert(0,int(divider))
            x -= divider
        divider = divider / 2
    return number_list

def reverse_paths(x: int, bitSize: int = 4) -> int:
    binary = bin(x)
    reverse = binary[-1:1:-1]
    reverse = reverse + (bitSize - len(reverse))*'0'

    return int(reverse,2)

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