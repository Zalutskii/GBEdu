value_list = [1, True, 3.14, 4]
type_list = [type(1), type(True), type(3.14), type(False)]

for i in range(4):
    print("Type 1 =", type(value_list[i]), "Type 2 =", type_list[i], "is the same type?", type(value_list[i]) == type_list[i])
