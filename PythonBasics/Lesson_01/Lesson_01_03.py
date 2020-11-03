value = input("Enter the number N ")
# ----------------------1--------------------------
if value.isdigit():
    new_value = int(value)
    print("new value", new_value*123)
else:
    print(value, "is not int")

# ----------------------2--------------------------
if value.isdigit():
    new_value = int(value)
    new_value += int(value*2)
    new_value += int(value*3)
    print("new value", new_value)
else:
    print(value, "is not int")
