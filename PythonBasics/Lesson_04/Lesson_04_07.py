def my_func(start):
    val = 1
    for i in range(1, start):
        val = val * i
        yield val


arg = input("Enter int value ")
if not arg.isdigit():
    print('args is not int')
else:
    for out in my_func(int(arg)):
        print(out)



