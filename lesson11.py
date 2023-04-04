#11. Дескрипторы (data descriptor и non-data descriptor)

# https://www.youtube.com/watch?v=ACqsYPbgePk&ab_channel=selfedu

class Integer:                          # весь этот код делает тоже салое, что ниже в коментах, но намного компактнее!
    @classmethod
    def verifynum(cls, num):            # проверяет каждое число
        if type(num) != int:
            raise TypeError('Координата должна быть целым числом!')

    def __set_name__(self, owner, name):    # self - ссылка на создаваемый экземпляр класса, owner - ссылка на класс Point3d, name - имя (х, у, z)
        self.name = '_'+name    # name - строка     name = (_x, _y, _z)

    def __get__(self, instance, owner):      #   instance - ссылка на экземпляр класса Point3d (p, p2), ownner - ссылка на класс Point3d
        return instance.__dict__[self.name]     # выводим значение атрибута (1, 2, 3)
        # return getattr(instance, self.name)   # тоже самое, предпочтительный вариант

    def __set__(self, instance, value):     #   instance - ссылка на ЭКЗЕМПЛЯР класса Point3d (p, p2), value - значение (1, 2, 3)
        self.verifynum(value)               # запускаем проверку значения
        print('__set__:', self.name, '=', value)
        instance.__dict__[self.name] = value        # создаем в ЭКЗЕМПЛЯРЕ класса свойство (_x: 1, _y: 2, _z: 3)
        # setattr(instance, self.name, value)       # тоже самое, предпочтительный вариант

class Point3d:
    x = Integer()       # каждый элемент преердаем в класс integer, для проверки и инициализации геттеров и сеттеров
    y = Integer()
    z = Integer()

    def __init__(self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z



    # @property                 # Без дексриптоов. Повторять для каждого атрибута.....
    # def x(self):
    #     return self._x
    #
    # @x.setter
    # def x(self, num):
    #     self.verifynum(num)
    #     self._x = num
    #
    # @property
    # def y(self):
    #     return self._y
    #
    # @y.setter
    # def y(self, num):
    #     self.verifynum(num)
    #     self._y = num
    #
    # @property
    # def z(self):
    #     return self._z
    #
    # @z.setter
    # def z(self, num):
    #     self.verifynum(num)
    #     self._z = num


p = Point3d(1, 2, 3)
print(p.__dict__)

p2 = Point3d(5, 7, '20')    # будет ошибка, из за проверки verifynum
print(p2.__dict__)