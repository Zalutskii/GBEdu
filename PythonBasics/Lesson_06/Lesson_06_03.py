class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


position = Position("Ivan", "Z", "Eng", {"wage": 125, "bonus": 543})
print("Full name = ", position.get_full_name())
print("Result = ", position.get_total_income())
