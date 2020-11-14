with open('Lesson_05_04_1.txt') as file_:
    num_lines = sum(1 for line in file_)
print(num_lines)
