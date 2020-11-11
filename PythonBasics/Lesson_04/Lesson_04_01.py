from sys import argv


def my_func(time, price, bonus):
    return time * price + bonus


print('args', argv)
if len(argv) != 4:
    print('Number of arguments is not 3')
elif not all(arg.isdigit() for arg in argv[1:]):
    print('Not all args is float')
else:
    print(my_func(float(argv[1]), float(argv[2]), float(argv[3])))
