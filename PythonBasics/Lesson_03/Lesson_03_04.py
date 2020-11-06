def my_func(a, b):
    res = 1
    for i in range(abs(b)):
        res = res * a

    if b < 0:
        return 1/res
    else:
        return res


x = input("Enter x ")
y = input("Enter y ")

if not x.replace('.', '', 1).isdigit() or not y.replace("-", "", 1).isdigit():
    print(x, "is not float", "or", y, "is not int")
else:
    print(f"{x}^{y}= {my_func(float(x), int(y))}")
    print(f"{x}^{y}= {float(x)**int(y)}")
