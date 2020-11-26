class Clothes:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def calculate_mass(self, mass, height):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        self._name = name
        self._v = v

    def calculate_consumption(self):
        return self._v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        self._name = name
        self._h = h

    def calculate_consumption(self):
        return 2 * self._h + 0.3


clothes = [Coat("Coat1", 11), Coat("Coat2", 12), Coat("Coat3", 13),
           Coat("Suit1", 14), Coat("Suit2", 15), Coat("Suit3", 16), ]

for cloth in clothes:
    print(F"Consumption for {cloth.name} = {cloth.calculate_consumption()}")
