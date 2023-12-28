import random
from tile import tile
from functions import decompose
from functions import reverse_paths
from data_types import point
from Paths import paths

z = tile()

print(z.get_paths())
print(z.get_enviro())
print(z.get_enviro_text())

z.set_paths(6)
z.set_environ(2)

print(z.get_paths())
print(z.get_enviro())
print(z.get_enviro_text())
