#17. Магический метод __bool__ определения правдивости объектов
# https://www.youtube.com/watch?v=a2L5vyCUvzo&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=18&ab_channel=selfedu

class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__')
        return self.x**2 + self.y**2

    def __bool__(self):     # приоритет по bool     ВОЗВРАЩАЕТ ТОЛЬКО TRUE или FAlse
        print('__bool__')
        return self.x ==self.y


p1 = Point(1, 2)
p2 = Point(0, 0)
print(bool(p1))     # bool всегда возвращает True для всех объектов класса
print(bool(p2))
p3 = Point(10, 10)
print(bool(p3))