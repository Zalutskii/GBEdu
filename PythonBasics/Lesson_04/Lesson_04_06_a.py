from sys import argv
from itertools import count


if len(argv) != 2:
    print('Number of arguments is not 2, input start value and end value')
elif not all(arg.isdigit() for arg in argv[1:]):
    print('Not all args is int')
else:
    for i, out in enumerate(count(int(argv[1]))):
        print(out)
        if i > 10:
            break
