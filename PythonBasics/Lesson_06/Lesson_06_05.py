class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print(f"Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки Pen, title = {self._title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки Pencil, title = {self._title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки Handle, title = {self._title}")


pen = Pen("Pen")
pen.draw()

pencil = Pencil("Pencil")
pencil.draw()

handle = Handle("Handle")
handle.draw()
