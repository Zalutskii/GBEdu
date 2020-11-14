dic_1 = {}
with open('Lesson_05_06_1.txt', encoding='cp1251') as file_:
    for line in file_:
        split_line = line.split(" ")
        str1 = [''.join([i for i in item if i.isdigit()]) for item in split_line[1:]]
        dic_1[split_line[0].replace(":", "")] = int(sum(int(i) for i in str1 if i.isdigit()))

print(dic_1)
