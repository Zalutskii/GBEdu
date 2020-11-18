class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_mass(self, mass, height):
        return self.__length * self.__width * height * mass


road = Road(20, 5000)
print("Result = ", road.calculate_mass(25, 5))
