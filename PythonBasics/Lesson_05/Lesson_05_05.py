with open("Lesson_05_05_1.txt", "w+") as f:
    f.write(" ".join(str(num) for num in range(10)))
with open("Lesson_05_05_1.txt", "r") as f:
    text = f.read()

print("sum = ", sum(int(item) for item in text.split(" ") if item.isdigit()))



