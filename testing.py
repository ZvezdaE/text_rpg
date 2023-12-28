from tile import tile
from functions import decompose
from functions import reverse_paths
from data_types import point
from Paths import paths


z = tile(point(0,0), 0, 15, 0, )

print(z.get_paths(), z.get_enviro(), z.get_town())