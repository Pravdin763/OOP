#21. Функция issubclass(). Наследование от встроенных типов и от object
# https://www.youtube.com/watch?v=JTmb2QHZUGg&ab_channel=selfedu

class Geom:             # Любой класс наследуется от класса Object
    pass

class Lime(Geom):
    pass


print(Geom.__name__)

g = Geom()
l = Lime()
print(g)
print(l.__class__)
print(issubclass(Lime, Geom))   # True Лайм наследуется от Геома    № issubclass Проверяет ТОЛЬКО наследование КЛАССОВ, а не их экземпляров!
print(issubclass(Geom, Lime))   # А не наоборот     № issubclass Проверяет ТОЛЬКО наследование КЛАССОВ, а не их экземпляров!

print(isinstance(l, Geom))  # тут можно проверять экземпляры класса

print(isinstance(int, object))  # int тоже класс
print()

class Vector(list):             # list тоже класс
    def __str__(self):          # переопределили маг. метод str
        return '~'.join(map(str, self))

v = Vector([1, 2, 3, 4])
print(v)