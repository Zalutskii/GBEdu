dict_1 = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("Lesson_05_04_1.txt", "r") as file_:
    text = file_.read()

for t1, t2 in dict_1.items():
    text = text.replace(t1, t2)

with open("Lesson_05_04_2.txt", "w+") as file_:
    file_.write(text)