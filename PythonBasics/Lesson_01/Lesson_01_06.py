a = input("Enter a ")
b = input("Enter b ")

if a.replace('.', '', 1).isdigit() & b.replace('.', '', 1).isdigit():
    a = float(a)
    b = float(b)
    counter = 1
    while a < b:
        a += a * 0.1
        counter += 1
    print("result ", a, "on ", counter, " day")
else:
    print(a, "or", b, "is not float")
