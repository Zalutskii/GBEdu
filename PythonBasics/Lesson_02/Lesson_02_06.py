value_list = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]

while True:
    print("Add new item")
    name = input("Input name (q for Exit) ")
    if name == "q":
        break
    price = input("Input price (q for Exit) ")
    if price == "q":
        break
    if not price.isdigit():
        print(price, "is not int")
        break
    quantity = input("Input quantity (q for Exit) ")
    if quantity == "q":
        break
    if not quantity.isdigit():
        print(quantity, "is not int")
        break
    unit = input("Input unit (q for Exit) ")
    if unit == "q":
        break

    value_list.append((len(value_list), {"название": name, "цена": price, "количество": quantity, "eд": unit}))
print("----------------------------------------------------------------")
print(value_list)
print("----------------------------------------------------------------")
dic_stat = {
    "название": [dic["название"] for num, dic in value_list],
    "цена": [dic["цена"] for num, dic in value_list],
    "количество": [dic["количество"] for num, dic in value_list],
    "eд": [dic["eд"] for num, dic in value_list]
}

print(dic_stat)
