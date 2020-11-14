import json


dic_1 = {}
with open('Lesson_05_07_1.txt', 'r') as file_:
    for line in file_:
        split_line = line.split(" ")
        dic_1[split_line[0]] = int(split_line[2]) - int(split_line[3])

for firm, t in dic_1.items():
    print(f"Profit company {firm} = {t}")

new_dic = {k: t for k, t in dic_1.items() if t > 0}
avr = sum(t for firm, t in new_dic.items())/len(new_dic)
print("Average =", avr)

l = [dic_1, {"average_profit", avr}]

print(l)

with open("Lesson_05_07_1.json", 'w+') as outfile:
    json.dump(str(l), outfile)


