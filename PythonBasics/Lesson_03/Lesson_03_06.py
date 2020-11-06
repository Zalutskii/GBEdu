def int_func(string):
    return string.capitalize()


text = input("Enter string")
print(' '.join(int_func(s) for s in text.split(" ")))
