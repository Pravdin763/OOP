#13. Магические методы __str__, __repr__, __len__, __abs__
# https://www.youtube.com/watch?v=Aabdr3yxEhQ&ab_channel=selfedu
class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):             # для внутренних данных.  ДОЛЖЕН ВЫВОДИТЬ СТРОКУ!  __class__ - имя класса
        return f'{self.__class__}: {self.name}'

    def __str__(self):              # для пользователя. Выводит через print
        return f'{self.name}'

c = Cat('Васька')
c           # __repr__ вывод в косоли
print(c)    # __str__ вывод для пользователя, через принт

print()

class Point:
    def __init__(self, *args):
        self.__coords = args        # список координат

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))

p = Point(1, -2)
print(len(p))
p2= Point(5, -7, 9)
print(len(p2))
print(abs(p))
print(abs(p2))