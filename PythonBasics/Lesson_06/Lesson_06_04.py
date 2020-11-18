class Car:
    speed = 0
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self):
        self.speed = 30
        print(f"{self.name} Going")
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f"{self.name} Stopped")
        self.show_speed()

    def turn(self, direction):
        print(f"{self.name} Turned, direction = {direction}")

    def show_speed(self):
        print(f"{self.name} Speed = {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} Speed > 60")
        super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Speed > 60, current speed", self.speed)
        else:
            print("Speed ", self.speed)


class PoliceCar(Car):
    pass


townCar = TownCar("red", "townCar")
townCar.stop()
townCar.go()
townCar.speed = 90
townCar.show_speed()

sportCar = SportCar("red", "sportCar")
sportCar.stop()
sportCar.go()
sportCar.speed = 90
sportCar.show_speed()


