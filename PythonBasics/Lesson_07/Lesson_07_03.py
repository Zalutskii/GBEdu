class Organic:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, next_val):
        return Organic(self.count + next_val.count)

    def __sub__(self, next_val):
        if self.count < next_val.count:
            print("the second cell is larger than the first")
        else:
            return Organic(self.count - next_val.count)

    def __mul__(self, next_val):
        return Organic(self.count * next_val.count)

    def __truediv__(self, next_val):
        return Organic(int(self.count / next_val.count))

    def __str__(self):
        return f"Organic cell with count {self.count}"

    def make_order(self, cells_in_line):
        return "".join(str("*" * cells_in_line+"\n") for l in range(int(self.count / cells_in_line))) + "*" * (self.count % cells_in_line)


cell1 = Organic(13)
cell2 = Organic(18)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell2 / cell1)

print(cell1.make_order(5))
print(cell2.make_order(6))
