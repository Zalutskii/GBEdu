class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def get_numbers(cls, date: str):
        if Date.validate(date):
            return [int(i) for i in date.split('-')]

    @staticmethod
    def validate(date: str):
        val = date.split('-')
        if len(val) != 3:
            return False
        if not val[2].isdigit():
            return False
        if not val[1].isdigit():
            return False
        month = int(val[1])
        if month < 1 or month > 12:
            return False
        if not val[0].isdigit():
            return False
        if int(val[0]) < 1 or int(val[0]) > 31:
            return False
        return True


date = Date("1.12.2020")
print(date.get_numbers(date.date))

date = Date("1-12-2020")
print(date.get_numbers(date.date))

date = Date("1-13-2020")
print(date.get_numbers(date.date))
