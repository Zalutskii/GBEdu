value = input("Enter the number of seconds ")
if value.isdigit():
    value = int(value)
    hh = value // 3600
    mm = (value % 3600) // 60
    ss = value % 60
    print('{:02}:{:02}:{:02}'.format(hh, mm, ss))
else:
    print(value, "is not int")
