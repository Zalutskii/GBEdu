value = input("Enter the number N")
if value.isdigit():
    value = int(value)
    new_value = 0
    counter = 1
    while (value//counter) > 0:
        counter *= 10
        num = value % counter
        num = num // (counter/10)
        if num > new_value:
            new_value = num
    print("max value", new_value)
else:
    print(value, "is not int")
