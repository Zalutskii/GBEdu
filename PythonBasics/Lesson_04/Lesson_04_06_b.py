from sys import argv
from itertools import cycle


for i, out in enumerate(cycle(argv[1:])):
    print(out)
    if i > 10:
        break
