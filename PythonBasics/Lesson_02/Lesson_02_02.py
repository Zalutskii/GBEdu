value_list = []
while True:
    input_str = input("add new item (q for Exit)")
    if input_str == "q":
        break
    else:
        value_list.append(input_str)

for i in range(0, len(value_list) - 1, 2):
    value_list[i], value_list[i + 1] = value_list[i + 1], value_list[i]

print(value_list)
