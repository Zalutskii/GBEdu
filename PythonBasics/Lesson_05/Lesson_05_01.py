with open("Lesson_05_01.txt", "w+") as file_:
    while True:
        input_str = input("Write text (empty for exit) ")
        if input_str == "":
            break
        else:
            file_.write(f"{input_str}\n")

