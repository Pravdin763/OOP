#27. Как работает __slots__ с property и при наследовании

class Point:
    __slots__ = ('x', 'y', '__lenght')      # __slots__ запрещает ТОЛЬКО локальные свойства(атрибуты) класса

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__lenght = (x * x + y * y) * 0.5

    @property
    def lenght(self):           # это атрибут, а не локальное свойство, поэтому __slots__ не распространяется
        return self.__lenght

    @lenght.setter              # это атрибут, а не локальное свойство, поэтому __slots__ не распространяется
    def lenght(self, value):
        self.__lenght = value

class Point2(Point):
    pass

class Point3(Point):
    __slots__ = ()

pt = Point(2, 3)
print(pt.lenght)    # Появляется сам
pt.lenght = 10      # разрешает изменить через сеттер
print(pt.lenght)

print()

pt2 = Point2(10, 20)
pt2.z = 30
print(pt2.__dict__)     # x и y не попадают     # __slots__ не наследуется от базового класса, в данном случае Point, т.е. в Point2 ограничений нет!

pt3 = Point3(2, 3)      # x и y из базового класса
#pt3.z = 4               # Ошибка! в Point3 тоже есть slots и он пустой!