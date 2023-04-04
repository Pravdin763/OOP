#6. Режимы доступа public, private, protected. Сеттеры и геттеры
# https://www.youtube.com/watch?v=RipfqbH0eqY&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=7&ab_channel=selfedu
class Point:
    def __init__(self, x=0, y=0, z=0, h=0):
        self.__h = 0
        if all([self.__checkvalue(i) for i in (x, y, z, h)]):
            self.x = x
            self.y =y
            self._z = z
            self.__h = h

    @classmethod
    def __checkvalue(cls, num):                 # private ный метод, который проверяет корректность атрибутов
        return isinstance(num, (int, float))

    def set_coord(self, x, y, z, h):        # set и get работают с защищенными локальными атрибутами _ и __
        if all([self.__checkvalue(i) for i in (x, y, z, h)]):
            self.x = x
            self.y = y
            self._z = z
            self.__h = h

    def get_coord(self):                    # set и get работают с защищенными локальными атрибутами _ и __
        return self.x, self.y , self._z, self.__h


pt = Point(1, 2, 7, 10)
print(pt.x, pt.y)
print(pt._z)        # Protected ошибки не будет
#print(pt.__h)      Вызовет ошибку, мы не можем обратиться к private


"""Мехагизм Инкапсуляции"""
# 1. Public (Публичное (обычное) свойство)
# 2. Protected (_ одно подчеркивание) - служит для обращения внутри класса и в дочерних классах (ниче не меняет)
# 3. private (__ два подчеркивания)  - служит для обращения только внутри класса

# dir() метод который выводит список ВСЕХ атрибутов, в том числе приватных! __

print()
pt.set_coord(10, 20, 30, 40)
print(pt.get_coord(), ', вызов через метод get_coord')
print(dir(pt))