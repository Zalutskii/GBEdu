def my_func(*args):
    l = list(args)
    l.sort()
    return l[-1] + l[-2]


a1 = input("Enter a1 ")
a2 = input("Enter a2 ")
a3 = input("Enter a3 ")

if not a1.isdigit() or not a2.isdigit() or not a3.isdigit():
    print(a1, "or", a2, "or", a3, "is not int")
else:
    print("sum of max 2 = ", my_func(int(a1), int(a2), int(a3)))
