#20. Наследование в объектно-ориентированном программировании
# https://www.youtube.com/watch?v=7WVYqjdMa6U&ab_channel=selfedu

class Geom:
    name = 'Geom'
    def set_coords(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
    def drow(self):
        print('Базовый класс')


class Lime(Geom):       # Geom - родительский, lime - дочерний. ИЗ lime можем вызвать атрибуты базового класса Geom
    def drow(self):
        print('Рисование линии')


class Rect(Geom):       # Geom - родительский, Rect - дочерний. ИЗ Rect можем вызвать атрибуты базового класса Geom
    name = 'Я класс Rect'
    pass


l = Lime()
      # Geom

r = Rect()
g = Geom()
r.set_coords(1, 2)
print(r.__dict__)
l.set_coords(3, 4)
print(l.__dict__)
g.drow()    # атрибут в тоже базовом классе
l.drow()    # атрибут есть в классе lime
r.drow()    # атрибута нет в классе rect, ищет в базовом классе geom
print(g.name)   # в базовом классе
print(r.name)   # переопределение, есть в классе Rect
print(l.name)   # нет атрибута в lime, ищет в базовом geom