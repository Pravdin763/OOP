#5. Методы класса (classmethod) и статические методы (staticmethod)
# https://www.youtube.com/watch?v=78PTvj2wYH8&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=6&ab_channel=selfedu

class Vector:

    min_coord = 0       # атрибуты класса
    max_coord = 100     # атрибуты класса

    @classmethod                # Работает ИСКЛЮЧИТЕЛЬНО с АТРИБУТАМИ КЛАССА (НЕ функциями)
    def validate(cls, arg):
        return cls.min_coord <= arg <= cls.max_coord


    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and self.validate(y):       # Можно через класс Vector или self, лучше self!!!
            self.x = x
            self.y = y

        print('вызов staticmethod внутри класса: ', self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod           # следует использовать ТОЛЬКО те параметры, которые объявлены внутри класса
    def norm2(x, y):
        return x*x + y*y

dp = Vector(1, 2)
res = dp.get_coord()                # одно и тоже, разный синтаксис
print('Координаты dp х, у: ', res,  Vector.validate(1), Vector.validate(2))
res2 = Vector.get_coord(dp)         # одно и тоже, разный синтаксис  (обязательно в скобках экземпляр класса)
print('Координаты dp х, у: ', res2)


print(Vector.validate(5))       # True
print(Vector.validate(-3))      # False


dp2 = Vector(-3, 200)
res3 = dp2.get_coord()
print('Координаты dp2: ', res3, Vector.validate(-3), Vector.validate(200))      # Кооридинаты 0, 0 тк -3 и 200 не проходят проверку validate

print(Vector.norm2(5, 6), ', через staticmethod')