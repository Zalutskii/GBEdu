my_list1 = [7, 5, 3, 3, 2]
num = input("Input number ")

if num.isdigit():
    val = int(num)
    if my_list1[-1] > val:
        my_list1.append(val)
    else:
        for i in range(0, len(my_list1), 1):
            if my_list1[i] < val:
                my_list1.insert(i, val)
                break
    print("1 example")
    print(my_list1)
else:
    print(num, "is not int")

