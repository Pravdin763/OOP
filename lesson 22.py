#22. Наследование. Функция super() и делегирование

class Geom:
    name = 'Geom'

    def __init__(self, x, y, z):
        print(f'Инициализатор Geom для {self.__class__}')
        self.x = x
        self.y = y
        self.z = z


class Line(Geom):

    def drow(self):
        print('Рисование линии')


class Rect(Geom):
    def __init__(self, x, y, z, fill= None):
        super().__init__(x, y, z)               # Вызывает инициализатор из класса Geom
        print('Инициализатор класса Rect')
        self.fill = fill


    def drow(self):
        print('Рисование прямоугольника')



l = Line(0, 3, 11)
print(l.__dict__)
r = Rect(10, 20, 30)
print(r.__dict__)