class ZeroDivisionErrorMy(Exception):
    def __init__(self):
        super().__init__("ZeroDivisionErrorMy")


value1 = input("Enter the first number ")
value2 = input("Enter the second number ")

try:
    if value2.isdigit() and int(value2) == 0:
        raise ZeroDivisionErrorMy
    print(int(value1)/int(value2))
except Exception as ex:
    print(ex)
