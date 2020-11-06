res = 0
exit_while = True
while exit_while:
    input_str = input("add new items (q for Exit)")
    for value in input_str.split(" "):
        if value.isdigit():
            res = res + int(value)
        elif value == "q":
            exit_while = False
            break
        else:
            print(value, "is not int")
    print(res)

