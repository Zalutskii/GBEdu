users = {}
with open('Lesson_05_03_1.txt') as file_:
    for line in file_:
        str1 = line.split(";")
        users[str1[0]] = int(str1[1])

print("This persons has less then 20000:", " ".join(user for user, price in users.items() if price < 20000))
print("Average = ", sum([price for user, price in users.items()])/len(users))
