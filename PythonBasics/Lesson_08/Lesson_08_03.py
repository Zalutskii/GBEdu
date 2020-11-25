class NotDigitErrorMy(Exception):
    def __init__(self):
        super().__init__("NotDigitErrorMy")


value_list = []

while True:
    input_str = input("add new number (q for Exit)")
    if input_str == "q":
        break
    else:
        try:
            if not input_str.isdigit():
                raise NotDigitErrorMy
            value_list.append(int(input_str))
        except Exception as ex:
            print(ex)

print(value_list)

