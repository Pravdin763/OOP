#7. Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__ |
# https://www.youtube.com/watch?v=CAx-NLFc-Z4&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=8&ab_channel=selfedu

class Point():

    min_coord = 0       # Атрибуты класса являются общими для всех его экземпляров
    max_coord = 100

    def __init__(self, x, y):
        self.x = x
        self.y =y

    def set_decord(self, x, y):
        if self.min_coord <= x <=self.max_coord and self.min_coord <= y <=self.max_coord:
            self.x = x
            self.y = y

    @classmethod                # с помощю него поменяли значение в классе Point
    def set_bound(cls, left):
        cls.min_coord =left

    def __getattribute__(self, item):
        print('__getattribute__')
        if item == 'z':
            raise ValueError('мне не ziганутые!')
        else:
            return object.__getattribute__(self, item)      # без return возвращает None

    def __setattr__(self, key, value):
        print('__setattr__')
        if key =='z' or key =='v':                      # если создаем имя z или v
            raise AttributeError('z v - залупа ватная')     # то ошибка
        else:
            object.__setattr__(self, key, value)        # или все ок

    def __getattr__(self, item):            # Если атрибута нет
        print('__getattr__:', item)         # выводит это и потом None, если атрибут есть, то выведет его значение
        return False    # необязательно, выведет иначе None

    def __delattr__(self, item):
        print('__delattr__:', item)
        object.__delattr__(self, item)

pt1 = Point(1, 2)
pt2 = Point(11, 22)
print(pt1.max_coord)
pt1.set_bound(-110)             # меняем значение в Point
print('pt1: ', pt1.__dict__, 'Point: ', Point.__dict__)
print(Point.min_coord)

#pt2.z = 3       # выведет ошибку __setattr__    AttributeError('z v - залупа ватная')
print()
print(pt1.puylo)

print()
del pt1.x
print(pt1.__dict__)

#  __setattr__ (self, key, value) - автоматически вызывается при изменении атрибута класса key = имя атрибута value = значение атрибута
# __getattribute__(self, item) - автоматически вызывается при получении свойств класса
# __getattr__ (self, item) - автоматически вызывается при получении несуществующего свойства (атрибута) класса
# __delattr__(self, item) - автоматически вызывается при удалении свойств класса (не важно существует оно или нет)
# object - от него наследуются все классы в пайтон! (самый базовый класс!)