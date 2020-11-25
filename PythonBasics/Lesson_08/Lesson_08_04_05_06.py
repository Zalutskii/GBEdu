class OfficeEquipment:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width


class Printer(OfficeEquipment):
    def __init__(self, height: int, width: int, is_laser: bool):
        super().__init__(height, width)
        self.isLaser = is_laser


class Scanner(OfficeEquipment):
    def __init__(self, height: int, width: int, speed: int):
        super().__init__(height, width)
        self.speed = speed


class Storage:
    def __init__(self):
        self.dict = {}
        pass

    def pull(self, equipment: OfficeEquipment, count: int):
        self.dict[equipment] = count

    def push(self, equipment: OfficeEquipment, count: int):
        value = self.dict.get(equipment, 0)
        if value < count:
            raise Exception("there is no such equipment in Storage")
        else:
            self.dict[equipment] = value - count


storage = Storage()
Printer1 = Printer(12, 13, True)
Printer2 = Printer(22, 23, False)
Scanner1 = Scanner(1, 2, 3)
Scanner2 = Scanner(3, 4, 5)

storage.pull(Printer1, 10)
storage.pull(Printer2, 10)
storage.pull(Scanner1, 10)
storage.pull(Scanner2, 10)

try:
    storage.push(Scanner2, 5)
except Exception as ex:
    print(ex)

print(storage.dict)

