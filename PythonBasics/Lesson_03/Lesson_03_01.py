def my_func(a, b):
    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        print(a, "or", b, "is not float")
        return
    if float(b) == 0:
        print("division by zero")
    else:
        return float(a) / float(b)


a = input("Enter a ")
b = input("Enter b ")

print(my_func(a, b))
