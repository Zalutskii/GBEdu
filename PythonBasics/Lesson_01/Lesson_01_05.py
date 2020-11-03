profit = input("Enter the profit ")
loss = input("Enter the loss ")

if profit.replace('.', '', 1).isdigit() & loss.replace('.', '', 1).isdigit():
    profit = float(profit)
    costs = float(loss)
    if profit > costs:
        print("You have a profit ", profit-costs)
        persons = input("Enter the number of people ")
        if persons.isdigit():
            persons = int(persons)
            print("You have a profit ", profit/persons, " on person")
        else:
            print(persons, "is not int")
    elif profit < costs:
        print("You have a loss ", costs - profit)

else:
    print(profit, "or", loss, "is not float")
