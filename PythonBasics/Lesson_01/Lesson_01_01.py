value = 1
print(type(value), value)

value = True
print(type(value), value)

value = 1.1
print(type(value), value)

value = "str str "
print(type(value), value)

value = input("Input value = ")
if value.isdigit():
    value = int(value)
print(type(value), value)
