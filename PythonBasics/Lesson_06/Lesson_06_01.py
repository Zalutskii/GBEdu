from time import sleep


class TrafficLight:
    __color_dic = {"Red": 7, "Yellow": 2, "Green": 5}
    __current_color = "Red"

    def running(self):
        for key, value in self.__color_dic.items():
            print(key)
            sleep(value)


traffic_light = TrafficLight()
traffic_light.running()
print("End program")
