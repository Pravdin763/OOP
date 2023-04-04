#15. Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие

#   __eq__() - ==
#   __ne__() - !=
#   __lt__() -  <
#   __le__() - <=
#   __gt__() - >
#   __ge__() - >=
# Достаточно 3 метода, будут работать (==, !=), (>, <), (>=, ,<=)

class Clock:
    __DAY = 86400   # колличество секунд в 1 дне
    def __init__(self, seconds):
        if not isinstance(seconds, int):
            raise TypeError('секунты долдны быть числами')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verifydata__(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('тип должен быть int или Clock')
        return other if isinstance(other, int) else other.seconds


    def __eq__(self, other):            # ПЕРЕОПРЕДЕЛИЛИ ПОВЕДЕНИЕ, ТЕПЕРЬ СРАВНИВАЮТСЯ НЕ АЙДИШНИКИ (id) экземпляров, а переданные аргументы!
        sc = self.__verifydata__(other) # вызов классметод, чтобы не было дублирования !
        return self.seconds ==sc

    def __lt__(self, other):            # ПЕРЕОПРЕДЕЛИЛИ ПОВЕДЕНИЕ, ТЕПЕРЬ СРАВНИВАЮТСЯ НЕ АЙДИШНИКИ (id) экземпляров, а переданные аргументы!
        sc = self.__verifydata__(other) # вызов классметод, чтобы не было дублирования !
        return self.seconds < sc

    def __ge__(self, other):            # ПЕРЕОПРЕДЕЛИЛИ ПОВЕДЕНИЕ, ТЕПЕРЬ СРАВНИВАЮТСЯ НЕ АЙДИШНИКИ (id) экземпляров, а переданные аргументы!
        sc = self.__verifydata__(other)     # вызов классметод, чтобы не было дублирования !
        return self.seconds >= sc

c1 = Clock(1000)
c2 = Clock(1000)
print(c1 ==c2)  # сравниваются id экземпляров классов   ИЗНАЧАЛЬНО
print(id(c1), id(c2))
print(c1 > c2)
print(c2>=c1)
