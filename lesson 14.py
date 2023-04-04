#14 Магические методы __add__, __sub__, __mul__, __truediv__
# https://www.youtube.com/watch?v=OMMQ1ZNKK6Q&ab_channel=selfedu

# __add__() - сложение
#.__sub__() -   вычитание
# __mul__() -   кмножение
# __truediv__() - деление

class Clock:
    __DAY = 86400 # число секунд в 1 дне
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('секунты долдны быть числами')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds //60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__getformated(h)}:{self.__getformated(m)}:{self.__getformated(s)}'

    @classmethod
    def __getformated(cls, x):
        return str(x).rjust(2, '0')     # добавляет 0 ко времени

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('праввый операнд должен быть int или Clock')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):      # метод если int + экземпляр класса
        return self + other

    def __iadd__(self, other):      # для работы += или -= итд
        print('__iadd__')
        if not isinstance(other, (int, Clock)):
            sc = other.seconds
        self.seconds += sc
        return self


c1 = Clock(1000)
c2 = Clock(2000)
c3 = c1 + 100
c4 = c1 + c2
print(c3.get_time())
print(c4.get_time())

c5 = c2 + 222
print(c5.get_time())