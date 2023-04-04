#23. Наследование. Атрибуты private и protected |

class Geom:
    name = 'Geom'       # К приватным атрибутам __ можно обращаться ТОЛЬКО из БАЗОВОГО КЛАССА! из дочерних, ошибка!

    def __init__(self, x, y, z):
        print(f'Инициализатор класса {self.__class__}')
        self._verify(x)
        self.__x = x
        self.__y = y
        self._z = z

    def get_coords(self):
        return (self.__x, self.__y)

    def _verify(self, coord):       # ЕСли 2 __ подчеркивания, у нас он есть в Rect, то будет ошибка, т.к. React Дочерний!
        return 0 < coord < 100


class Rect(Geom):
    def __init__(self, x, y , z, fill=None):
        super().__init__(x, y, z)
        self.__fill = fill
        self._verify(x)

    def get_coordsRect(self):
        return self._z



r = Rect(0, 10 ,20)
print(r.__dict__)
r.get_coords()
print(r._z)     # не стоит так обращаться напрямую к _

