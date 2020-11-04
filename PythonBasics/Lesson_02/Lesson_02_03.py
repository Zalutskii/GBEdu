month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
month_dic = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}

num = input("Input number of month ")
if num.isdigit():
    num = int(num)
    if num > 0 & num < 12:
        print("Month from list", month_list[num - 1])
        print("Month from dictionary", month_dic[num])
    else:
        print(num, "is not in range 0..12")
else:
    print(num, "is not int")
